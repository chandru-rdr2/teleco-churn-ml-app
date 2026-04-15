import streamlit as st
from src.predict import predict_churn

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Telecom Churn Prediction",
    layout="wide"
)

# ------------------ CUSTOM STYLE ------------------
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: #e5e7eb;
    }
    h1 {
        color: #d4af37; /* gold */
        text-align: center;
    }
    .stButton>button {
        background-color: #d4af37;
        color: black;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #b8962e;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.title("📊 Telecom Customer Churn Prediction")
st.write("Predict whether a customer will churn or not")

# ------------------ SIDEBAR INPUT ------------------
st.sidebar.header("Customer Inputs")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
Partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
Dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])

tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)

PhoneService = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.sidebar.selectbox("Multiple Lines", ["Yes", "No"])

InternetService = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

OnlineSecurity = st.sidebar.selectbox("Online Security", ["Yes", "No"])
OnlineBackup = st.sidebar.selectbox("Online Backup", ["Yes", "No"])
DeviceProtection = st.sidebar.selectbox("Device Protection", ["Yes", "No"])
TechSupport = st.sidebar.selectbox("Tech Support", ["Yes", "No"])

StreamingTV = st.sidebar.selectbox("Streaming TV", ["Yes", "No"])
StreamingMovies = st.sidebar.selectbox("Streaming Movies", ["Yes", "No"])

Contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])

PaymentMethod = st.sidebar.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

MonthlyCharges = st.sidebar.number_input("Monthly Charges", value=50.0)
TotalCharges = st.sidebar.number_input("Total Charges", value=500.0)

# ------------------ INPUT DICTIONARY ------------------
input_data = {
    'gender': gender,
    'SeniorCitizen': SeniorCitizen,
    'Partner': Partner,
    'Dependents': Dependents,
    'tenure': tenure,
    'PhoneService': PhoneService,
    'MultipleLines': MultipleLines,
    'InternetService': InternetService,
    'OnlineSecurity': OnlineSecurity,
    'OnlineBackup': OnlineBackup,
    'DeviceProtection': DeviceProtection,
    'TechSupport': TechSupport,
    'StreamingTV': StreamingTV,
    'StreamingMovies': StreamingMovies,
    'Contract': Contract,
    'PaperlessBilling': PaperlessBilling,
    'PaymentMethod': PaymentMethod,
    'MonthlyCharges': MonthlyCharges,
    'TotalCharges': TotalCharges
}

# ------------------ BUTTON + OUTPUT ------------------
if st.button("🚀 Predict Churn"):

    prediction, probability = predict_churn(input_data)

    st.markdown("---")

    # RESULT
    if prediction == 1:
        st.error(f"⚠️ Customer is likely to churn")
    else:
        st.success(f"✅ Customer is not likely to churn")

    # PROBABILITY
    st.subheader("📊 Prediction Confidence")

    prob_percent = int(probability * 100)

    st.progress(prob_percent)
    st.write(f"Churn Probability: **{prob_percent}%**")

# ------------------ FOOTER ------------------
st.markdown("---")
st.write("Built with Machine Learning & Streamlit 🚀")