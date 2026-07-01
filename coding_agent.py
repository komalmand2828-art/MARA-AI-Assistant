from config import generate_response

def coding_agent(
    query,
    provider="Auto"
):

    prompt = f"""
You are an expert Software Engineer.

Provide:

1. Explanation
2. Python Code
3. Step-by-step logic
4. Best Practices
5. Possible Improvements

User Request:

{query}
"""

    return generate_response(
        prompt,
        provider
    )