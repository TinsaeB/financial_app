import streamlit as st
import requests
import plotly.express as px

# FastAPI base URL (adjust if needed)
FASTAPI_BASE_URL = "http://localhost:8000"

def show_dashboard():
    st.header("Financial Overview")

    # Example: Fetch sales data and display a bar chart
    response = requests.get(f"{FASTAPI_BASE_URL}/sales/sales-orders")
    if response.status_code == 200:
        sales_data = response.json()
        # Process sales_data with pandas if needed
        fig = px.bar(sales_data, x="order_date", y="total_amount", title="Sales Revenue Over Time")
        st.plotly_chart(fig)
