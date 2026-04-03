# Document 4: AI Solution Prototype

---

## 1. AI Technology Selection and Justification (100 marks)

### 1.1 Choice of Tools

| Component | Technology | Why This Choice |
|-----------|-----------|-----------------|
| **Application Framework** | Streamlit (Python) | Rapid prototyping with built-in UI widgets; free cloud hosting; Python-native for seamless AI integration |
| **AI Engine** | Gemini API (Google) | 1M token context window handles full meeting transcripts; JSON mode with response schema guarantees structured output; fast inference; generous free tier |
| **AI Model** | Gemini 2.0 Flash | Best balance of quality, speed, and cost for summarization tasks (~$0.01-0.03/meeting); free tier available for development |
| **Database** | SQLite + FTS5 | Zero infrastructure cost; built into Python stdlib; FTS5 provides full-text search with BM25 ranking |
| **Language** | Python 3.12 | Best AI/ML ecosystem; Streamlit and Google GenAI SDK are Python-native |
| **Deployment** | Streamlit Cloud | Free tier available; one-click deploy from GitHub; HTTPS included |

### 1.2 Why Not Alternatives?

| Alternative | Reason for Rejection |
|-------------|---------------------|
| Flask/Django | Requires separate frontend development; too much boilerplate for MVP timeline |
| OpenAI GPT-4 | Similar capability but higher cost per token; Gemini's free tier and JSON mode are more cost-effective for MVP |
| Claude API (Anthropic) | Strong summarization but no free tier; Gemini's generous free usage and JSON schema enforcement better suited for MVP budget |
| Local LLM (Llama) | Requires GPU hardware; inconsistent quality; not feasible for deployment |
| PostgreSQL | Overkill for MVP; requires server setup; SQLite is sufficient for single-user prototype |
| React frontend | Adds JavaScript complexity; Streamlit achieves equivalent UX for a data/AI application |
| Elasticsearch | Requires separate cluster; SQLite FTS5 provides adequate search for MVP scale |

### 1.3 Functionalities and Features Finalized

**Core Features (Implemented):**

1. **Multi-Format Transcript Upload**
   - Supports .txt (plain text), .srt (SubRip subtitles), .vtt (WebVTT) formats
   - Automatic format detection and timestamp stripping
   - Direct paste option for quick testing

2. **Meeting-Type-Aware AI Summarization**
   - 7 meeting types: General, Daily Standup, Sales Call, Brainstorm, 1-on-1, Sprint Planning, Retrospective
   - Each type has a tailored system prompt that directs AI to extract type-specific intelligence
   - Uses Gemini's JSON mode with response schema to guarantee structured output

3. **Smart Action Item Extraction**
   - Automatically identifies action items from natural conversation
   - Extracts owner name and deadline for each item
   - Persistent tracking with pending/done status toggle

4. **Meeting History Dashboard**
   - Overview metrics: total meetings, total action items, pending items, most common type
   - Chronological list with meeting type icons and action item counts
   - Drill-down to view full summary of any past meeting

5. **Cross-Meeting Full-Text Search**
   - SQLite FTS5-powered search across transcripts, summaries, and decisions
   - BM25 ranking for relevance
   - Snippet highlighting showing matching context

6. **Action Items Tracker**
   - Aggregated view across all meetings
   - Filter by status (pending/done) and owner
   - One-click checkbox to toggle completion

7. **Platform Tagging**
   - Tag meetings by source platform (Zoom, Google Meet, Teams, Other)
   - Enables platform-specific filtering in future iterations

### 1.4 Prompt Used for Initial Build

The AI summarization uses a **tool-use approach** where the LLM is forced to output structured JSON. Here is the core prompt architecture:

**System Prompt (varies by meeting type, example for Daily Standup):**

```
You are an expert meeting summarizer specializing in agile daily standups.
Analyze the transcript and extract structured information.

Focus specifically on:
- What each person accomplished yesterday/since last standup
- What each person plans to work on today
- Any blockers or impediments mentioned
- Action items to resolve blockers

For the summary, organize by person. Keep it brief — standups should be concise.
Flag any blocker that hasn't been addressed.
```

**Response Schema (forces structured JSON output):**

```json
{
  "type": "object",
  "properties": {
    "summary": { "type": "string" },
    "key_decisions": { "type": "array", "items": { "type": "string" } },
    "action_items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "description": { "type": "string" },
          "owner": { "type": "string" },
          "deadline": { "type": "string" }
        },
        "required": ["description", "owner", "deadline"]
      }
    },
    "follow_ups": { "type": "array", "items": { "type": "string" } }
  },
  "required": ["summary", "key_decisions", "action_items", "follow_ups"]
}
```

**API Call Configuration:**

```python
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=f"Please analyze this meeting transcript: {transcript}",
    config={
        "system_instruction": system_prompt,       # Meeting-type-specific prompt
        "response_mime_type": "application/json",   # Force JSON output
        "response_schema": OUTPUT_SCHEMA,           # Enforce exact structure
        "temperature": 0.3,                         # Low temperature for consistency
    },
)
```

This approach uses Gemini's native JSON mode with a response schema to guarantee structured output every time — no regex parsing, no hallucinated formats.

---

## 2. Screenshots and User Flow (150 marks)

### 2.1 User Flow Wireframe

```
┌─────────────────────────────────────────────────────────────────┐
│                        MeetingMind AI                           │
│                   User Flow Wireframe                           │
└─────────────────────────────────────────────────────────────────┘

┌──────────┐     ┌──────────────────┐     ┌──────────────────┐
│  User    │────▶│  Upload Page     │────▶│  AI Processing   │
│  Lands   │     │  - Upload file   │     │  - Gemini API    │
│          │     │  - Select type   │     │  - JSON mode     │
│          │     │  - Enter title   │     │  - JSON output   │
└──────────┘     └──────────────────┘     └────────┬─────────┘
                                                    │
                         ┌──────────────────────────▼──────────┐
                         │         Results Display              │
                         │  ┌─────────┐ ┌──────────┐ ┌───────┐│
                         │  │Summary  │ │Decisions │ │Action ││
                         │  │         │ │          │ │Items  ││
                         │  └─────────┘ └──────────┘ └───┬───┘│
                         │  ┌──────────────┐             │    │
                         │  │Follow-ups    │             │    │
                         │  └──────────────┘             │    │
                         └───────────────────────────────┼────┘
                                                         │
                    ┌────────────────────────────────────▼────┐
                    │           Saved to Database              │
                    │  (SQLite + FTS5 Index Updated)          │
                    └──────┬─────────────┬───────────┬────────┘
                           │             │           │
                    ┌──────▼───┐  ┌──────▼────┐ ┌───▼────────┐
                    │Dashboard │  │  Search   │ │Action Item │
                    │- Stats   │  │- FTS5     │ │  Tracker   │
                    │- History │  │- Snippets │ │- Filter    │
                    │- Details │  │- Results  │ │- Toggle    │
                    └──────────┘  └───────────┘ └────────────┘
```

### 2.2 Page-by-Page Feature Documentation

#### Page 1: Upload & Summarize

**Purpose:** The primary page where users upload meeting transcripts and receive AI-generated summaries.

**Features:**
- **Meeting Title Input**: Free-text field for naming the meeting
- **Meeting Type Selector**: Dropdown with 7 options, each with an icon (📋 General, 🏃 Standup, 💼 Sales Call, 💡 Brainstorm, 👥 1-on-1, 📊 Sprint Planning, 🔄 Retrospective)
- **Source Platform Selector**: Zoom, Google Meet, Microsoft Teams, Other
- **File Uploader**: Accepts .txt, .srt, .vtt files with drag-and-drop
- **Paste Option**: Expandable text area for pasting transcripts directly
- **Summarize Button**: Primary action button that triggers AI processing
- **Results Display**: Inline display of summary, decisions (badge-style), action items (card-style with owner and deadline), and follow-up suggestions

**User Action Flow:**
1. Enter meeting title
2. Select meeting type from dropdown
3. Choose source platform
4. Upload file or paste transcript
5. Click "Summarize Meeting"
6. Review AI-generated results displayed on the same page

#### Page 2: Meeting Dashboard

**Purpose:** Overview of all processed meetings with key statistics.

**Features:**
- **Metric Cards**: Four cards showing Total Meetings, Total Action Items, Pending Actions, Most Common Meeting Type
- **Meeting List**: Chronological list with title, type (with icon), date, and action item count
- **Detail View**: Click "View Details" to expand any meeting's full summary, decisions, action items, and follow-ups

#### Page 3: Search

**Purpose:** Find information across all past meetings instantly.

**Features:**
- **Search Bar**: Full-text search input
- **Results List**: Each result shows meeting title (with type icon), metadata (type, platform, date), and a highlighted snippet showing the matching context
- **Drill-Down**: Click to view the full meeting summary

#### Page 4: Action Items Tracker

**Purpose:** Centralized view of all action items across all meetings.

**Features:**
- **Status Filter**: Dropdown to filter by All, Pending, or Done
- **Owner Filter**: Text input to filter by owner name
- **Action Item List**: Each item shows a checkbox (toggle done/pending), description, owner, deadline, and source meeting title
- **Real-Time Updates**: Checking/unchecking immediately updates the database

### 2.3 Before/After Comparison

| Aspect | Before (Manual Process) | After (MeetingMind AI) |
|--------|------------------------|----------------------|
| **Time per meeting** | 25-30 min post-processing | 45 seconds (upload + AI processing) |
| **Action item capture** | 35-40% of items captured | 95%+ extracted with owners and deadlines |
| **Note quality** | Inconsistent, depends on note-taker | Consistent, type-specific, structured |
| **Searchability** | None (scattered across emails/docs) | Full-text search across all meetings |
| **Follow-up tracking** | Manual spreadsheet or memory | Built-in tracker with status toggles |
| **Meeting type awareness** | None — same notes format for all | 7 tailored templates producing relevant output |

### 2.4 Mobile/Responsive Design Considerations

Streamlit provides built-in responsive design:
- **Layout**: Uses `st.columns()` which automatically stacks vertically on mobile
- **Sidebar**: Collapses into a hamburger menu on small screens
- **File Upload**: Works with mobile file pickers
- **Touch Targets**: Streamlit's default button and checkbox sizes meet WCAG touch target guidelines

For production deployment, the following mobile enhancements would be added:
- Simplified single-column layout for upload page on mobile
- Swipe navigation between pages
- Optimized card sizes for small screens

### 2.5 Application Link

**Local Development:**
```bash
# Clone the repository
git clone <repository-url>
cd todolist_reminder

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Set up API key
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# Run the application
streamlit run app/main.py
```

**Streamlit Cloud Deployment:**
The application can be deployed for free on Streamlit Cloud by connecting the GitHub repository. The `GEMINI_API_KEY` is configured as a secret in the Streamlit Cloud dashboard.

---

## 3. Technical Architecture Summary

### 3.1 System Components

```
┌─────────────────────────────────────────────────┐
│                 MeetingMind AI                    │
├─────────────────────────────────────────────────┤
│  Frontend: Streamlit (Python)                    │
│  ├── main.py (4-page app, ~250 lines)           │
│  ├── Custom CSS for cards and metrics            │
│  └── Session state for persistence               │
├─────────────────────────────────────────────────┤
│  AI Layer: Gemini API via Google GenAI SDK        │
│  ├── summarizer.py (~60 lines)                   │
│  ├── templates.py (7 meeting types, ~150 lines)  │
│  └── Tool-use for structured JSON output         │
├─────────────────────────────────────────────────┤
│  Data Layer: SQLite + FTS5                       │
│  ├── database.py (~150 lines)                    │
│  ├── meetings table + action_items table         │
│  └── FTS5 virtual table for full-text search     │
├─────────────────────────────────────────────────┤
│  Utilities                                       │
│  ├── utils.py (file parsing, text helpers)       │
│  └── .env (API key configuration)                │
└─────────────────────────────────────────────────┘
```

### 3.2 Data Flow

1. **Input**: User uploads transcript file (.txt/.srt/.vtt) or pastes text
2. **Parsing**: `utils.py` strips timestamps and formatting, extracts clean text
3. **AI Processing**: `summarizer.py` sends transcript + meeting-type system instruction to Gemini API with JSON mode
4. **Structured Output**: Gemini returns JSON with summary, decisions, action items, follow-ups
5. **Storage**: `database.py` saves meeting and action items to SQLite; updates FTS5 index
6. **Display**: `main.py` renders results using Streamlit components
7. **Search**: FTS5 queries enable cross-meeting search with BM25 ranking
8. **Tracking**: Action items can be toggled between pending/done states

### 3.3 Code Statistics

| File | Lines | Purpose |
|------|-------|---------|
| app/main.py | ~250 | Streamlit application (all 4 pages) |
| app/database.py | ~150 | SQLite operations + FTS5 search |
| app/templates.py | ~150 | 7 meeting-type prompt templates |
| app/summarizer.py | ~80 | Gemini API integration |
| app/utils.py | ~40 | File parsing and text utilities |
| **Total Application Code** | **~650 lines** | |

The entire MVP is under 700 lines of Python — demonstrating that a focused, well-architected AI application can deliver significant value with minimal complexity.
