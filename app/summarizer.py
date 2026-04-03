import os
import json
from google import genai
from dotenv import load_dotenv
from app.templates import get_system_prompt

load_dotenv()

_client = None


def _get_client():
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not set. Add it to your .env file.")
        _client = genai.Client(api_key=api_key)
    return _client

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "A concise but comprehensive summary of the meeting (2-4 paragraphs)."
        },
        "key_decisions": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List of key decisions made during the meeting."
        },
        "action_items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string",
                        "description": "What needs to be done."
                    },
                    "owner": {
                        "type": "string",
                        "description": "Who is responsible. Use the person's name from the transcript."
                    },
                    "deadline": {
                        "type": "string",
                        "description": "When it's due (ISO date or 'TBD' if not specified)."
                    }
                },
                "required": ["description", "owner", "deadline"]
            },
            "description": "Action items with clear ownership and deadlines."
        },
        "follow_ups": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Suggested follow-up topics or meetings."
        }
    },
    "required": ["summary", "key_decisions", "action_items", "follow_ups"]
}


def summarize_meeting(transcript, meeting_type="general"):
    system_prompt = get_system_prompt(meeting_type)

    response = _get_client().models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Please analyze this meeting transcript and extract a structured summary:\n\n{transcript}",
        config={
            "system_instruction": system_prompt,
            "response_mime_type": "application/json",
            "response_schema": OUTPUT_SCHEMA,
            "temperature": 0.3,
        },
    )

    result = json.loads(response.text)

    # Ensure all required keys exist
    result.setdefault("summary", "")
    result.setdefault("key_decisions", [])
    result.setdefault("action_items", [])
    result.setdefault("follow_ups", [])

    # Ensure each action item has required fields
    for item in result["action_items"]:
        item.setdefault("description", "")
        item.setdefault("owner", "Unassigned")
        item.setdefault("deadline", "TBD")

    return result
