from langgraph.graph import StateGraph, END
from typing import TypedDict

from router import route_query
from agents.chat_agent import run_chat_agent
from agents.indian_agent import run_indian_agent
from agents.global_agent import run_global_agent


# ----- STATE -----
class GraphState(TypedDict):
    query: str
    agent: str
    response: str


# ----- NODES -----

def start_node(state):
    return {
        "query": state["query"]
    }


def classifier_node(state):
    q = state["query"].lower()

    if "india" in q or "nse" in q:
        intent = "indian"
    elif "hi" in q or "hello" in q or "how are you" in q:
        intent = "chat"
    else:
        intent = "global"

    return {
        **state,
        "agent": intent
    }


def router_node(state):
    agent = state["agent"]

    if agent == "indian":
        return "indian_agent"
    elif agent == "chat":
        return "chat_agent"
    else:
        return "global_agent"


def indian_agent_node(state):
    res = run_indian_agent(state["query"])
    return {
        **state,
        "response": res
    }


def chat_agent_node(state):
    res = run_chat_agent(state["query"])
    return {
        **state,
        "response": res
    }


def global_agent_node(state):
    res = run_global_agent(state["query"])
    return {
        **state,
        "response": res
    }


# ----- BUILD GRAPH -----

builder = StateGraph(GraphState)

builder.add_node("START", start_node)
builder.add_node("classifier", classifier_node)
builder.add_node("router", router_node)

builder.add_node("indian_agent", indian_agent_node)
builder.add_node("chat_agent", chat_agent_node)
builder.add_node("global_agent", global_agent_node)

builder.set_entry_point("START")

builder.add_edge("START", "classifier")

builder.add_conditional_edges(
    "classifier",
    lambda state: state["agent"],
    {
        "indian": "indian_agent",
        "chat": "chat_agent",
        "global": "global_agent"
    }
)

builder.add_edge("indian_agent", END)
builder.add_edge("chat_agent", END)
builder.add_edge("global_agent", END)

app = builder.compile()
