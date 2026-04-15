import joblib
import pandas as pd

# Load model
model = joblib.load("model_pipeline.pkl")

def predict_churn(input_data: dict):
    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    # ----------- SIMPLE RULE-BASED EXPLANATION -----------
    reasons = []

    if input_data['Contract'] == "Month-to-month":
        reasons.append("Month-to-month contract")

    if input_data['TechSupport'] == "No":
        reasons.append("No tech support")

    if input_data['OnlineSecurity'] == "No":
        reasons.append("No online security")

    if input_data['InternetService'] == "Fiber optic":
        reasons.append("High-cost fiber internet")

    if input_data['MonthlyCharges'] > 70:
        reasons.append("High monthly charges")

    if input_data['tenure'] < 12:
        reasons.append("Low tenure (new customer)")

    return prediction, probability, reasons