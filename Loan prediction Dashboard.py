import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import joblib

# Load your trained model (make sure this file exists in your project directory)
model = joblib.load("Loan_approval_predictions.pkl")

st.title("🧠 Loan Approval Outcome Predictor")

st.markdown("Enter customer details below to check if the loan will be approved.")

with st.form("prediction_form"):
    customer_name = st.text_input("Customer Name")

    monthly_installment = st.number_input("Monthly Installment", min_value=0.0)
    account_age = st.number_input("Account Age (Years)", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0.0)
    interest_rate = st.number_input("Interest Rate", min_value=0.0)
    credit_limit = st.number_input("Credit Limit", min_value=0.0)
    credit_card_balance = st.number_input("Credit Card Balance", min_value=0.0)
    account_balance = st.number_input("Account Balance", min_value=0.0)

    submitted = st.form_submit_button("Predict")

if submitted:
    # === AUTO-CALCULATED METRICS ===
    credit_usage_ratio = credit_card_balance / (credit_limit + 1)
    debt_burden_score = (loan_amount + credit_card_balance) / (account_balance + 1)
    trust_index = (account_age * credit_limit) / (loan_amount + 1)
    
    # Show calculated values
    st.markdown("### 🧠 Auto-Calculated Metrics")
    st.write(f"**Credit Usage Ratio**: `{credit_usage_ratio:.4f}`")
    st.write(f"**Debt Burden Score**: `{debt_burden_score:.4f}`")
    st.write(f"**Trust Index**: `{trust_index:.2f}`")

    # Prepare input for prediction model
    new_data = pd.DataFrame([{
        "Monthly_Installment": monthly_installment,
        "Account Age (Years)": account_age,
        "Loan Amount": loan_amount,
        "Interest Rate": interest_rate,
        "Credit Limit": credit_limit,
        "Credit Card Balance": credit_card_balance,
        "Credit_Usage_Ratio": credit_usage_ratio,
        "Debt_Burden_Score": debt_burden_score,
        "Trust_Index": trust_index
    }])

    # Make prediction (assuming your model is loaded as `model`)
    prediction = model.predict(new_data)[0]

    st.success(f"Prediction for **{customer_name or 'Unnamed'}**: **{'Qualified ✅' if prediction == 1 else 'Not Qualified ❌'}**")

