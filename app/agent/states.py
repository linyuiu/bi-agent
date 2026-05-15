from typing import TypedDict, Any

class AgentState(TypedDict):
    question: str
    sql: str
    result: str