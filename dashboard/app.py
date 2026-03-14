import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="AI Insider Threat Detection",
    page_icon="🛡️",
    layout="wide"
)

# Title
st.title("🛡️ AI Insider Threat Detection System")

st.markdown("Monitor suspicious user behavior using AI anomaly detection.")

# Load dataset
data = pd.read_csv("dataset/threat_detection_results.csv")

# =========================
# KPI METRICS
# =========================

total_users = len(data)
high_risk = len(data[data["risk_level"] == "HIGH"])
medium_risk = len(data[data["risk_level"] == "MEDIUM"])
low_risk = len(data[data["risk_level"] == "LOW"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Users", total_users)
col2.metric("High Risk Users", high_risk)
col3.metric("Medium Risk Users", medium_risk)
col4.metric("Low Risk Users", low_risk)

st.divider()

# =========================
# ALERT SECTION
# =========================

st.subheader("🚨 Security Alerts")

alerts = data[data["risk_level"] == "HIGH"]

if len(alerts) > 0:
    for index, row in alerts.iterrows():
        st.error(f"⚠ Insider Threat Detected → User: {row['user']} | Risk Score: {row['risk_score']:.2f}")
else:
    st.success("No high-risk users detected")

st.divider()

# =========================
# CHARTS
# =========================

col5, col6 = st.columns(2)

with col5:
    st.subheader("Risk Score Distribution")
    fig = px.histogram(data, x="risk_score", color="risk_level")
    st.plotly_chart(fig, use_container_width=True)

with col6:
    st.subheader("User Login Behavior")
    fig2 = px.scatter(
        data,
        x="avg_login_hour",
        y="login_count",
        color="risk_level",
        hover_data=["user"]
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# =========================
# TOP THREATS
# =========================

st.subheader("🔥 Top Insider Threats")

top_threats = data.sort_values(by="risk_score", ascending=False).head(10)

st.dataframe(top_threats)

st.divider()

# =========================
# FULL DATA TABLE
# =========================

st.subheader("User Behavior Dataset")

st.dataframe(data)