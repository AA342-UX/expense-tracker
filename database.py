import sqlite3


DB_NAME = "expenses.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  #lets us access columns by name instead of index
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute("""
                     CREATE TABLE IF NOT EXISTS expenses(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         title TEXT NOT NULL,
                         amount REAL NOT NULL,
                         category TEXT NOT NULL,
                         date TEXT NOT NULL
                     )
                     """)
       
def add_expense(title, amount, category, date)->int:
    with get_connection() as conn:
        cursor = conn.execute("""
                              INSERT INTO expenses(title, amount, category, date) VALUES (?, ?, ?, ?)
                              """, (title, amount, category, date))
        return cursor.lastrowid
   
def get_expenses():
    with get_connection() as conn:
            return conn.execute("SELECT * FROM expenses ORDER BY date DESC").fetchall()
       
def delete_expense(expense_id) -> bool:
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        return cursor.rowcount > 0
