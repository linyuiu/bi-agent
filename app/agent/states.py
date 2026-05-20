from typing import TypedDict

class AgentState(TypedDict):
    question: str
    sql: str
    result: str
    rows: list