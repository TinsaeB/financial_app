import streamlit as st
import requests

# FastAPI base URL (adjust if needed)
FASTAPI_BASE_URL = "http://localhost:8000"

def show_purchasing():
    st.header("Purchasing")
    # Fetch suppliers
    response = requests.get(f"{FASTAPI_BASE_URL}/suppliers/")
    if response.status_code == 200:
        suppliers = response.json()
        st.subheader("Suppliers")
        st.table(suppliers)
    else:
        st.error("Failed to fetch suppliers")

    # Fetch purchase orders
    response = requests.get(f"{FASTAPI_BASE_URL}/purchase-orders/")
    if response.status_code == 200:
        purchase_orders = response.json()
        st.subheader("Purchase Orders")
        st.table(purchase_orders)
    else:
        st.error("Failed to fetch purchase orders")

    # Fetch purchase items
    response = requests.get(f"{FASTAPI_BASE_URL}/purchase-items/")
    if response.status_code == 200:
        purchase_items = response.json()
        st.subheader("Purchase Items")
        st.table(purchase_items)
    else:
        st.error("Failed to fetch purchase items")
