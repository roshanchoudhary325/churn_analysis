import streamlit as st
import pandas as pd
import joblib

model = joblib.load("dtc_model.pkl")
encoder = joblib.load("encoder.pkl")

st.title("Bank Marketing Prediction")

age = st.number_input("Age", 18, 100, 35)
job = st.selectbox("Job", list(encoder['job'].classes_))
marital = st.selectbox("Marital", list(encoder['marital'].classes_))
education = st.selectbox("Education", list(encoder['education'].classes_))
default = st.selectbox("Default", list(encoder['default'].classes_))
balance = st.number_input("Balance", value=1000)
housing = st.selectbox("Housing", list(encoder['housing'].classes_))
loan = st.selectbox("Loan", list(encoder['loan'].classes_))
day = st.number_input("Day", 1, 31, 15)
month = st.selectbox("Month", list(encoder['month'].classes_))
duration = st.number_input("Duration", value=200)
campaign = st.number_input("Campaign", value=1)
pdays = st.number_input("Pdays", value=-1)
previous = st.number_input("Previous", value=0)

if st.button("Predict"):

    df = pd.DataFrame({
        'age': [age],
        'job': [job],
        'marital': [marital],
        'education': [education],
        'default': [default],
        'balance': [balance],
        'housing': [housing],
        'loan': [loan],
        'day_of_week': [day],
        'month': [month],
        'duration': [duration],
        'campaign': [campaign],
        'pdays': [pdays],
        'previous': [previous]
    })

    cat_cols = [
        'job',
        'marital',
        'education',
        'default',
        'housing',
        'loan',
        'month'
    ]

    for col in cat_cols:
        df[col] = encoder[col].transform(df[col])

    prediction = model.predict(df)

    if prediction[0] == 1:
        st.success("Customer Will Subscribe")
    else:
        st.error("Customer Will Not Subscribe")