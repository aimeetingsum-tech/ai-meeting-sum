import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
import pandas as pd
from datetime import datetime

from app.database import (
    init_db, save_meeting, get_meeting, list_meetings,
    search_meetings, get_all_action_items, update_action_item_status, get_stats
)
from app.summarizer import summarize_meeting
from app.templates import get_meeting_types, get_meeting_type_icon
from app.utils import parse_transcript_file, truncate_text

# Initialize
init_db()

st.set_page_config(
    page_title="MeetingMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header { font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem; }
    .sub-header { color: #666; margin-bottom: 2rem; }
    .metric-card {
        background: #f8f9fa; border-radius: 10px; padding: 1.2rem;
        text-align: center; border: 1px solid #e9ecef;
    }
    .metric-value { font-size: 2rem; font-weight: 700; color: #1f77b4; }
    .metric-label { color: #666; font-size: 0.85rem; }
    .action-item-card {
        background: #fff; border-radius: 8px; padding: 1rem;
        border-left: 4px solid #1f77b4; margin-bottom: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .decision-badge {
        background: #e8f4fd; color: #1f77b4; padding: 0.3rem 0.8rem;
        border-radius: 15px; display: inline-block; margin: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## 🧠 MeetingMind AI")
st.sidebar.markdown("*The privacy-first meeting summarizer*")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    ["📤 Upload & Summarize", "📊 Dashboard", "🔍 Search", "✅ Action Items"],
    label_visibility="collapsed"
)

# ─── PAGE 1: Upload & Summarize ──────────────────────────────────────────────
if page == "📤 Upload & Summarize":
    st.markdown('<div class="main-header">Upload & Summarize</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Upload a meeting transcript to get an AI-powered summary with action items.</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        meeting_title = st.text_input("Meeting Title", placeholder="e.g., Q2 Sprint Planning")
    with col2:
        meeting_types = get_meeting_types()
        meeting_type = st.selectbox(
            "Meeting Type",
            options=list(meeting_types.keys()),
            format_func=lambda x: f"{get_meeting_type_icon(x)} {meeting_types[x]}"
        )
    with col3:
        platform = st.selectbox("Source Platform", ["Zoom", "Google Meet", "Microsoft Teams", "Other"])

    uploaded_file = st.file_uploader(
        "Upload Transcript",
        type=["txt", "srt", "vtt"],
        help="Supported formats: .txt, .srt (SubRip), .vtt (WebVTT)"
    )

    # Option to paste transcript directly
    with st.expander("Or paste transcript directly"):
        pasted_text = st.text_area("Paste meeting transcript here", height=200)

    if st.button("🚀 Summarize Meeting", type="primary", use_container_width=True):
        transcript = ""
        if uploaded_file:
            transcript = parse_transcript_file(uploaded_file)
        elif pasted_text.strip():
            transcript = pasted_text.strip()

        if not transcript:
            st.error("Please upload a file or paste a transcript.")
        elif not meeting_title.strip():
            st.error("Please enter a meeting title.")
        else:
            with st.spinner("🧠 AI is analyzing your meeting..."):
                try:
                    result = summarize_meeting(transcript, meeting_type)

                    meeting_id = save_meeting(
                        title=meeting_title.strip(),
                        meeting_type=meeting_type,
                        transcript=transcript,
                        summary=result["summary"],
                        key_decisions=result["key_decisions"],
                        follow_ups=result["follow_ups"],
                        action_items=result["action_items"],
                        platform=platform.lower().replace(" ", "_")
                    )

                    st.success(f"Meeting summarized and saved! (ID: {meeting_id})")

                    # Display results
                    st.markdown("### 📝 Summary")
                    st.markdown(result["summary"])

                    st.markdown("### 🎯 Key Decisions")
                    for decision in result["key_decisions"]:
                        st.markdown(f'<span class="decision-badge">{decision}</span>', unsafe_allow_html=True)

                    st.markdown("### ✅ Action Items")
                    if result["action_items"]:
                        for item in result["action_items"]:
                            st.markdown(f"""
                            <div class="action-item-card">
                                <strong>{item['description']}</strong><br/>
                                👤 <em>{item.get('owner', 'Unassigned')}</em> &nbsp;|&nbsp;
                                📅 <em>{item.get('deadline', 'TBD')}</em>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.info("No action items extracted.")

                    st.markdown("### 💡 Follow-up Suggestions")
                    for followup in result["follow_ups"]:
                        st.markdown(f"- {followup}")

                except Exception as e:
                    st.error(f"Error during summarization: {str(e)}")
                    st.info("Make sure your GEMINI_API_KEY is set in the .env file.")

# ─── PAGE 2: Dashboard ───────────────────────────────────────────────────────
elif page == "📊 Dashboard":
    st.markdown('<div class="main-header">Meeting Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Overview of all your processed meetings.</div>', unsafe_allow_html=True)

    stats = get_stats()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-value">{stats['total_meetings']}</div>
            <div class="metric-label">Total Meetings</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-value">{stats['total_actions']}</div>
            <div class="metric-label">Total Action Items</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-value">{stats['pending_actions']}</div>
            <div class="metric-label">Pending Actions</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-value">{get_meeting_type_icon(stats['top_meeting_type'])}</div>
            <div class="metric-label">Most Common: {stats['top_meeting_type']}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Recent Meetings")

    meetings = list_meetings()
    if not meetings:
        st.info("No meetings processed yet. Go to 'Upload & Summarize' to get started!")
    else:
        for m in meetings:
            icon = get_meeting_type_icon(m["meeting_type"])
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            with col1:
                st.markdown(f"**{icon} {m['title']}**")
            with col2:
                st.caption(m["meeting_type"])
            with col3:
                st.caption(m["created_at"][:16] if m["created_at"] else "")
            with col4:
                st.caption(f"{m['action_count']} actions")

            if st.button("View Details", key=f"view_{m['id']}"):
                detail = get_meeting(m["id"])
                if detail:
                    st.markdown(f"#### Summary")
                    st.markdown(detail["summary"])
                    st.markdown(f"#### Key Decisions")
                    for d in detail["key_decisions"]:
                        st.markdown(f"- {d}")
                    st.markdown(f"#### Action Items")
                    for a in detail["action_items"]:
                        status_icon = "✅" if a["status"] == "done" else "⬜"
                        st.markdown(f"{status_icon} **{a['description']}** — {a.get('owner', 'Unassigned')} (Due: {a.get('deadline', 'TBD')})")
                    st.markdown(f"#### Follow-ups")
                    for f in detail["follow_ups"]:
                        st.markdown(f"- {f}")

# ─── PAGE 3: Search ──────────────────────────────────────────────────────────
elif page == "🔍 Search":
    st.markdown('<div class="main-header">Search Meetings</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Search across all your meeting transcripts, summaries, and decisions.</div>', unsafe_allow_html=True)

    query = st.text_input("🔍 Search", placeholder="e.g., budget approval, Q2 targets, deployment plan")

    if query:
        results = search_meetings(query)
        if results:
            st.markdown(f"**{len(results)} result(s) found**")
            for r in results:
                icon = get_meeting_type_icon(r["meeting_type"])
                with st.container():
                    st.markdown(f"### {icon} {r['title']}")
                    st.caption(f"{r['meeting_type']} | {r['source_platform']} | {r['created_at'][:16]}")
                    if r.get("snippet"):
                        st.markdown(r["snippet"], unsafe_allow_html=True)
                    if st.button("View Full Meeting", key=f"search_{r['id']}"):
                        detail = get_meeting(r["id"])
                        if detail:
                            st.markdown(detail["summary"])
                    st.markdown("---")
        else:
            st.info("No results found. Try different keywords.")

# ─── PAGE 4: Action Items ────────────────────────────────────────────────────
elif page == "✅ Action Items":
    st.markdown('<div class="main-header">Action Items Tracker</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Track and manage action items across all meetings.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        status_filter = st.selectbox("Filter by Status", ["All", "Pending", "Done"])
    with col2:
        owner_input = st.text_input("Filter by Owner", placeholder="Leave blank for all")

    sf = None if status_filter == "All" else status_filter.lower()
    of = owner_input.strip() if owner_input.strip() else None
    items = get_all_action_items(status_filter=sf, owner_filter=of)

    if not items:
        st.info("No action items found matching your filters.")
    else:
        st.markdown(f"**{len(items)} action item(s)**")
        for item in items:
            col1, col2, col3, col4 = st.columns([0.5, 4, 2, 2])
            with col1:
                is_done = item["status"] == "done"
                new_status = st.checkbox(
                    "done", value=is_done, key=f"action_{item['id']}",
                    label_visibility="collapsed"
                )
                if new_status != is_done:
                    update_action_item_status(item["id"], "done" if new_status else "pending")
                    st.rerun()
            with col2:
                style = "text-decoration: line-through; color: #999;" if item["status"] == "done" else ""
                st.markdown(f'<span style="{style}">{item["description"]}</span>', unsafe_allow_html=True)
            with col3:
                st.caption(f"👤 {item.get('owner') or 'Unassigned'}")
            with col4:
                st.caption(f"📅 {item.get('deadline') or 'TBD'} | From: {item['meeting_title']}")
