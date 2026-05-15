from fastapi import FastAPI

app = FastAPI(title="BI Agent API")


@app.get("/")
def health_check():
    return {"status": "ok", "message": "BI Agent API is running"}
