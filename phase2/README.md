# Phase 2: Fraud Detection API 

---

## Overview

This phase converts the trained Machine Learning model into a real-time API using FastAPI.

The API accepts transaction details and returns:

* Fraud prediction (0 = Safe, 1 = Fraud)
* Risk score (0–100%)

---

## Tech Used

* Python
* FastAPI
* Pandas
* Joblib

---

## Files

* `fraud_api.py` → API server for fraud prediction

---

## How to Run

### 1. Install dependencies

```bash
pip install fastapi uvicorn pandas joblib
```

---

### 2. Start the API

```bash
python -m uvicorn fraud_api:app --reload
```

---

### 3. Open in browser

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST `/predict`

#### Input:

```json
{
  "user_id": "user_1",
  "amount": 1800,
  "transaction_time": "2026-03-17 10:30:00",
  "device_id": "device_10",
  "location": "Chicago",
  "merchant": "Amazon"
}
```

---

#### Output:

```json
{
  "fraud_prediction": 1,
  "risk_score": 82.45
}
```

---

## How It Works

* Loads trained model from Phase 1
* Applies feature engineering on input data
* Aligns input with trained model features
* Predicts fraud probability

---

## Important Note

The model may not always flag high-value transactions as fraud.

This is because **behavioral context is simplified in this phase**, including:

* No real-time user transaction history
* Device and location change are approximated
* Transaction velocity is not dynamically tracked

These limitations will be addressed in **Phase 3**, where real-time user behavior tracking will be implemented.

---

##  Next Phase

Phase 3 will introduce:

* Real-time transaction simulation
* User behavior tracking
* Improved fraud detection accuracy

---

## Goal

Move from a static ML model to a **real-time intelligent fraud detection system**.
