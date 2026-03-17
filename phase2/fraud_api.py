from fastapi import FastAPI
import joblib
import pandas as pd

app=FastAPI()

model=joblib.load("fraud_detection_model.pkl")
model_features=joblib.load("model_features.pkl")

@app.get("/")
def home():
    return {"message": "Welcome to the UPI Fraud Detection API! (running)"}

@app.post("/predict")
def predict(transaction: dict):
    df=pd.DataFrame([transaction]) #input into dataframe

    df["transaction_time"]=pd.to_datetime(df["transaction_time"])  #convert to datetime
    df["hour"]=df["transaction_time"].dt.hour  #hour of transaction

    df["txn_last_10min"]=1  #placeholder for rolling count(real time will improve this)
    df["txn_count_user"]=1  
    df["user_av"]=df["amount"]  
    df["amount_deviation"]=0

    df["device_changed"]=0
    df["location_changed"]=0

    df_encoded=pd.get_dummies(df, columns=["device_id", "location", "merchant"])

    for col in model_features:
        if col not in df_encoded.columns:
            df_encoded[col]=0

    df_encoded=df_encoded[model_features]  #align with model features

    #PREDICTION
    prediction=model.predict(df_encoded)[0]
    probability=model.predict_proba(df_encoded)[0][1]*100  #fraud probability

    return{
        "fraud_prediction": int(prediction),
        "risk_score": round(probability, 2)
    }