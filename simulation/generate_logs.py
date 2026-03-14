import pandas as pd
import random
import time

users = [f"U{i}" for i in range(1,50)]
pcs = [f"PC{i}" for i in range(1,10)]

while True:

    new_log = {
        "user": random.choice(users),
        "login_count": random.randint(1,200),
        "pcs_used": random.randint(1,6),
        "avg_login_hour": random.randint(0,23)
    }

    df = pd.DataFrame([new_log])

    df.to_csv("dataset/live_logs.csv", mode="a", header=False, index=False)

    print("New log generated:", new_log)

    time.sleep(3)