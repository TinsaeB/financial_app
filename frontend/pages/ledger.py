import streamlit as st
import requests
from ..app import fetch_data_from_api, display_data_table

st.title("Ledger Module")

st.header("Record Transactions")
st.markdown("Record transactions functionality will be implemented here.")

st.header("View Financial Statements")
try:
    income_data = fetch_data_from_api("http://localhost:8000/ledger/income-statement")
    if income_data:
        st.subheader("Income Statement")
        st.markdown(f"**Revenue:** {income_data['revenue']:.2f}")
        st.markdown(f"**Expenses:** {income_data['expenses']:.2f}")
        st.markdown(f"**Gross Profit:** {income_data['gross_profit']:.2f}")
        st.markdown(f"**Net Income:** {income_data['net_income']:.2f}")
    
    balance_data = fetch_data_from_api("http://localhost:8000/ledger/balance-sheet")
    if balance_data:
        st.subheader("Balance Sheet")
        st.markdown(f"**Assets:** {balance_data['assets']:.2f}")
        st.markdown(f"**Liabilities:** {balance_data['liabilities']:.2f}")
        st.markdown(f"**Equity:** {balance_data['equity']:.2f}")
    
    cashflow_data = fetch_data_from_api("http://localhost:8000/ledger/cash-flow-statement")
    if cashflow_data:
        st.subheader("Cash Flow Statement")
        st.markdown(f"**Cash from Operating Activities:** {cashflow_data['cash_from_operating_activities']:.2f}")

except Exception as e:
    st.error(f"Error fetching financial statements: {e}")

st.header("View Trial Balance")
try:
    trial_balance_data = fetch_data_from_api("http://localhost:8000/ledger/trial-balance")
    if trial_balance_data:
        st.subheader("Trial Balance")
        display_data_table([{"Account": k, "Balance": v} for k, v in trial_balance_data.items()])
    else:
        st.markdown("No trial balance data found.")
except Exception as e:
    st.error(f"Error fetching trial balance: {e}")

st.header("View General Ledger Detail Report")
try:
    ledger_detail_data = fetch_data_from_api("http://localhost:8000/ledger/general-ledger-detail")
    if ledger_detail_data:
        st.subheader("General Ledger Detail Report")
        display_data_table(ledger_detail_data)
    else:
        st.markdown("No general ledger detail data found.")
except Exception as e:
    st.error(f"Error fetching general ledger detail: {e}")
