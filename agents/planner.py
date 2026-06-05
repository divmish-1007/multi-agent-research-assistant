# agents/planner.py
from state import ResearchState
from langchain_groq import ChatGroq
from config.llm import llm
import ast


def planner_node(state: ResearchState):
    query = state["query"]

    prompt = f"""
    You are a research planner.
    
    User Question: {query}
    
    Break this question into exactly 2 different research angles/sub-topics
    so two researchers can work in parallel.
    
    Each angle must clearly relate to the original question.
    
    Return ONLY a Python list with exactly 2 strings. Example:
    ["angle 1 to research", "angle 2 to research"]
    
    Nothing else. No explanation. No extra text.
    """

    response = llm.invoke(prompt)

    plan = ast.literal_eval(response.content.strip())
    print(f"\n[Planner] Research angles: {plan}")
    
    return {"plan": plan}