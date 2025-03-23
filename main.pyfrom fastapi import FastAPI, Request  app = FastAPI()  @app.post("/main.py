from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/")
async def line_webhook(request: Request):
    body = await request.json()
    print("LINE 傳來的資料：", body)
    return {"status": "ok"}
