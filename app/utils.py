import re


def parse_transcript_file(uploaded_file):
    content = uploaded_file.read().decode("utf-8", errors="replace")
    filename = uploaded_file.name.lower()

    if filename.endswith(".srt"):
        return _parse_srt(content)
    elif filename.endswith(".vtt"):
        return _parse_vtt(content)
    else:
        return content.strip()


def _parse_srt(content):
    """Strip SRT sequence numbers and timestamps, keep dialogue."""
    lines = []
    for line in content.split("\n"):
        line = line.strip()
        # Skip sequence numbers (pure digits) and timestamp lines
        if re.match(r"^\d+$", line):
            continue
        if re.match(r"\d{2}:\d{2}:\d{2}", line):
            continue
        if line:
            lines.append(line)
    return "\n".join(lines)


def _parse_vtt(content):
    """Strip WebVTT headers and timestamps, keep dialogue."""
    lines = []
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if re.match(r"\d{2}:\d{2}:\d{2}\.\d{3}", line):
            continue
        if line and not line.startswith("NOTE"):
            lines.append(line)
    return "\n".join(lines)


def truncate_text(text, max_chars=200):
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rsplit(" ", 1)[0] + "..."
