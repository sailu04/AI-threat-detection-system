# 🛡️ AI-Based Insider Threat Detection System

## 📌 Overview

This project is an **AI-powered cybersecurity system** designed to detect potential insider threats within an organization.

The system analyzes user login behavior and identifies abnormal activity using **machine learning anomaly detection techniques**. It mimics a simplified **User and Entity Behavior Analytics (UEBA)** system used in modern Security Operations Centers (SOC).

The project also includes an interactive monitoring dashboard for visualizing suspicious users and threat indicators.

---

# 🚨 Problem Statement

Insider threats are among the most difficult cybersecurity risks to detect because malicious activity originates from trusted users within the organization.

Traditional rule-based systems often fail to detect subtle behavioral anomalies.
This project addresses the problem using **machine learning-based anomaly detection** to identify unusual user behavior patterns.

---

# ⚙️ System Architecture

User Activity Logs
⬇
Feature Engineering
⬇
Machine Learning Anomaly Detection
⬇
Risk Scoring Engine
⬇
Security Monitoring Dashboard

---

# 🧠 Key Features

✔ User behavior analysis from login activity logs
✔ Feature engineering for behavioral indicators
✔ AI-based anomaly detection using Isolation Forest
✔ Insider threat risk scoring system
✔ Interactive security monitoring dashboard
✔ Real-time log simulation
✔ Automated threat alerts

---

# 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Plotly
* Machine Learning (Isolation Forest)

---

# 📂 Project Structure

AI_INSIDER_THREAT

dashboard/
  app.py → Security monitoring dashboard

models/
  anomaly_detection.py → AI anomaly detection model
  realtime_detection.py → Real-time threat detection

preprocessing/
  load_data.py → Dataset loading and preprocessing

simulation/
  generate_logs.py → Real-time log simulation

dataset/
  logon.csv → User activity dataset (not included in repo)

README.md
requirements.txt

---

# 📊 Dashboard Features

The monitoring dashboard provides:

* Security alerts for high-risk users
* Risk score visualization
* Login behavior analysis
* Top insider threat identification
* Interactive charts for user activity

---

# 🧪 Machine Learning Model

The system uses the **Isolation Forest algorithm** for anomaly detection.

Isolation Forest works by isolating unusual behavior patterns in the dataset.
Users whose behavior significantly deviates from normal activity are flagged as potential insider threats.

---

# 📥 Dataset

This project uses the **CERT Insider Threat Dataset**.

Due to GitHub file size limitations, the dataset is not included in this repository.

Download the dataset and place it in:

dataset/logon.csv

---

# ▶️ Running the Project

## Install dependencies

pip install -r requirements.txt

## Run anomaly detection

python models/anomaly_detection.py

## Launch the dashboard

python -m streamlit run dashboard/app.py

---

# 📈 Example Use Cases

* Detect abnormal login patterns
* Identify suspicious employee activity
* Monitor potential insider threats
* Behavioral analytics in cybersecurity

---

# 🚀 Future Improvements

* Real-time log ingestion from enterprise systems
* Deep learning-based anomaly detection
* Network activity monitoring
* Integration with SIEM platforms
* Advanced threat visualization dashboards

---

# 👨‍💻 Author

Cybersecurity student project focused on **AI-driven threat detection and behavioral analytics**.
