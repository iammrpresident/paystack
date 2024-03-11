import json

def parse_response(response):
    """Parse JSON response from API."""
    try:
        return response.json()
    except json.JSONDecodeError:
        return None