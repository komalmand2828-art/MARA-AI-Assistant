from config import generate_response
from rag import retrieve_context, retrieve_docs
from web_search import search_web
from database import get_memory

from document_agent import document_agent
from email_agent import email_agent
from calendar_agent import calendar_agent
from coding_agent import coding_agent

from tools.calculator_tool import calculator_tool
from tools.web_tool import web_tool
from tools.time_tool import time_tool


# ==================================
# MEMORY MANAGER
# ==================================

def update_memory(query, memory):

    q = query.lower()

    try:

        if "my name is" in q:

            memory["name"] = query.split(
                "my name is"
            )[1].strip()

        elif "i am studying" in q:

            memory["course"] = query.split(
                "i am studying"
            )[1].strip()

        elif "my college is" in q:

            memory["college"] = query.split(
                "my college is"
            )[1].strip()

    except Exception:
        pass

    return memory


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

    past_memory = get_memory()

    memory_text = ""

    for q, a in past_memory:

        memory_text += (
            f"User: {q}\n"
            f"Assistant: {a}\n\n"
        )

    prompt = f"""
You are MARA AI Assistant.

You are a professional AI assistant capable of solving any task.

Answer ONLY in:
{language}

Response Style:
{mode}

Conversation History:
{history}

Long Term Memory:
{memory_text}

Current User Question:
{query}

Instructions:

• Give accurate answers.
• Use headings wherever suitable.
• Use bullet points when needed.
• Explain step-by-step if required.
• Keep formatting clean.
• Be friendly and professional.
• If coding is requested, format code properly.
• If the answer is unknown, honestly say so.

Generate the best possible response.
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
You are MARA's Study Agent.

Answer in:
{language}

Your responsibilities:

• Explain concepts in simple language.
• Give step-by-step explanations.
• Include examples whenever useful.
• Include formulas if required.
• Highlight important exam points.
• Mention common mistakes.
• End with a quick revision summary.

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
You are MARA's Research Agent.

Answer in:
{language}

Provide a professional research-style response.

Include:

• Introduction
• Detailed Explanation
• Technical Concepts
• Advantages
• Limitations
• Real-world Applications
• Future Scope
• Conclusion

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
You are MARA's Career Mentor.

Answer in:
{language}

Help the user with:

• Career guidance
• Resume improvement
• Internship preparation
• Placement preparation
• Interview questions
• LinkedIn optimization
• Project suggestions
• Skill roadmap

Question:

{query}
"""

    return generate_response(
        prompt,
        provider
    )


# ==================================
# NOTES AGENT
# ==================================

def notes_agent(
    text,
    provider="Auto",
    language="English"
):

    prompt = f"""
Create high-quality study notes.

Language:
{language}

Include:

# Summary

# Important Concepts

# Key Definitions

# Important Formulas

# Examples

# Interview Questions

# Viva Questions

# Revision Tips

Content:

{text}
"""

    return generate_response(
        prompt,
        provider
    )


# ==================================
# QUIZ AGENT
# ==================================

def quiz_agent(
    text,
    provider="Auto"
):

    prompt = f"""
Generate an exam-quality quiz.

Requirements:

• 15 Multiple Choice Questions
• Four options
• Correct answer
• Medium to Hard difficulty
• Mix conceptual and numerical questions

Content:

{text}
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

    try:

        context = retrieve_context(
            vector_db,
            query
        )

        docs = retrieve_docs(
            vector_db,
            query
        )

        prompt = f"""
You are MARA AI PDF Agent.

Answer ONLY from the uploaded documents.

Language:
{language}

Rules:

• Never make up information.
• If the answer is unavailable in the document,
  clearly say:
  "The answer is not available in the uploaded document."

• Give a structured answer.
• Use bullet points whenever appropriate.

Document Context:

{context}

User Question:

{query}
"""

        answer = generate_response(
            prompt,
            provider
        )

        source_list = []

        for i, doc in enumerate(docs):

            preview = (
                doc.page_content[:120]
                .replace("\n", " ")
            )

            source_list.append(
                f"📄 Chunk {i+1}: {preview}..."
            )

        confidence = min(
            95,
            70 + len(docs) * 5
        )

        response = answer

        response += "\n\n---"

        response += (
            f"\n🎯 Confidence: {confidence}%"
        )

        response += "\n\n### 📚 Sources Used\n"

        response += "\n".join(source_list)

        return response

    except Exception as e:

        return (
            "⚠️ PDF Agent Error\n\n"
            + str(e)
        )


# ==================================
# WEB AGENT
# ==================================

def web_agent(query):

    try:

        results = search_web(query)

        if not results:

            return (
                "⚠️ No web results found."
            )

        output = "## 🌐 Web Search Results\n\n"

        for i, item in enumerate(results, start=1):

            output += (
                f"### {i}. {item['title']}\n\n"
            )

            output += (
                f"{item['body']}\n\n"
            )

            output += (
                f"🔗 {item['url']}\n\n"
            )

            output += "---\n\n"

        return output

    except Exception as e:

        return (
            "⚠️ Web Agent Error\n\n"
            + str(e)
        )
# ==================================
# MANAGER AGENT (Compatibility Wrapper)
# ==================================

def manager_agent(
    query,
    vector_db=None,
    mode="Professional",
    history="",
    provider="Auto",
    memory=None,
    web_search=False,
    language="English"
):
    """
    Legacy compatibility function.

    LangGraph now handles routing.
    This wrapper simply calls the General Agent.
    """

    return {
        "agent": "General Agent",
        "response": general_agent(
            query=query,
            history=history,
            mode=mode,
            provider=provider,
            language=language
        )
    }