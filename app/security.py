# app/security.py
from passlib.context import CryptContext

# 创建一个密码哈希上下文，指定使用 bcrypt 算法
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证明文密码和哈希密码是否匹配"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """生成密码的哈希值"""
    return pwd_context.hash(password)
