import os

from langchain_openai.chat_models.base import BaseChatOpenAI
from dotenv import load_dotenv

from app.agent.states import AgentState
from app.db.dataset_structure import execute_pgsql



load_dotenv()

llm = BaseChatOpenAI(
    model=os.getenv("OPENAI_MODEL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    temperature=0,
    extra_body={"thinking": {"type": "enabled"}}
)

def generate_sql(state:AgentState):
    question = state["question"]

    dataset_structure = execute_pgsql("""SELECT 
    column_name, 
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_name = 'orders';""")

    print("表结构",dataset_structure)

    prompt = f"""
    你是一个 PostgreSQL SQL 生成器。

    要求：
    1. 只返回一条 SQL
    2. 不要解释
    3. 不要 Markdown
    4. 不要代码块
    5. 不要返回多个 SQL
    6. SQL 必须可以直接执行
    
    用户问题：
    {question}
    表结构信息
    {dataset_structure}
    请生成 SQL
    """
    response = llm.invoke(prompt)

    print("大模型 sql", response.content.strip())

    sql = response.content.strip()

    return  {
        "sql": sql,
    }

def execute_sql(state:AgentState):

    sql = state["sql"]

    rows = execute_pgsql(sql)

    return {
        "rows": rows,
    }


def analyze_result(state:AgentState):

    rows = state["rows"]

    prompt = f"""你是数据分析师，分析最近 30 天的订单数据数据给出一个分析的结论
    数据
    {rows}
    """
    response = llm.invoke(prompt)

    return {"result": response.content}




