import pandas as pd
from sklearn.ensemble import IsolationForest

# Load feature dataset
data = pd.read_csv("dataset/user_behavior_features.csv")

# Select features
X = data[["login_count", "pcs_used", "avg_login_hour"]]

# Train model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X)

# Predict anomaly
data["anomaly"] = model.predict(X)

# Get anomaly scores
data["anomaly_score"] = model.decision_function(X)

# Convert to positive risk score
data["risk_score"] = (1 - data["anomaly_score"]) * 100


# Assign risk levels
def risk_level(score):
    if score > 80:
        return "HIGH"
    elif score > 50:
        return "MEDIUM"
    else:
        return "LOW"


data["risk_level"] = data["risk_score"].apply(risk_level)

# Show suspicious users
suspicious = data[data["risk_level"] == "HIGH"]

print("\n⚠ High Risk Users")
print(suspicious)

# Save results
data.to_csv("dataset/threat_detection_results.csv", index=False)

print("\nResults saved successfully")