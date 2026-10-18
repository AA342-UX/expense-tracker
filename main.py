from fastapi import FastAPI, HTTPException
import database
from model import Expense, ExpenseCreate

app = FastAPI(title="Expense Tracker API", description="A simple API to track expenses", version="1.0.0")
database.init_db()  #initialize the database when the app starts

@app.post("/expenses", response_model=Expense, status_code=201)
def create_expense(expense: ExpenseCreate):
    expense_id = database.add_expense(expense.title, expense.amount, expense.category, expense.date.isoformat())
    return Expense(id=expense_id, **expense.model_dump()) # {"title": "Lunch", "amount": 10.5, "category": "Food", "date": "2023-09-01"}

@app.get("/expenses", response_model=list[Expense])
def list_expenses():
   return [dict(row) for row in database.get_expenses()]

@app.delete("/expenses/{expense_id}", status_code=204)
def remove_expense(expense_id: int):
    if not database.delete_expense(expense_id):
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense deleted successfully"}
