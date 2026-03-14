import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("dataset/user_behavior_features.csv")

X = data[["login_count","pcs_used","avg_login_hour"]]

model = IsolationForest(contamination=0.05)

model.fit(X)


live_data = pd.read_csv("dataset/live_logs.csv")

live_data["anomaly"] = model.predict(live_data)

alerts = live_data[live_data["anomaly"] == -1]

print("⚠ Real-Time Threat Alerts")

print(alerts)