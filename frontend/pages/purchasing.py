import streamlit as st
import requests
from ..app import fetch_data_from_api, display_data_table

st.title("Purchasing Module")

st.header("Manage Suppliers")
try:
    suppliers = fetch_data_from_api(f"http://localhost:8000/purchasing/suppliers")
    if suppliers:
        st.subheader("List of Suppliers")
        for supplier in suppliers:
            st.markdown(f"- **{supplier['name']}**: {supplier['contact_person']}")
    else:
        st.markdown("No suppliers found.")
except Exception as e:
    st.error(f"Error fetching suppliers: {e}")
st.markdown("Add/edit/delete suppliers functionality will be implemented here.")

st.header("Manage Purchase Orders")
st.markdown("Create, list, view, edit, and delete purchase orders functionality will be implemented here.")

st.header("Manage Purchase Items")
st.markdown("Manage purchase items functionality will be implemented here.")

st.header("Process Payment")
st.markdown("Process payment functionality will be implemented here.")
