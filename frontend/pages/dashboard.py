import streamlit as st
import plotly.graph_objects as go

st.title("Financial Dashboard")

import streamlit as st
import plotly.graph_objects as go
import requests

st.title("Financial Dashboard")

import streamlit as st
import plotly.graph_objects as go
import requests

st.title("Financial Dashboard")

st.header("Key Financial Metrics")
# Placeholder for interactive charts and graphs
fig = go.Figure(data=[go.Bar(x=['Revenue', 'Expenses', 'Profit'], y=[10000, 7000, 3000])])
st.plotly_chart(fig)

st.header("Financial Performance Summaries")
st.markdown("Total Revenue, Expenses, and Profit/Loss will be displayed here.")

# Fetch data from backend API
try:
    response = requests.get("http://localhost:8000/ledger/income-statement")
    response.raise_for_status()
    income_data = response.json()

    response = requests.get("http://localhost:8000/ledger/balance-sheet")
    response.raise_for_status()
    balance_data = response.json()

    response = requests.get("http://localhost:8000/ledger/cash-flow-statement")
    response.raise_for_status()
    cashflow_data = response.json()

    st.markdown(f"**Total Revenue:** {income_data['revenue']:.2f}")
    st.markdown(f"**Total Expenses:** {income_data['expenses']:.2f}")
    st.markdown(f"**Gross Profit:** {income_data['gross_profit']:.2f}")
    st.markdown(f"**Net Income:** {income_data['net_income']:.2f}")
    
    st.markdown(f"**Total Assets:** {balance_data['assets']:.2f}")
    st.markdown(f"**Total Liabilities:** {balance_data['liabilities']:.2f}")
    st.markdown(f"**Total Equity:** {balance_data['equity']:.2f}")
    
    st.markdown(f"**Cash from Operating Activities:** {cashflow_data['cash_from_operating_activities']:.2f}")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data from API: {e}")

st.markdown("Key metrics from the Income Statement, Balance Sheet, and Cash Flow Statement will be displayed here.")

st.header("Outstanding Invoices")
try:
    response = requests.get("http://localhost:8000/ledger/aged-receivables")
    response.raise_for_status()
    receivables_data = response.json()

    response = requests.get("http://localhost:8000/ledger/aged-payables")
    response.raise_for_status()
    payables_data = response.json()

    st.subheader("Aged Receivables")
    if receivables_data:
        for receivable in receivables_data:
            st.markdown(f"- **{receivable['account']}:** {receivable['amount']:.2f} (Days Outstanding: {receivable['days_outstanding']})")
    else:
        st.markdown("No outstanding receivables.")

    st.subheader("Aged Payables")
    if payables_data:
        for payable in payables_data:
            st.markdown(f"- **{payable['account']}:** {payable['amount']:.2f} (Days Outstanding: {payable['days_outstanding']})")
    else:
        st.markdown("No outstanding payables.")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data from API: {e}")

st.header("Key Performance Indicators (KPIs)")
st.markdown("Key performance indicators will be displayed here. (e.g., Profit Margin, Return on Assets)")

st.header("Budget vs. Actual Performance")
st.markdown("Budget vs. actual performance metrics will be displayed here. (e.g., Budget Variance)")
