# agents/researcher_b.py
from state import ResearchState
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq
from config.llm import llm
search = DuckDuckGoSearchRun()

def researcher_b_node(state: ResearchState):
    original_query = state["query"]
    angle = state["plan"][1]

    full_topic = f"{angle} {original_query}"

    # Step 1: Search the web
    print(f"\n[Researcher B] Searching: {full_topic}")
    search_results = search.run(full_topic)

    # Step 2: LLM summarizes the search results
    prompt = f"""
    You are a thorough researcher.
    
    Original Question: {original_query}
    Your specific research angle: {angle}
    
    Web Search Results:
    {search_results}
    
    Write a detailed, well structured research report on this specific angle.
    Keep the original question in mind throughout.
    Include key facts, insights and important points.
    """

    response = llm.invoke(prompt)
    
    print(f"[Researcher B] Done!")
    return {"research_b": response.content}