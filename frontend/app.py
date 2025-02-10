import streamlit as st
import requests
import plotly.express as px
from typing import Dict, Any, List

# FastAPI base URL (adjust if needed)
FASTAPI_BASE_URL = "http://localhost:8000"

def fetch_data_from_api(url: str) -> Dict[str, Any]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from API: {e}")
        return {}

def display_data_table(data: List[Dict[str, Any]]):
    if data:
        st.table(data)
    else:
        st.markdown("No data to display.")

st.title("SME Financial Management")

# Sidebar navigation
page = st.sidebar.selectbox("Choose a page", ["Dashboard", "Purchasing", "Sales", "Ledger"])

if page == "Dashboard":
    st.header("Financial Overview")

    # Example: Fetch sales data and display a bar chart
    sales_data = fetch_data_from_api(f"{FASTAPI_BASE_URL}/sales/sales-orders")
    if sales_data:
        # Process sales_data with pandas if needed
        fig = px.bar(sales_data, x="order_date", y="total_amount", title="Sales Revenue Over Time")
        st.plotly_chart(fig)

elif page == "Purchasing":
    st.header("Purchasing")
    # ... implement purchasing UI components (forms, tables, etc.)

elif page == "Sales":
    st.header("Sales")
    # ... implement sales UI components

elif page == "Ledger":
    st.header("Ledger")
    # ... implement ledger UI components
