# 定义了 API 请求和响应的数据格式，并进行数据验证
# app/schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime


# 用于接收用户创建请求的 Schema
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# 用于API响应的 Schema，确保密码哈希不会被泄露
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True  # 允许 pydantic 从 ORM 对象 (SQLAlchemy模型) 中读取数据
