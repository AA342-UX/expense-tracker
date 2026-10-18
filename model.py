import datetime
from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    amount: float = Field(gt=0)  #gt means greater than 0
    category: str = "General"
    date: datetime.date = Field(default_factory=datetime.date.today)  #default value is today's date
   
   
class Expense(ExpenseCreate):
    id: int    
