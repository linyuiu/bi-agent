from fastapi import FastAPI

from app.agent.graph import app



if __name__ == '__main__':
    result = app.invoke({"question": "查询最近 30 订单数据"})

    print("question:：")
    print(result["rows"])

    print("\n")

    print("result")
    print(result["result"])
# app = FastAPI(title="BI Agent API")
#
#
# @app.get("/")
# def health_check():
#     return {"status": "ok", "message": "BI Agent API is running"}
