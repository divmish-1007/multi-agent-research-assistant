from typing import TypedDict

class ResearchState(TypedDict, total=False):
    query: str
    plan: list[str]
    research_a: str
    research_b: str
    final_answer: str