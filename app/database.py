import sqlite3
import json
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "meetings.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_connection()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS meetings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            meeting_type TEXT NOT NULL DEFAULT 'general',
            raw_transcript TEXT NOT NULL,
            summary TEXT,
            key_decisions TEXT,
            follow_ups TEXT,
            source_platform TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS action_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            meeting_id INTEGER NOT NULL REFERENCES meetings(id) ON DELETE CASCADE,
            description TEXT NOT NULL,
            owner TEXT,
            deadline TEXT,
            status TEXT DEFAULT 'pending'
        );

        CREATE VIRTUAL TABLE IF NOT EXISTS meetings_fts USING fts5(
            title, raw_transcript, summary, key_decisions,
            content=meetings, content_rowid=id
        );
    """)
    conn.commit()
    conn.close()


def save_meeting(title, meeting_type, transcript, summary, key_decisions,
                 follow_ups, action_items, platform):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO meetings (title, meeting_type, raw_transcript, summary,
           key_decisions, follow_ups, source_platform)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (title, meeting_type, transcript, summary,
         json.dumps(key_decisions), json.dumps(follow_ups), platform)
    )
    meeting_id = cursor.lastrowid

    for item in action_items:
        cursor.execute(
            """INSERT INTO action_items (meeting_id, description, owner, deadline)
               VALUES (?, ?, ?, ?)""",
            (meeting_id, item["description"], item.get("owner"), item.get("deadline"))
        )

    # Update FTS index
    cursor.execute(
        """INSERT INTO meetings_fts (rowid, title, raw_transcript, summary, key_decisions)
           VALUES (?, ?, ?, ?, ?)""",
        (meeting_id, title, transcript, summary, json.dumps(key_decisions))
    )

    conn.commit()
    conn.close()
    return meeting_id


def get_meeting(meeting_id):
    conn = get_connection()
    meeting = conn.execute(
        "SELECT * FROM meetings WHERE id = ?", (meeting_id,)
    ).fetchone()
    if not meeting:
        conn.close()
        return None

    action_items = conn.execute(
        "SELECT * FROM action_items WHERE meeting_id = ? ORDER BY id",
        (meeting_id,)
    ).fetchall()
    conn.close()

    result = dict(meeting)
    result["key_decisions"] = json.loads(result["key_decisions"] or "[]")
    result["follow_ups"] = json.loads(result["follow_ups"] or "[]")
    result["action_items"] = [dict(a) for a in action_items]
    return result


def list_meetings(limit=50, offset=0):
    conn = get_connection()
    rows = conn.execute(
        """SELECT id, title, meeting_type, source_platform, created_at,
           (SELECT COUNT(*) FROM action_items WHERE meeting_id = meetings.id) as action_count
           FROM meetings ORDER BY created_at DESC LIMIT ? OFFSET ?""",
        (limit, offset)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def search_meetings(query):
    conn = get_connection()
    rows = conn.execute(
        """SELECT m.id, m.title, m.meeting_type, m.created_at, m.source_platform,
           snippet(meetings_fts, 2, '<b>', '</b>', '...', 32) as snippet
           FROM meetings_fts
           JOIN meetings m ON m.id = meetings_fts.rowid
           WHERE meetings_fts MATCH ?
           ORDER BY rank""",
        (query,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_all_action_items(status_filter=None, owner_filter=None):
    conn = get_connection()
    query = """SELECT a.*, m.title as meeting_title, m.created_at as meeting_date
               FROM action_items a
               JOIN meetings m ON m.id = a.meeting_id
               WHERE 1=1"""
    params = []
    if status_filter:
        query += " AND a.status = ?"
        params.append(status_filter)
    if owner_filter:
        query += " AND a.owner = ?"
        params.append(owner_filter)
    query += " ORDER BY a.meeting_id DESC, a.id"

    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def update_action_item_status(item_id, status):
    conn = get_connection()
    conn.execute(
        "UPDATE action_items SET status = ? WHERE id = ?",
        (status, item_id)
    )
    conn.commit()
    conn.close()


def get_stats():
    conn = get_connection()
    total_meetings = conn.execute("SELECT COUNT(*) FROM meetings").fetchone()[0]
    total_actions = conn.execute("SELECT COUNT(*) FROM action_items").fetchone()[0]
    pending_actions = conn.execute(
        "SELECT COUNT(*) FROM action_items WHERE status = 'pending'"
    ).fetchone()[0]
    top_type = conn.execute(
        """SELECT meeting_type, COUNT(*) as cnt FROM meetings
           GROUP BY meeting_type ORDER BY cnt DESC LIMIT 1"""
    ).fetchone()
    conn.close()
    return {
        "total_meetings": total_meetings,
        "total_actions": total_actions,
        "pending_actions": pending_actions,
        "top_meeting_type": top_type[0] if top_type else "N/A"
    }
