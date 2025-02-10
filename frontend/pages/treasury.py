import streamlit as st
import requests
from ..app import fetch_data_from_api, display_data_table

st.title("Treasury Module")

st.header("Manage Assets")
st.markdown("Manage assets, their values and depreciations functionality will be implemented here.")

st.header("Track Loans")
st.markdown("Track loans, payments and repayment schedules functionality will be implemented here.")
