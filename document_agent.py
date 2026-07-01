from config import generate_response

def document_agent(
    query,
    provider="Auto"
):

    prompt = f"""
You are a Professional Document Generator.

Create a formal document.

Include:

1. Title
2. Introduction
3. Main Content
4. Conclusion

Topic:

{query}
"""

    return generate_response(
        prompt,
        provider
    )