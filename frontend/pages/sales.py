import streamlit as st
import requests
from ..app import fetch_data_from_api, display_data_table

st.title("Sales Module")

st.header("Manage Customers")
try:
    customers = fetch_data_from_api(f"http://localhost:8000/sales/customers")
    if customers:
        st.subheader("List of Customers")
        for customer in customers:
            st.markdown(f"- **{customer['name']}**: {customer['contact_person']}")
    else:
        st.markdown("No customers found.")
except Exception as e:
    st.error(f"Error fetching customers: {e}")
st.markdown("Add/edit/delete customers functionality will be implemented here.")

st.header("Manage Sales Orders")
st.markdown("Create, list, view, edit, and delete sales orders functionality will be implemented here.")

st.header("Manage Sale Items")
st.markdown("Manage sale items functionality will be implemented here.")

st.header("Manage Installment Plans")
st.markdown("Manage installment plans functionality will be implemented here.")
