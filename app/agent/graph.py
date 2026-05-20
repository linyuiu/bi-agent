from langgraph.graph import StateGraph, END

from app.agent.states import AgentState
from app.agent.nodes import generate_sql,execute_sql,analyze_result


graph= StateGraph(AgentState)

graph.add_node("generate_sql",generate_sql)
graph.add_node("execute_sql",execute_sql)
graph.add_node("analyze_result",analyze_result)

graph.set_entry_point("generate_sql")

graph.add_edge("generate_sql","execute_sql")
graph.add_edge("execute_sql","analyze_result")
graph.add_edge("analyze_result",END)

app = graph.compile()


