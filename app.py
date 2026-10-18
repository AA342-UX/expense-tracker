import pandas as pd
import streamlit as st
import requests


API = "http://127.0.0.1:8000"


st.title("Expense Tracker")


with st.form("add_expense"):
    st.subheader("Add a new expense")
    title = st.text_input("Title")
    amount = st.number_input("Amount", min_value=0.01, step=1.0)
    category = st.selectbox("Category", ["Food", "Transport", "Bills","Entertainment", "Utilities", "General"])
    date = st.date_input("Date")

    submitted = st.form_submit_button("Add Expense")

if submitted:
    response = requests.post(f"{API}/expenses", json={"title": title, "amount": amount, "category": category, "date": date.isoformat()})
    if response.status_code == 201:
        st.success("Expense added successfully!")
    else:
        st.error(f"Invalid Data . Check the title and amount.")
       
       
data = requests.get(f"{API}/expenses").json()


if data:
    df = pd.DataFrame(data)
    st.metric("Total Expenses", f"${df['amount'].sum():.2f}")
    st.subheader("By category")    
    st.bar_chart(df.groupby("category")["amount"].sum())
    st.subheader("All Expenses")
    st.dataframe(df, use_container_width=True)
else:
    st.info("No expenses recorded yet . Add your first expense using the form above.")




