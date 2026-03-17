
# Phase 1: CSV + ML Fraud Detection Model
---

## Overview

This phase builds the foundation of the fraud detection system:

* Synthetic UPI transaction generation
* Feature engineering
* Machine Learning model training
* Risk scoring

---

## Files

* `generate_data.py` → Generates synthetic UPI transaction data
* `train_model.py` → Trains fraud detection model
* `fraud_model.pkl` → Saved trained model
* `feature_columns.pkl` → Feature structure for prediction

---

## Steps to Run

### 1. Generate Data

```bash
python generate_data.py
```

### 2. Train Model

```bash
python train_model.py
```

---

## Features Used

* Transaction frequency
* Transaction amount deviation
* Transactions in last 10 minutes
* Device change detection
* Location change detection

---

## Output

* Model performance metrics
* Risk score for each transaction
* Top suspicious transactions

---

## Goal

Detect micro-fraud patterns in UPI transactions using behavioral analysis.
