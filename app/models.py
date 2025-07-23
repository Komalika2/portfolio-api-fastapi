# app/models.py
# Placeholder for your Pydantic models or database models
# app/models.py
from sqlalchemy import Column, String, Float
from app.database import Base

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    value = Column(Float, nullable=False)
    title = Column(String, nullable=True)
    skills = Column(String, nullable=True)
    projects = Column(String, nullable=True)
    linkedin = Column(String, nullable=True)
    github = Column(String, nullable=True)


