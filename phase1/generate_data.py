import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

num_user=100
transactions_per_user=200

users=[f"user_{i}" for i in range(num_user)]
locations=["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
merchants=["Amazon", "Walmart", "Target", "Best Buy", "eBay"]
devices=[f"device_{i}" for i in range(50)]

data=[]
for user in users:
    base_amount=random.uniform(200, 1500)
    last_time=  datetime.now() - timedelta(days=365)

    for i in range(transactions_per_user):
        amount=abs(np.random.normal(base_amount, 300))
        fraud=0

        device=random.choice(devices)
        location=random.choice(locations)
        txn_time=last_time + timedelta(minutes=random.randint(10, 600))

        if random.random() < 0.03:  # 3% fraud
            fraud=1
            amount=random.uniform(1500, 1999)

            txn_time=last_time + timedelta(minutes=random.randint(1, 5))  #fraud happens within 10 min of last txn
            device=random.choice(devices)
            location=random.choice(locations)
            
        last_time=txn_time

        data.append([
            user,
            amount,
            txn_time,
            device,
            location,
            random.choice(merchants),
            fraud
        ])

df=pd.DataFrame(data, columns=["user_id", "amount", "transaction_time", "device_id", "location", "merchant", "label"])
df.to_csv("synthetic_upi_data.csv", index=False)
print("Synthetic UPI transaction data generated and saved to 'synthetic_upi_data.csv'.")
