from config import generate_response
from datetime import datetime

def calendar_agent(
    query,
    provider="Auto"
):

    prompt = f"""
You are a Smart Calendar Assistant.

Current Date:

{datetime.now()}

User Request:

{query}

Provide:

- Schedule
- Task Breakdown
- Priority
- Deadlines
"""
    
    return generate_response(
        prompt,
        provider
    )