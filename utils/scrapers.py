import re

def sanitize_web_content(raw_html_or_text: str, max_chars: int = 1000) -> str:
    """
    Cleans raw web content and prepares it for AI token processing.
    """
    # Remove HTML tags if present
    clean_text = re.sub(r'<[^>]+>', '', raw_html_or_text)
    # Remove extra spaces and newlines
    clean_text = ' '.join(clean_text.split())
    # Truncate to limit execution costs
    return clean_text[:max_chars]

def calculate_risk_level(fud_index: int) -> str:
    """
    Categorizes the risk based on FUD score.
    """
    if fud_index >= 75:
        return "CRITICAL_FUD"
    elif fud_index >= 45:
        return "MODERATE_RUMOR"
    else:
        return "SAFE_OR_NEUTRAL"
