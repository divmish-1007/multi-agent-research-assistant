from langgraph.graph import (
    StateGraph,
    START, 
    END
)

from state import ResearchState

from agents.planner import planner_node
from agents.researcher_a import researcher_a_node
from agents.researcher_b import researcher_b_node
from agents.synthesizer import synthesizer_node

builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)

builder.add_node("researcher_a", researcher_a_node)
builder.add_node("researcher_b", researcher_b_node)
builder.add_node("syntheiszer", synthesizer_node)

builder.add_edge(START, "planner")
builder.add_edge("planner", "researcher_a")
builder.add_edge("planner", "researcher_b")

builder.add_edge("researcher_a", "syntheiszer")
builder.add_edge("researcher_b", "syntheiszer")

builder.add_edge("syntheiszer", END)

graph = builder.compile()