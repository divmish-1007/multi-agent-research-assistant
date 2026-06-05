from state import ResearchState
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq
from config.llm import llm

search = DuckDuckGoSearchRun()


def researcher_a_node(state: ResearchState):
    
    original_query = state["query"]
    angle = state["plan"][0]
    
    full_topic = f"{angle} {original_query}"   

    # Step 1: Search the Web

    print(f"\n[Researcher A] Searching: {full_topic}")
    search_result = search.run(full_topic)
    
    prompt = f"""
    You are a thorough researcher.
    
    Original Question: {original_query}
    Your specific research angle: {angle}

    Web Search Result: {search_result}

    write a detailed, well structured research report on this specific angle.
    Keep the original question in mind throughout.
    Include key facts, insights and important points.
    
    """
    
    response = llm.invoke(prompt)
    
    print(f"[Researcher A] Done!")

    return{"research_a": response.content}