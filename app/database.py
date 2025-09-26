# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 你的 docker-compose.yml 中定义的 PostgreSQL 连接 URL
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@db/stock_alerts"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
