from state import ResearchState
from langchain_groq import ChatGroq
from config.llm import llm

def synthesizer_node(state: ResearchState):
    prompt = f""" 
    You are an expert writer.
    
    Original Question: {state["query"]}
    
    Research Report 1 ({state["plan"][0]}):
    {state["research_a"]}
    
    Research Report 2 ({state["plan"][1]}):
    {state["research_b"]}
    
    Now write one final, comprehensive and well structured answer
    to the original question using both research reports.
    Make it clear, detailed and easy to understand.
    
    """
    
    response = llm.invoke(prompt)
    print(f"\n[Synthesizer] Final answer ready!")
    
    return {"final_answer": response.content}