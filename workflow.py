from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents import (
    general_agent,
    study_agent,
    career_agent,
    research_agent,
    pdf_agent,
    web_agent,
    coding_agent,
    email_agent,
    calendar_agent,
    document_agent
)

class MARAState(TypedDict):

    query: str

    history: str

    provider: str

    mode: str

    vector_db: object

    memory: object

    language: str

    web_search: bool

    route: str

    response: str

    confidence: int

    agent: str

def router_node(state):

    query = state["query"].lower()

    if any(word in query for word in [
        "pdf",
        "chapter",
        "notes"
    ]):

        route = "pdf"

    elif any(word in query for word in [
        "study",
        "quiz",
        "mcq",
        "summary"
    ]):

        route = "study"

    elif any(word in query for word in [
        "resume",
        "job",
        "career",
        "internship"
    ]):

        route = "career"

    elif any(word in query for word in [
        "today",
        "latest",
        "news"
    ]):

        route = "web"

    elif any(word in query for word in [
        "code",
        "python",
        "java",
        "bug",
        "debug"
    ]):

        route = "coding"

    elif any(word in query for word in [
        "email",
        "mail"
    ]):

        route = "email"

    elif any(word in query for word in [
        "calendar",
        "meeting",
        "schedule"
    ]):

        route = "calendar"

    elif any(word in query for word in [
        "report",
        "proposal",
        "document"
    ]):

        route = "document"

    else:

        route = "general"

    state["route"] = route

    return state

def memory_node(state):

    # Future:
    # Retrieve long-term memory
    # Update conversation memory
    # Personalize responses

    return state
def general_node(state):

    response = general_agent(
        query=state["query"],
        history=state["history"],
        mode=state["mode"],
        provider=state["provider"],
        language=state["language"]
    )

    state["response"] = response
    state["agent"] = "General Agent"

    return state

def pdf_node(state):

    response = pdf_agent(
        query=state["query"],
        vector_db=state["vector_db"],
        provider=state["provider"],
        language=state["language"]
    )

    state["response"] = response
    state["agent"] = "PDF Agent"

    return state

def study_node(state):

    response = study_agent(
        query=state["query"],
        provider=state["provider"],
        language=state["language"]
    )

    state["response"] = response
    state["agent"] = "Study Agent"

    return state

def career_node(state):

    response = career_agent(
        query=state["query"],
        provider=state["provider"],
        language=state["language"]
    )

    state["response"] = response
    state["agent"] = "Career Agent"

    return state

def web_node(state):

    response = web_agent(
        state["query"]
    )

    state["response"] = response
    state["agent"] = "Web Agent"

    return state

def coding_node(state):

    response = coding_agent(
        query=state["query"],
        provider=state["provider"]
    )

    state["response"] = response
    state["agent"] = "Coding Agent"

    return state

def email_node(state):

    response = email_agent(
        query=state["query"],
        provider=state["provider"]
    )

    state["response"] = response
    state["agent"] = "Email Agent"

    return state

def calendar_node(state):

    response = calendar_agent(
        query=state["query"],
        provider=state["provider"]
    )

    state["response"] = response
    state["agent"] = "Calendar Agent"

    return state

def document_node(state):

    response = document_agent(
        query=state["query"],
        provider=state["provider"]
    )

    state["response"] = response
    state["agent"] = "Document Agent"

    return state

def research_node(state):

    response = research_agent(
        query=state["query"],
        provider=state["provider"],
        language=state["language"]
    )

    state["response"] = response
    state["agent"] = "Research Agent"

    return state

def confidence_node(state):

    scores = {

        "pdf": 95,

        "study": 92,

        "career": 90,

        "research": 89,

        "web": 85,

        "coding": 94,

        "email": 93,

        "calendar": 92,

        "document": 94,

        "general": 80

    }

    state["confidence"] = scores.get(
        state["route"],
        80
    )

    return state

# ==================================
# BUILD LANGGRAPH
# ==================================

builder = StateGraph(MARAState)

# Add Nodes

builder.add_node("router", router_node)

builder.add_node("memory", memory_node)

builder.add_node("general", general_node)

builder.add_node("pdf", pdf_node)

builder.add_node("study", study_node)

builder.add_node("career", career_node)

builder.add_node("research", research_node)

builder.add_node("web", web_node)

builder.add_node("coding", coding_node)

builder.add_node("email", email_node)

builder.add_node("calendar", calendar_node)

builder.add_node("document", document_node)

builder.add_node("confidence", confidence_node)

# ==================================
# ROUTING FUNCTION
# ==================================

def route_after_router(state):

    return state["route"]

builder.set_entry_point("router")

builder.add_edge(
    "router",
    "memory"
)

builder.add_conditional_edges(

    "memory",

    route_after_router,

    {

        "general": "general",

        "pdf": "pdf",

        "study": "study",

        "career": "career",

        "research": "research",

        "web": "web",

        "coding": "coding",

        "email": "email",

        "calendar": "calendar",

        "document": "document"

    }

)

builder.add_edge("general", "confidence")

builder.add_edge("pdf", "confidence")

builder.add_edge("study", "confidence")

builder.add_edge("career", "confidence")

builder.add_edge("research", "confidence")

builder.add_edge("web", "confidence")

builder.add_edge("coding", "confidence")

builder.add_edge("email", "confidence")

builder.add_edge("calendar", "confidence")

builder.add_edge("document", "confidence")

builder.set_finish_point("confidence")

graph = builder.compile()