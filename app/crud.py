# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas, security


def get_user_by_email(db: Session, email: str):
    """通过邮箱查询用户"""
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    """创建新用户"""
    # 获取密码的哈希值
    hashed_password = security.get_password_hash(user.password)

    # 创建数据库模型实例
    db_user = models.User(email=user.email, hashed_password=hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
