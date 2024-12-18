import streamlit as st
import requests
import plotly.express as px

# FastAPI base URL (adjust if needed)
FASTAPI_BASE_URL = "http://localhost:8000"

st.title("SME Financial Management")

# Sidebar navigation
page = st.sidebar.selectbox("Choose a page", ["Dashboard", "Purchasing", "Sales", "Ledger"])

if page == "Dashboard":
    st.header("Financial Overview")

    # Example: Fetch sales data and display a bar chart
    response = requests.get(f"{FASTAPI_BASE_URL}/sales/sales-orders")
    if response.status_code == 200:
        sales_data = response.json()
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
