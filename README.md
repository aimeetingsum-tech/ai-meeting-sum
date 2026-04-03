# MeetingMind AI

**The privacy-first, cross-platform meeting summarizer that actually understands your meeting type.**

MeetingMind AI transforms meeting transcripts into structured, actionable summaries with smart action item extraction, cross-meeting search, and meeting-type-aware templates.

## Features

- **7 Meeting Type Templates**: Standup, Sales Call, Brainstorm, 1-on-1, Sprint Planning, Retrospective, General — each produces tailored summaries
- **Smart Action Items**: AI extracts action items with owners and deadlines automatically
- **Cross-Meeting Search**: Full-text search across all your meeting history
- **Privacy-First**: Upload transcripts manually — no bots joining your meetings
- **Action Item Tracker**: Track pending/done status across all meetings
- **Multi-Format Support**: Upload .txt, .srt, or .vtt transcript files

## Quick Start

### Prerequisites
- Python 3.10+
- A Google Gemini API key ([get one here](https://aistudio.google.com/apikey))

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd todolist_reminder

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### Run

```bash
streamlit run app/main.py
```

The app opens at `http://localhost:8501`.

## Project Structure

```
todolist_reminder/
├── app/
│   ├── main.py          # Streamlit app (4 pages)
│   ├── summarizer.py    # Claude API integration
│   ├── templates.py     # 7 meeting-type prompt templates
│   ├── database.py      # SQLite + FTS5 search
│   └── utils.py         # File parsing helpers
├── docs/                # Capstone documents
├── data/                # Sample transcripts
├── tests/               # Database tests
├── requirements.txt
└── .env.example
```

## How It Works

1. **Upload** a meeting transcript (.txt, .srt, .vtt) or paste it directly
2. **Select** the meeting type (standup, sales call, brainstorm, etc.)
3. **Click Summarize** — Claude AI analyzes the transcript with a type-specific prompt
4. **Review** the structured summary: key decisions, action items (with owners + deadlines), and follow-ups
5. **Search** across all past meetings anytime
6. **Track** action items with a built-in pending/done tracker

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| AI Engine | Gemini API (Google) |
| Database | SQLite + FTS5 |
| Language | Python 3.12 |

## Sample Transcripts

The `data/` folder contains sample transcripts for testing:
- `sample_standup.txt` — Daily standup with 4 team members
- `sample_sales_call.txt` — Sales discovery call with a prospect
- `sample_brainstorm.txt` — Brainstorming session for user onboarding
- `sample_sprint_planning.txt` — Sprint planning with story estimation

## License

This project was built as a capstone project for an AI Solutions certificate program.
