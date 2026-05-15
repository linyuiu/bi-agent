from fastapi import FastAPI

from app.agent.graph import app

result = app.invoke({"question": "查询最近 30 天 GMV", })


print(result)
# app = FastAPI(title="BI Agent API")
#
#
# @app.get("/")
# def health_check():
#     return {"status": "ok", "message": "BI Agent API is running"}
