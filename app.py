import streamlit as st
import plotly.graph_objects as go
from src.predict import predict_churn

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Telecom Churn AI", layout="wide")

# ------------------ THEME SELECTOR ------------------
st.sidebar.title("🎨 Theme Customization")

theme = st.sidebar.selectbox(
    "Choose Theme",
    ["Light", "Dark", "Gold", "Silver", "Pale Pink"]
)

# ------------------ THEME COLORS ------------------
if theme == "Light":
    bg = "#ffffff"
    text = "#000000"
    card = "#f1f5f9"
    accent = "#2563eb"

elif theme == "Dark":
    bg = "#000000"
    text = "#ffffff"
    card = "#111827"
    accent = "#22c55e"

elif theme == "Gold":
    bg = "#FFD700"
    text = "#000000"
    card = "rgba(255,255,255,0.6)"
    accent = "#b45309"

elif theme == "Silver":
    bg = "#C0C0C0"
    text = "#000000"
    card = "rgba(255,255,255,0.7)"
    accent = "#374151"

elif theme == "Pale Pink":
    bg = "#fbcfe8"
    text = "#000000"
    card = "rgba(255,255,255,0.8)"
    accent = "#be185d"

# ------------------ FORCE FULL BACKGROUND FIX ------------------
st.markdown(f"""
<style>

/* FORCE FULL PAGE BACKGROUND */
.stApp {{
    background-color: {bg} !important;
    color: {text} !important;
}}

/* REMOVE DEFAULT HEADER */
header, footer {{
    visibility: hidden;
}}

/* MAIN AREA */
.block-container {{
    padding-top: 2rem;
}}

/* CARD DESIGN */
.card {{
    background: {card};
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}}

/* TITLE */
.title {{
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: {accent};
}}

/* BUTTON */
.stButton>button {{
    width: 100%;
    height: 50px;
    border-radius: 12px;
    border: none;
    background: {accent};
    color: white;
    font-size: 16px;
    font-weight: bold;
}}

.stButton>button:hover {{
    opacity: 0.85;
}}

/* TEXT COLOR FIX */
label, .stMarkdown, .stText {{
    color: {text} !important;
}}

</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="title">📊 Telecom Churn AI</div>', unsafe_allow_html=True)
st.write("### 🤖 Smart Customer Retention System")

# ------------------ LAYOUT ------------------
col1, col2 = st.columns([1, 2], gap="large")

# ------------------ INPUT SECTION ------------------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Customer Details")

    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])

    tenure = st.slider("Tenure", 0, 72, 12)

    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No"])

    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No"])

    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No"])

    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])

    PaymentMethod = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]
    )

    MonthlyCharges = st.number_input("Monthly Charges", value=50.0)
    TotalCharges = st.number_input("Total Charges", value=500.0)

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ INPUT DATA ------------------
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

# ------------------ OUTPUT SECTION ------------------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Prediction Result")

    if st.button("🚀 Predict"):
        prediction, probability = predict_churn(input_data)

        churn = probability
        stay = 1 - probability

        if prediction == 1:
            st.error("⚠️ High Risk Customer")
        else:
            st.success("✅ Safe Customer")

        st.subheader("Confidence")

        st.progress(int(churn * 100))
        st.write(f"### {int(churn * 100)}% Churn Probability")

        # CHART
        fig = go.Figure(data=[
            go.Bar(x=["Stay", "Churn"], y=[stay, churn])
        ])

        fig.update_layout(
            plot_bgcolor=bg,
            paper_bgcolor=bg,
            font=dict(color=text)
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown(
    "<center>🚀 Portfolio Project | AI + Streamlit</center>",
    unsafe_allow_html=True
)