import streamlit as st
import pickle
import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

model = pickle.load(open("ott_model.pkl", "rb"))

st.title("OTT Churn Predictor & Revenue Impact")
st.caption("Predict which users will cancel their subscription")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 70, 35)
    watch_hours = st.slider("Total Watch Hours", 0, 100, 20)
    last_login = st.slider("Days Since Last Login", 0, 60, 15)
    monthly_fee = st.selectbox("Monthly Fee ($)", [8.99, 13.99, 17.99])

with col2:
    subscription = st.selectbox("Subscription", ["Basic","Standard","Premium"])
    device = st.selectbox("Device", ["Mobile","TV","Tablet","Laptop"])
    profiles = st.slider("Number of Profiles", 1, 5, 2)
    avg_watch = st.slider("Avg Daily Watch Time (hrs)", 0.0, 5.0, 1.0)

gender = st.selectbox("Gender", ["Male","Female","Other"])
region = st.selectbox("Region", ["Asia","Europe","North America","South America","Africa","Oceania"])
payment = st.selectbox("Payment Method", ["Credit Card","Debit Card","Gift Card","Crypto"])
genre = st.selectbox("Favorite Genre", ["Action","Drama","Comedy","Sci-Fi","Horror","Romance"])

le = LabelEncoder()

def encode(val, options):
    return sorted(options).index(val)

if st.button("Predict Churn Risk"):
    features = [[
        age,
        encode(gender, ["Female","Male","Other"]),
        encode(subscription, ["Basic","Premium","Standard"]),
        watch_hours,
        last_login,
        encode(region, ["Africa","Asia","Europe","North America","Oceania","South America"]),
        encode(device, ["Laptop","Mobile","TV","Tablet"]),
        monthly_fee,
        encode(payment, ["Credit Card","Crypto","Debit Card","Gift Card"]),
        profiles,
        avg_watch,
        encode(genre, ["Action","Comedy","Drama","Horror","Romance","Sci-Fi"])
    ]]
    
    prob = model.predict_proba(features)[0][1]
    pred = model.predict(features)[0]
    
    if prob >= 0.7:
        risk = "HIGH RISK"
        color = "error"
        action = "Offer 20% discount immediately"
    elif prob >= 0.3:
        risk = "MEDIUM RISK"
        color = "warning"
        action = "Send personalized content recommendations"
    else:
        risk = "LOW RISK"
        color = "success"
        action = "No action needed — user is engaged"
    
    st.markdown("---")
    if color == "error":
        st.error(f"Churn Risk: {risk} ({prob*100:.1f}%)")
    elif color == "warning":
        st.warning(f"Churn Risk: {risk} ({prob*100:.1f}%)")
    else:
        st.success(f"Churn Risk: {risk} ({prob*100:.1f}%)")
    
    st.info(f"Recommended Action: {action}")
    st.metric("Monthly Revenue at Risk", f"${monthly_fee}")
