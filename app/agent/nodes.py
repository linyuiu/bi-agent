from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="",
    api_key=""
)

def generate_sql(state):
    question = state["question"]
    prompt = f"""
    你是 BI 分析师。
    用户问题：
    {question}
    请生成 SQL
    """
    response = llm.invoke(prompt)
    return  {"sql": response.content}

