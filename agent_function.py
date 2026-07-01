from config import generate_response
from rag import retrieve_context, retrieve_docs
from web_search import search_web


# ==================================
# GENERAL AGENT
# ==================================

def general_agent(
    query,
    history="",
    mode="Professional",
    provider="Auto",
    language="English"
):

    prompt = f"""
You are MARA AI Assistant.

Always answer in:
{language}

Response Mode:
{mode}

Previous Conversation:
{history}

Current Question:
{query}

Give a helpful response.
"""

    return generate_response(
        prompt,
        provider
    )


# ==================================
# STUDY AGENT
# ==================================

def study_agent(
    query,
    provider="Auto",
    language="English"
):

    prompt = f"""
You are a Study Assistant.

Answer in:
{language}

Explain concepts in simple language.

Question:
{query}
"""

    return generate_response(
        prompt,
        provider
    )


# ==================================
# CAREER AGENT
# ==================================

def career_agent(
    query,
    provider="Auto",
    language="English"
):

    prompt = f"""
You are a Career Mentor.

Answer in:
{language}

Question:
{query}
"""

    return generate_response(
        prompt,
        provider
    )


# ==================================
# RESEARCH AGENT
# ==================================

def research_agent(
    query,
    provider="Auto",
    language="English"
):

    prompt = f"""
You are a Research Assistant.

Answer in:
{language}

Question:
{query}
"""

    return generate_response(
        prompt,
        provider
    )


# ==================================
# PDF AGENT
# ==================================

def pdf_agent(
    query,
    vector_db,
    provider="Auto",
    language="English"
):

    context = retrieve_context(
        vector_db,
        query
    )

    docs = retrieve_docs(
        vector_db,
        query
    )

    prompt = f"""
Answer in:
{language}

Context:
{context}

Question:
{query}
"""

    answer = generate_response(
        prompt,
        provider
    )

    return answer


# ==================================
# WEB AGENT
# ==================================

def web_agent(query):

    try:

        search_results = search_web(
            query
        )

        result_text = (
            "🌐 Web Search Results\n\n"
        )

        for i, result in enumerate(
            search_results,
            start=1
        ):

            result_text += (
                f"### {i}. "
                f"{result['title']}\n\n"
                f"{result['body']}\n\n"
                f"🔗 {result['url']}\n\n"
            )

        return result_text

    except Exception as e:

        return (
            "⚠️ Web Search Error\n\n"
            + str(e)
        )