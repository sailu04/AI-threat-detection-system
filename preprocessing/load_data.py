import pandas as pd

# 1️⃣ Load dataset
data = pd.read_csv("dataset/logon.csv")

print("Dataset loaded successfully")
print(data.head())


# 2️⃣ Convert date column to datetime
data["date"] = pd.to_datetime(data["date"])


# 3️⃣ Extract login hour
data["hour"] = data["date"].dt.hour


# 4️⃣ Filter only Logon events
logins = data[data["activity"] == "Logon"]


# 5️⃣ Feature 1: login count per user
login_counts = logins.groupby("user").size()


# 6️⃣ Feature 2: number of unique PCs used
pc_usage = logins.groupby("user")["pc"].nunique()


# 7️⃣ Feature 3: average login hour
avg_login_hour = logins.groupby("user")["hour"].mean()


# 8️⃣ Combine all features
features = pd.DataFrame({
    "login_count": login_counts,
    "pcs_used": pc_usage,
    "avg_login_hour": avg_login_hour
})


# 9️⃣ Handle missing values
features = features.fillna(0)


# 🔟 Reset index
features = features.reset_index()


# 11️⃣ Save processed dataset
features.to_csv("dataset/user_behavior_features.csv", index=False)


print("\nFeature dataset created successfully")
print(features.head())