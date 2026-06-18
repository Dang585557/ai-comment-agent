"""
AI-COMPANY
dashboard/backend/database.py

Database Manager
"""

import os
from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./ai_company.db"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite")
    else {}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    team = Column(String, nullable=False)

    status = Column(String, default="PENDING")

    priority = Column(String, default="NORMAL")

    progress = Column(Integer, default=0)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Agent(Base):

    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    team = Column(String, nullable=False)

    status = Column(String, default="ONLINE")

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class SystemLog(Base):

    __tablename__ = "system_logs"

    id = Column(Integer, primary_key=True, index=True)

    level = Column(String)

    message = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


def create_database():

    Base.metadata.create_all(bind=engine)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


if __name__ == "__main__":

    create_database()

    print("AI-COMPANY Database Ready")
