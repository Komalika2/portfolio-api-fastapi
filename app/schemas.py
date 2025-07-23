# from pydantic import BaseModel
# from typing import Optional

# class PortfolioBase(BaseModel):
#     name: str
#     description: Optional[str] = None
#     value: float

# class PortfolioCreate(PortfolioBase):
#     pass

# class Portfolio(PortfolioBase):
#     id: str

#     class Config:
#         orm_mode = True
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class PortfolioBase(BaseModel):
    name: str
    description: Optional[str] = None
    value: float
    title: Optional[str] = None
    skills: Optional[str] = None
    projects: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None

class PortfolioCreate(PortfolioBase):
    pass

class Portfolio(PortfolioBase):
    id: UUID  # ✅ UUID instead of int

    class Config:
        orm_mode = True
