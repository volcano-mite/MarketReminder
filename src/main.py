# src/main.py
from fastapi import FastAPI

# 创建一个 FastAPI 应用实例
app = FastAPI()


# 定义一个根路由
@app.get("/")
def read_root():
    return {"Hello": "World", "status": "It's working!"}
