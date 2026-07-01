from config import generate_response

def email_agent(
    query,
    provider="Auto"
):

    prompt = f"""
You are a professional Email Writing Assistant.

Create:

- Subject
- Professional Email
- Proper Greeting
- Proper Closing

Request:

{query}
"""

    return generate_response(
        prompt,
        provider
    )