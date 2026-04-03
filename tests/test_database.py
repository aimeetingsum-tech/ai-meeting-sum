import sys
import os
import tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import app.database as db

# Use temp DB for tests
db.DB_PATH = os.path.join(tempfile.gettempdir(), "test_meetings.db")


def test_full_flow():
    # Clean start
    if os.path.exists(db.DB_PATH):
        os.remove(db.DB_PATH)

    db.init_db()

    # Save a meeting
    mid = db.save_meeting(
        title="Test Standup",
        meeting_type="standup",
        transcript="Alice: I worked on the API. Bob: I fixed bugs.",
        summary="Alice worked on API, Bob fixed bugs.",
        key_decisions=["Deploy on Friday"],
        follow_ups=["Check deployment status"],
        action_items=[
            {"description": "Deploy API to staging", "owner": "Alice", "deadline": "2024-01-15"},
            {"description": "Write regression tests", "owner": "Bob", "deadline": "TBD"}
        ],
        platform="zoom"
    )
    assert mid == 1, f"Expected meeting ID 1, got {mid}"

    # Retrieve meeting
    meeting = db.get_meeting(mid)
    assert meeting["title"] == "Test Standup"
    assert len(meeting["action_items"]) == 2
    assert meeting["key_decisions"] == ["Deploy on Friday"]

    # List meetings
    meetings = db.list_meetings()
    assert len(meetings) == 1
    assert meetings[0]["action_count"] == 2

    # Search
    results = db.search_meetings("API")
    assert len(results) >= 1

    # Action items
    items = db.get_all_action_items()
    assert len(items) == 2

    # Update status
    db.update_action_item_status(items[0]["id"], "done")
    items = db.get_all_action_items(status_filter="done")
    assert len(items) == 1

    # Stats
    stats = db.get_stats()
    assert stats["total_meetings"] == 1
    assert stats["total_actions"] == 2
    assert stats["pending_actions"] == 1

    print("All database tests passed!")

    # Cleanup
    os.remove(db.DB_PATH)


if __name__ == "__main__":
    test_full_flow()
