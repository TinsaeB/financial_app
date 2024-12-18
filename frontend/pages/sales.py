import streamlit as st
import requests

# FastAPI base URL (adjust if needed)
FASTAPI_BASE_URL = "http://localhost:8000"

def show_sales():
    st.header("Sales")
    # Fetch customers
    response = requests.get(f"{FASTAPI_BASE_URL}/customers/")
    if response.status_code == 200:
        customers = response.json()
        st.subheader("Customers")
        st.table(customers)
    else:
        st.error("Failed to fetch customers")

    # Fetch sales orders
    response = requests.get(f"{FASTAPI_BASE_URL}/sales-orders/")
    if response.status_code == 200:
        sales_orders = response.json()
        st.subheader("Sales Orders")
        st.table(sales_orders)
    else:
        st.error("Failed to fetch sales orders")

    # Fetch sale items
    response = requests.get(f"{FASTAPI_BASE_URL}/sale-items/")
    if response.status_code == 200:
        sale_items = response.json()
        st.subheader("Sale Items")
        st.table(sale_items)
    else:
        st.error("Failed to fetch sale items")
