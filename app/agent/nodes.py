import os

from langchain_openai.chat_models.base import BaseChatOpenAI
from dotenv import load_dotenv



load_dotenv()

llm = BaseChatOpenAI(
    model=os.getenv("OPENAI_MODEL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    temperature=0,
    extra_body={"thinking": {"type": "enabled"}}
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

def execute_sql(state):
    sql = state["sql"]

    print("执行 SQL:")
    print(sql)

    mock_result = [
        {"date": "2025-05-01", "gmv": 1000},
        {"date": "2025-05-02", "gmv": 2000},
    ]

    return {
        "result": mock_result
    }





