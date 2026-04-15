import joblib
import pandas as pd

# Load model
model = joblib.load("model_pipeline.pkl")

def predict_churn(input_data: dict):
    # Convert input to DataFrame
    df = pd.DataFrame([input_data])

    # Prediction
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return prediction, probability