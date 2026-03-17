import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import joblib

df=pd.read_csv("synthetic_upi_data.csv")
df["transaction_time"]=pd.to_datetime(df["transaction_time"])  #convert to datetime
df=df.sort_values(["user_id", "transaction_time"]).reset_index(drop=True)  #sort by user and time

df["txn_last_10min"]=(df.groupby("user_id").rolling("10min", on="transaction_time")["amount"].count().reset_index(drop= True))
df["hour"]=pd.to_datetime(df["transaction_time"]).dt.hour  #hour of transaction
df["txn_count_user"]=df.groupby("user_id")["amount"].transform("count")  #number of transactions by user
df["user_av"]=df.groupby("user_id")["amount"].transform("mean")  #average transaction amount by user
df["amount_deviation"]=df["amount"]-df["user_av"]  #deviation from user's average

df["device_changed"]=(df.groupby("user_id")["device_id"].transform(lambda x: x != x.shift(1)).astype(int))  #device change indicator

df["location_changed"]=(df.groupby("user_id")["location"].transform(lambda x: x != x.shift(1)).astype(int))  #location change indicator

df_encoded=pd.get_dummies(df, columns=["device_id", "location", "merchant"], drop_first=True)

X=df_encoded.drop(["label", "user_id", "transaction_time"], axis=1)
y=df_encoded["label"]

#train
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)

#model
model=RandomForestClassifier(n_estimators=150, random_state=42, class_weight="balanced")
model.fit(X_train, y_train)

#prediction
y_pred=model.predict(X_test)
print("\nModel Performance:\n")
print(classification_report(y_test, y_pred))

#risk score
df["risk_score"]=model.predict_proba(X)[:, 1]*100  #probability
df["risk_score"]=df["risk_score"].round(2)  #rounding

print("\nTop transactions with high risk scores:\n")
print(df.sort_values("risk_score", ascending=False)[["user_id", "amount", "risk_score", "location", "merchant"]].head(10))

plt.figure(figsize=(8, 5))
df["risk_score"].hist(bins=50)
plt.title("Distribution of Risk Scores")
plt.xlabel("Risk Score")
plt.ylabel("Number of transactions")
plt.show()

#save model
joblib.dump(model, "fraud_detection_model.pkl")
joblib.dump(X.columns, "model_features.pkl")  #save feature names for later use
print("\nModel saved as 'fraud_detection_model.pkl'.")
print("Feature names saved as 'model_features.pkl'.")
