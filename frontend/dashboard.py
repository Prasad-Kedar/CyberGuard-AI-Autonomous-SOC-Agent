import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="CyberGuard AI",
    layout="wide"
)

st.title("CyberGuard AI")
st.subheader("SOC Alert Dashboard")

st.markdown("---")

source = st.selectbox(
    "Source",
    ["Firewall", "EDR", "SIEM", "IDS"]
)

severity = st.selectbox(
    "Severity",
    ["Low", "Medium", "High", "Critical"]
)

event = st.text_input("Event")

ip = st.text_input("IP Address")

if st.button("Submit Alert"):

    payload = {
        "source": source,
        "severity": severity,
        "event": event,
        "ip": ip
    }

    response = requests.post(
        "http://127.0.0.1:8000/alert",
        json=payload
    )

    if response.status_code == 200:
        st.success("Alert Submitted")


        st.markdown("---")

st.header("Recent Alerts")

response = requests.get(
    "http://127.0.0.1:8000/alerts"
)

if response.status_code == 200:

    alerts = response.json()

    if len(alerts) > 0:
        df = pd.DataFrame(alerts)
        st.dataframe(df)