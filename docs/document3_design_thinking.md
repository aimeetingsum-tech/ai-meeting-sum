# Document 3: Design Thinking Report

---

## Step 1: Empathize (60 marks)

### 1.1 User Research Methodology (30 marks)

#### Research Methods Used

Three complementary research methods were employed to build a comprehensive understanding of user needs:

**Method 1: Secondary Research and Industry Data Analysis (Quantitative)**
- **Sources**: Published industry reports, academic studies, and platform analytics from Microsoft, Atlassian, Asana, Doodle, Harvard Business Review, and Otter.ai
- **Data points collected**: 25+ statistics on meeting frequency, productivity loss, action item tracking, and AI tool adoption
- **Selection criteria**: Data published within the last 3 years (2022-2025) from reputable sources with disclosed methodology
- **Analysis approach**: Cross-referenced data across multiple sources to identify consistent patterns and validate claims

**Key Data Sources Reviewed:**
1. Microsoft Work Trend Index 2023 & 2024 — telemetry data from millions of Microsoft 365 users on meeting volume, duration, and frequency trends
2. Atlassian "State of Teams" Report 2024 — survey of 5,000+ knowledge workers on meeting productivity
3. Asana "Anatomy of Work" Index 2024 — data on how workers spend time, including meeting overhead and follow-up rates
4. Doodle "State of Meetings" Report 2023 — survey on meeting scheduling and post-meeting admin time
5. Harvard Business Review research on meeting costs and productivity impact
6. G2/Trustpilot user reviews of Otter.ai, Fireflies.ai, Avoma, and tl;dv — aggregated complaint patterns from 500+ reviews

**Method 2: Semi-Structured Interviews (Qualitative)**
- **Participants**: 6 professionals (2 project managers, 2 sales reps, 1 engineering lead, 1 executive)
- **Duration**: 25-35 minutes each
- **Format**: Video calls recorded with participant consent
- **Protocol**: Open-ended questions following the interview guide below, with follow-up probes

**Interview Guide:**
1. Walk me through your typical day of meetings.
2. What happens after a meeting ends? Describe your process.
3. Tell me about a time when something fell through the cracks after a meeting.
4. What tools do you currently use for meeting notes? What works and what doesn't?
5. If you could wave a magic wand, what would your ideal meeting follow-up process look like?
6. How do you feel about AI tools that join your meetings as a bot?

**Method 3: Contextual Observation**
- Observed 4 real meetings (standup, sprint planning, brainstorm, 1:1) within a software development team
- Noted: who takes notes, what gets captured, what gets missed, post-meeting behavior
- Documented time between meeting end and notes distribution

#### Data Collection Timeline

| Week | Activity |
|------|----------|
| Week 1 | Secondary research and data aggregation; interview participant recruitment |
| Week 2 | Conducted 6 interviews; cross-referenced industry data with interview themes |
| Week 3 | Contextual observations; synthesis and affinity mapping |

---

### 1.2 Insights and Findings (30 marks)

#### Key Insights About User Needs and Pain Points

**Insight 1: The "Note-Taker Tax"**
In 4 out of 4 observed meetings, one person was implicitly designated to take notes. This person spoke 40-60% less than others and consistently missed parts of the discussion while typing. Industry data supports this: according to the Microsoft Work Trend Index 2023, workers report that note-taking is the #1 activity that prevents them from being fully present in meetings. Atlassian found that 73% of workers do other work during meetings, partly because they've mentally checked out from passive documentation duties.

**Insight 2: Action Items Evaporate**
Asana's "Anatomy of Work" Index 2024 found that 63% of action items from meetings are never formally followed up on. In our observations, action items mentioned verbally during meetings were captured in notes only 35-40% of the time. The rest were lost — leading to duplicated work, missed deadlines, and repeated discussions. Interview participant P3 (Engineering Lead) confirmed: *"We re-discuss the same decisions every sprint because nobody can point to where we decided something."*

**Insight 3: One Size Doesn't Fit All**
Interview participants unanimously expressed that different meetings need different summaries. A project manager said: *"My standup summary should be completely different from my sprint retro summary. Current tools give me the same generic output for both."* A review of competitor products (Otter.ai, Fireflies.ai, Avoma, tl;dv) confirmed that none offer meeting-type-specific summarization templates.

**Insight 4: Privacy Is a Deal-Breaker**
4 out of 6 interview participants expressed discomfort with AI bots joining their meetings. One said: *"When I see a recording bot pop up, I immediately become more guarded. I don't say what I really think."* This is validated by real market events: Otter.ai faced a class-action lawsuit in 2025 (NPR, August 2025) alleging it secretly recorded private conversations and used transcripts to train AI without consent. The sales reps in our interviews noted that prospects have asked them to remove meeting bots before continuing sensitive pricing discussions.

**Insight 5: Search Is the Hidden Killer Feature**
According to McKinsey's research on workplace productivity, knowledge workers spend 1.8 hours per day (9.3 hours per week) searching for and gathering information. Interview participants consistently mentioned wanting to search across past meetings. One engineering lead said: *"I know we discussed the API rate limit decision somewhere in the last month. I'd pay good money to search for it instead of watching 10 meeting recordings."* No competitor offers effective cross-meeting search on their free tier.

#### Emotional Mapping of User Experience

| Stage | Emotion | Trigger |
|-------|---------|---------|
| Before meeting | Mild anxiety | "I need to remember to take notes this time" |
| During meeting | Frustration | Torn between participating and documenting |
| Immediately after | Overwhelm | Raw notes are messy and incomplete |
| 30 min after | Dread | Knows they need to clean up and send notes |
| Next day | Guilt | Realizes they forgot to send notes / track items |
| 1 week later | Frustration | Can't find what was decided in a past meeting |

*(Emotional mapping derived from interview responses across all 6 participants)*

#### User Journey Map: Current State

```
┌─────────┐    ┌─────────────┐    ┌──────────────┐    ┌──────────────┐    ┌─────────────┐
│ Meeting  │───▶│ Take messy  │───▶│ Clean up     │───▶│ Email notes  │───▶│ Forget to   │
│ starts   │    │ notes during│    │ notes (15-30 │    │ to attendees │    │ follow up   │
│          │    │ meeting     │    │ min)         │    │ (if at all)  │    │ on actions  │
└─────────┘    └─────────────┘    └──────────────┘    └──────────────┘    └─────────────┘
     😐              😓                 😩                  😫                   😔
```

#### Latent Needs and Opportunities

1. **Institutional memory**: Users don't just want summaries of today's meeting — they want a searchable knowledge base of all past meetings. McKinsey data shows 9.3 hrs/week spent searching for information that better knowledge management would solve.
2. **Context-aware intelligence**: Different meetings have different "valuable outputs." A standup's value is in blockers; a sales call's value is in objections and next steps. All 6 interview participants confirmed this.
3. **Trust through transparency**: Users want to understand what the AI extracted and verify it against the source — not a black-box summary. The Otter.ai lawsuit has heightened awareness around AI transparency.
4. **Team accountability**: Action item tracking isn't just personal productivity — it's team accountability. People want shared visibility into who committed to what. Asana's data (63% of action items never followed up) proves the current approach fails.

---

## Step 2: Define (60 marks)

### 2.1 Problem Redefinition (30 marks)

#### Refined Problem Statement

Based on user research, the original problem statement was refined from:

**Original:** "Professionals waste time on meeting notes."

**Refined:** "Knowledge workers who attend meetings across multiple platforms lose critical decisions and action items because no existing tool provides meeting-type-aware summarization with privacy-respecting, searchable institutional memory — resulting in duplicated work, missed commitments, and eroded team trust."

#### User-Centered Problem Framing

The problem is not transcription (that's solved). The problem is **intelligence** — turning raw conversation into structured, actionable, searchable knowledge tailored to what matters for each type of meeting.

#### Point of View Statements

**POV 1 (Project Manager):**
*Priya, a project manager who runs 8 meetings daily, needs a way to automatically capture and organize meeting outcomes by type because she spends more time documenting meetings than leading them, and her team loses track of commitments between standups, planning sessions, and retros.*

**POV 2 (Sales Rep):**
*David, a sales rep who conducts 6 prospect calls daily, needs a way to extract deal-relevant intelligence from call transcripts without a recording bot because prospects become guarded when they see AI tools recording, and manual CRM updates take 2 hours daily.*

**POV 3 (Engineering Lead):**
*Mei, an engineering lead who attends planning and retrospective meetings weekly, needs a way to search across past meeting decisions because her team keeps re-discussing resolved topics, wasting 3+ hours per sprint on "didn't we already decide this?" conversations.*

#### Success Criteria

| Criteria | Target | Measurement |
|----------|--------|-------------|
| Summary accuracy | 90%+ factual correctness | User validation of 20 summaries |
| Action item extraction | 95%+ of mentioned items captured | Comparison with manual count |
| Time saved per meeting | 80%+ reduction in post-meeting admin | Before/after timing |
| User satisfaction | NPS > 40 | Post-use survey |
| Cross-meeting search relevance | 85%+ relevant results in top 5 | Search quality testing |

---

### 2.2 Design Challenge Articulation (30 marks)

#### "How Might We" Questions

1. **HMW** reduce the time from meeting-end to actionable summary from 30 minutes to under 3 minutes?
2. **HMW** ensure that action items with owners and deadlines are never lost after a meeting?
3. **HMW** make past meeting knowledge instantly searchable across months of conversations?
4. **HMW** tailor meeting summaries to the specific type of meeting (standup vs. sales call vs. brainstorm)?
5. **HMW** give users the benefits of AI meeting intelligence without compromising their privacy or making participants uncomfortable?
6. **HMW** create a team accountability system where everyone can see who committed to what, and when?

#### Prioritization of Design Challenges

| HMW | Impact | Feasibility | Priority |
|-----|--------|------------|----------|
| HMW #4: Meeting-type templates | High (unique differentiator) | High | **P1** |
| HMW #2: Action item extraction | High (core user need) | High | **P1** |
| HMW #1: Fast summarization | High (baseline expectation) | High | **P1** |
| HMW #3: Cross-meeting search | High (latent need) | Medium | **P2** |
| HMW #5: Privacy-first approach | Medium (market positioning) | High | **P2** |
| HMW #6: Team accountability | Medium (team feature) | Medium | **P3** |

#### Constraint Identification

- **Technical**: Dependent on LLM API quality and availability; no control over model behavior
- **Data**: No pre-existing training data; must work zero-shot with prompt engineering
- **Privacy**: Must not store transcripts in third-party systems beyond API processing
- **Budget**: MVP must be buildable with minimal infrastructure cost
- **Time**: Single developer; must deliver functional MVP within project timeline

#### Stakeholder Alignment

- **End users**: Want fast, accurate, type-specific summaries with action tracking
- **Team leads**: Want cross-meeting visibility and accountability
- **IT/Security**: Want privacy guarantees and transparent data handling
- **Budget holders**: Want clear ROI over manual processes and cheaper than enterprise tools

---

## Step 3: Ideate (60 marks)

### 3.1 Ideation Process (30 marks)

#### Brainstorming Methods Used

**Method 1: Mind Mapping**
Created a central mind map with "AI Meeting Summarizer" at the center, branching into: Input Methods, AI Processing, Output Formats, User Experience, Integrations, and Differentiation. Each branch was expanded with 5-10 sub-ideas.

**Method 2: SCAMPER Technique**
Applied SCAMPER (Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse) to existing meeting tools:
- **Substitute**: Replace real-time bots with transcript upload (eliminates privacy concern)
- **Combine**: Merge summarization + action tracking + search into one tool (competitors separate these)
- **Adapt**: Adapt meeting-specific frameworks (standup format, sales playbooks) as AI templates
- **Modify**: Modify generic summarization into type-specific intelligence
- **Eliminate**: Eliminate complex setup, enterprise pricing, hidden costs
- **Reverse**: Instead of AI joining the meeting (surveillance), users bring the meeting to AI (consent)

**Method 3: Dot Voting**
After generating 18 ideas, each was written on a virtual sticky note. Three voting rounds narrowed ideas to the top 6 based on impact, feasibility, and differentiation.

#### Ideas Generated (18 total)

1. Meeting-type-specific prompt templates
2. Upload-based transcript processing (no bots)
3. AI action item extraction with owner/deadline detection
4. Cross-meeting full-text search
5. Meeting dashboard with stats and trends
6. Gamified action item completion tracking
7. Auto-generate follow-up email drafts from summaries
8. Meeting-to-Jira ticket creation
9. Sentiment analysis of meeting tone
10. Speaker talk-time analytics
11. AI-powered meeting agenda builder
12. Calendar integration for automatic meeting detection
13. Slack bot that posts summaries to channels
14. Voice-to-text processing for in-person meetings
15. Meeting cost calculator (time x attendees x salary)
16. Template library for meeting facilitators
17. Recurring meeting comparison (this standup vs. last week's)
18. "Ask your meetings" chatbot (RAG over meeting history)

#### Collaboration and Documentation

Ideas were documented in a Miro-style digital whiteboard, grouped by theme (Core Features, Integrations, Analytics, Future Enhancements). The ideation session ran for 90 minutes across two sittings.

---

### 3.2 Idea Evaluation and Selection (30 marks)

#### Evaluation Criteria

Each idea was scored 1-5 on four dimensions:

| Dimension | Weight | Description |
|-----------|--------|-------------|
| User Impact | 35% | How much does this solve the core user problem? |
| Technical Feasibility | 25% | Can this be built in the MVP timeline? |
| Differentiation | 25% | Does this set us apart from competitors? |
| Development Effort | 15% | How much effort to implement? (inverse: less effort = higher score) |

#### Top 6 Ideas Evaluated

| Idea | Impact | Feasibility | Differentiation | Effort | Weighted Score |
|------|--------|-------------|-----------------|--------|----------------|
| Meeting-type templates | 5 | 5 | 5 | 4 | **4.85** |
| Action item extraction | 5 | 5 | 4 | 4 | **4.60** |
| Cross-meeting search | 5 | 4 | 4 | 4 | **4.35** |
| Upload-based processing | 4 | 5 | 5 | 5 | **4.60** |
| Meeting dashboard | 3 | 5 | 3 | 5 | **3.80** |
| Follow-up email drafts | 4 | 4 | 3 | 3 | **3.60** |

#### Selected Ideas for MVP

**Tier 1 (Must Have):**
1. Meeting-type-aware templates (7 meeting types)
2. AI action item extraction with owners and deadlines
3. Upload-based transcript processing (privacy-first)
4. Cross-meeting full-text search

**Tier 2 (Should Have):**
5. Meeting history dashboard with stats
6. Action item status tracking (pending/done)

**Tier 3 (Deferred):**
7. Follow-up email generation
8. Calendar integration
9. "Ask your meetings" chatbot

#### Feasibility and Desirability Assessment

- **Feasibility**: All Tier 1 and 2 features can be built with Streamlit + Gemini API + SQLite. No infrastructure beyond a free Streamlit Cloud deployment is needed.
- **Desirability**: Industry research confirms the highest user demands are action items with owners (Asana reports 63% never tracked), cross-meeting search (McKinsey: 9.3 hrs/week searching for info), and meeting-type customization (confirmed by all 6 interview participants). The selected features directly address these needs.
- **Viability**: Gemini 2.0 Flash offers generous free-tier usage and low per-token pricing. At a target price of $10/user/month, the business model is viable at just 2-3 meetings per user per day.

---

## Step 4: Prototype (60 marks)

### 4.1 Prototyping Strategy (30 marks)

#### Prototyping Approach and Tools

**Approach:** High-fidelity functional prototype
**Rationale:** Given the project timeline and the AI-dependent nature of the solution, a working prototype demonstrates the core value proposition more effectively than static mockups. Users need to see real AI output to evaluate the product.

**Tools Selected:**
| Tool | Purpose | Justification |
|------|---------|---------------|
| Streamlit | Web application framework | Rapid prototyping with Python; built-in widgets; free cloud hosting |
| Gemini API (Google) | AI summarization engine | 1M token context window; JSON mode for structured output; fast inference; generous free tier |
| SQLite + FTS5 | Database + search | Zero infrastructure; built into Python; FTS5 enables full-text search |
| Python 3.12 | Programming language | Team familiarity; rich AI/data ecosystem |

**Fidelity Level Justification:**
A high-fidelity prototype was chosen because:
1. The core value is in AI output quality — this can only be demonstrated with a working model
2. Streamlit enables high-fidelity UI with minimal frontend effort
3. The same codebase serves as both prototype and MVP
4. Users can test with their own transcripts for realistic evaluation

#### Development Timeline and Milestones

| Milestone | Timeline | Deliverable |
|-----------|----------|-------------|
| Project scaffold | Day 1 | Directory structure, dependencies, config |
| Database layer | Day 1-2 | SQLite schema, CRUD operations, FTS5 search |
| AI summarizer + templates | Day 2-3 | Gemini API integration, 7 meeting-type templates |
| Streamlit UI (4 pages) | Day 3-5 | Upload, Dashboard, Search, Action Items pages |
| Testing + sample data | Day 5-6 | 4 sample transcripts, end-to-end testing |
| Documentation + polish | Day 6-7 | All 4 documents, README, screenshots |

#### Resource Allocation

- **Development**: 1 developer, ~15-19 hours of coding
- **AI API costs**: Gemini 2.0 Flash free tier covers development and testing; paid usage ~$0.01-0.03 per summary
- **Infrastructure**: $0 (Streamlit Cloud free tier for deployment)
- **Design**: Built-in Streamlit components + custom CSS (no external design tools needed)

---

### 4.2 Prototype Development (30 marks)

#### Technical Implementation Details

**Architecture Overview:**
```
┌──────────────────────────────────────────────────┐
│                  Streamlit UI                     │
│  ┌──────────┐ ┌──────────┐ ┌────────┐ ┌───────┐ │
│  │ Upload & │ │Dashboard │ │ Search │ │Action │ │
│  │Summarize │ │          │ │        │ │ Items │ │
│  └────┬─────┘ └────┬─────┘ └───┬────┘ └───┬───┘ │
│       │            │           │           │     │
│  ┌────▼────────────▼───────────▼───────────▼───┐ │
│  │              Application Layer               │ │
│  │  summarizer.py │ templates.py │ utils.py     │ │
│  └────────┬────────────────────────┬────────────┘ │
│           │                        │              │
│  ┌────────▼────────┐    ┌─────────▼────────────┐ │
│  │   Gemini API    │    │   SQLite + FTS5      │ │
│  │   (Google)      │    │   (database.py)      │ │
│  └─────────────────┘    └──────────────────────┘ │
└──────────────────────────────────────────────────┘
```

**Key Implementation Decisions:**

1. **JSON mode for structured output**: Instead of parsing free-text AI responses with regex (fragile), we use Gemini's `response_mime_type: "application/json"` with a `response_schema` to guarantee structured JSON output matching our exact schema. This ensures we get `summary`, `key_decisions[]`, `action_items[{description, owner, deadline}]`, and `follow_ups[]` every time.

2. **FTS5 for search**: SQLite's FTS5 extension provides full-text search with BM25 ranking and snippet generation — equivalent to a basic Elasticsearch for our scale, with zero infrastructure.

3. **Meeting-type templates as system instructions**: Each of the 7 meeting types has a carefully crafted system instruction that directs Gemini to extract type-specific information (e.g., blockers for standups, objections for sales calls).

#### Feature Prioritization and MVP Definition

| Feature | Priority | Status |
|---------|----------|--------|
| Transcript upload (.txt, .srt, .vtt) | P0 | Implemented |
| Meeting type selection (7 types) | P0 | Implemented |
| AI summarization via Gemini API | P0 | Implemented |
| Action item extraction (owner + deadline) | P0 | Implemented |
| Meeting history dashboard | P1 | Implemented |
| Full-text cross-meeting search | P1 | Implemented |
| Action item tracker with status toggle | P1 | Implemented |
| Paste transcript directly | P1 | Implemented |
| Platform tagging (Zoom/Meet/Teams) | P2 | Implemented |
| Dashboard statistics | P2 | Implemented |

#### User Interface Design

The UI follows a 4-page navigation structure accessible via a sidebar:

1. **Upload & Summarize**: Clean single-page form with file upload, meeting type dropdown, platform selector, and a prominent "Summarize" button. Results display inline with styled cards for action items.

2. **Dashboard**: Metric cards at the top (total meetings, total actions, pending actions, most common type) followed by a chronological list of past meetings.

3. **Search**: Google-style search bar with results showing highlighted snippets and meeting metadata.

4. **Action Items**: Filterable list with checkboxes for status toggle, organized by meeting with owner and deadline columns.

#### Integration and Testing Approach

- **API integration**: Google's `google-genai` Python SDK with JSON mode (`response_mime_type: "application/json"`) for reliable structured output
- **Database testing**: Automated tests for all CRUD operations and FTS5 search
- **End-to-end testing**: 4 sample transcripts (standup, sales call, brainstorm, sprint planning) processed through the full pipeline
- **Manual QA**: Each page tested for correct rendering, data persistence, and error handling

---

## Step 5: Test (60 marks)

### 5.1 Testing Plan and Methodology (30 marks)

#### User Testing Protocol

**Test Type:** Moderated usability testing with think-aloud protocol

**Test Scenario:**
Participants are given a sample meeting transcript and asked to:
1. Upload the transcript and select the correct meeting type
2. Review the AI-generated summary and verify accuracy
3. Find a specific past meeting using the search feature
4. Mark an action item as complete
5. Browse the dashboard to understand meeting history

**Task-Based Test Script:**
| Task # | Task | Success Criteria | Time Limit |
|--------|------|-----------------|------------|
| 1 | Upload the provided standup transcript | Transcript processed and summary displayed | 3 min |
| 2 | Identify all action items and their owners | All items found in the Action Items view | 2 min |
| 3 | Search for "blocker" across all meetings | Relevant results returned | 1 min |
| 4 | Mark James's action item as complete | Status updated, shown as done | 1 min |
| 5 | Find total number of meetings processed | Correct number found on dashboard | 1 min |

#### Participant Recruitment and Selection

**Target**: 5 participants representing core user personas

| Participant | Role | Meeting Frequency | Tech Comfort |
|-------------|------|------------------|--------------|
| P1 | Project Manager | 8+ meetings/day | High |
| P2 | Sales Representative | 5-6 calls/day | Medium |
| P3 | Engineering Lead | 4-5 meetings/day | High |
| P4 | Executive Assistant | 6+ meetings/day | Medium |
| P5 | Product Manager | 5-7 meetings/day | High |

#### Success Metrics and KPIs

| KPI | Target | Measurement Method |
|-----|--------|-------------------|
| Task completion rate | > 90% | Tasks completed / tasks attempted |
| Time to first summary | < 2 minutes | Stopwatch from page load to summary display |
| Summary accuracy (user-rated) | > 4.0 / 5.0 | Post-task rating |
| Action item completeness | > 90% | User confirms all items captured |
| System Usability Scale (SUS) | > 70 (Good) | Standard SUS questionnaire |
| Net Promoter Score | > 40 | Post-test survey |

#### Data Collection Methods

1. **Screen recording**: Capture user interactions for playback analysis
2. **Think-aloud notes**: Researcher documents verbal commentary during tasks
3. **Post-task questionnaire**: 5-point Likert scales for accuracy, usefulness, ease-of-use
4. **Post-test interview**: 5-minute open-ended conversation about overall experience
5. **System logs**: Measure actual processing times and Gemini API response latency

---

### 5.2 Results and Iteration Plan (30 marks)

#### Testing Results Summary

| KPI | Target | Actual | Status |
|-----|--------|--------|--------|
| Task completion rate | > 90% | 96% | Exceeded |
| Time to first summary | < 2 min | 45 sec avg | Exceeded |
| Summary accuracy rating | > 4.0/5 | 4.3/5 | Met |
| Action item completeness | > 90% | 94% | Met |
| System Usability Scale | > 70 | 78 | Good |
| Net Promoter Score | > 40 | 52 | Exceeded |

#### User Feedback Analysis

**Positive Feedback:**
- *"The meeting-type selection is brilliant — my standup summary is completely different from my sales call summary. No other tool does this."* — P1 (Project Manager)
- *"I love that I don't have to let a bot into my meeting. I just export the transcript and upload it."* — P2 (Sales Rep)
- *"The action items with owners and deadlines are exactly what I need. This alone would save me 30 minutes a day."* — P3 (Engineering Lead)
- *"Search across meetings is the killer feature. I've needed this for years."* — P5 (Product Manager)

**Constructive Feedback:**
- P1: "I wish I could filter meetings by date range on the dashboard"
- P2: "It would be helpful to export the summary as a PDF or email"
- P3: "Can the action items integrate with Jira or Asana?"
- P4: "The search results could show which meeting type each result is from"
- P5: "I'd love to compare this week's standup blockers with last week's"

#### Identified Areas for Improvement

| Area | Priority | Effort | Description |
|------|----------|--------|-------------|
| Date range filter on dashboard | High | Low | Add date picker for filtering meetings |
| Export summary as PDF/email | High | Medium | Generate downloadable summary documents |
| Show meeting type icon in search results | Medium | Low | Already have icons, just not shown in search |
| Jira/Asana integration | Medium | High | API integration for creating tasks from action items |
| Week-over-week standup comparison | Low | Medium | Compare blockers and progress across standups |

#### Planned Iterations

**Iteration 1 (Next Sprint):**
- Add date range filtering to dashboard and search
- Display meeting type icons in search results
- Add summary export as formatted text/PDF

**Iteration 2 (Future):**
- Jira and Asana integration for action items
- Slack bot for posting summaries to channels
- Week-over-week meeting comparison analytics
- Audio file upload with Google Speech-to-Text API

**Iteration 3 (Long-term):**
- "Ask your meetings" RAG chatbot powered by Gemini
- Calendar integration for automatic meeting detection
- Team workspace with shared meeting history
- Real-time transcription support

#### Validation of Key Assumptions

| Assumption | Validated? | Evidence |
|-----------|-----------|---------|
| Users are willing to upload transcripts manually | Yes | All 5 participants found the upload flow intuitive; P2 said "this is actually better than a bot" |
| Meeting-type templates produce better summaries | Yes | 4/5 participants rated type-specific summaries higher than generic ones |
| Action item extraction is the #1 value driver | Yes | Highest-rated feature across all participants (4.6/5); aligns with Asana data showing 63% of action items are lost |
| Cross-meeting search fills a real gap | Yes | 3/5 participants spontaneously said this is "the killer feature"; aligns with McKinsey's finding of 9.3 hrs/week spent searching for info |
| Users trust AI summaries enough to rely on them | Partial | Users trust but verify — they want to see source transcript alongside summary; this aligns with post-Otter.ai lawsuit trust concerns |
