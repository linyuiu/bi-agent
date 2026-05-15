from langgraph.graph import StateGraph, END

from app.agent.states import AgentState
from app.agent.nodes import generate_sql,execute_sql

graph= StateGraph(AgentState)

graph.add_node("generate_sql",generate_sql)
graph.add_node("execute_sql",execute_sql)

graph.set_entry_point("generate_sql")

graph.add_edge("generate_sql","execute_sql")
graph.add_edge("execute_sql",END)
app = graph.compile()


