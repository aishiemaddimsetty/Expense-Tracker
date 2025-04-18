from pydantic import BaseModel
from typing import Optional
from datetime import date


# Shared Category fields
class CategoryBase(BaseModel):
    name: str


# When creating a category
class CategoryCreate(CategoryBase):
    pass


# What we return in responses
class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# Shared Expense fields
class ExpenseBase(BaseModel):
    amount: float
    date: date
    description: Optional[str] = None
    category_id: int


class ExpenseCreate(ExpenseBase):
    pass


class Expense(ExpenseBase):
    id: int
    category: Category

    class Config:
        orm_mode = True


# Shared Budget fields
class BudgetBase(BaseModel):
    category_id: int
    month: str  # Format: "YYYY-MM"
    limit: float


class BudgetCreate(BudgetBase):
    pass


class Budget(BudgetBase):
    id: int
