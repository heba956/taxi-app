import streamlit as st
import pandas as pd
import joblib
import numpy as np
st.title('The Survivors')
st.info('Welcome to Survivors Team's App')

model1 = joblib.load("taxi_model.pkl")
model2 =joblib.load("")
columns = [
    'passenger_count', 'trip_distance', 'pickup_longitude', 'pickup_latitude',
    'dropoff_longitude', 'dropoff_latitude', 'improvement_surcharge',
    'trip_duration', 'pickup_month', 'pickup_day', 'pickup_hour', 'pickup_minute',
    'distance_km', 'VendorID_2', 'RatecodeID_2.0', 'RatecodeID_3.0', 
    'RatecodeID_4.0', 'RatecodeID_5.0', 'RatecodeID_6.0', 'RatecodeID_99.0'
]

# تقسيم الأعمدة حسب النوع لتسهيل الإدخال
numeric_cols = [
    'passenger_count', 'trip_distance', 'pickup_longitude', 'pickup_latitude',
    'dropoff_longitude', 'dropoff_latitude', 'improvement_surcharge',
    'trip_duration', 'pickup_month', 'pickup_day', 'pickup_hour', 'pickup_minute',
    'distance_km'
]

onehot_cols = [
    'VendorID_2', 'RatecodeID_2.0', 'RatecodeID_3.0', 'RatecodeID_4.0',
    'RatecodeID_5.0', 'RatecodeID_6.0', 'RatecodeID_99.0'
]

st.title("Taxi Trip Fare Prediction")

st.header("Enter Trip Details:")

# ------------------------------
# 3️⃣ إدخال القيم Numeric
# ------------------------------
input_data = {}
for col in numeric_cols:
    if 'count' in col or 'month' in col or 'day' in col or 'hour' in col or 'minute' in col:
        input_data[col] = st.number_input(col.replace("_", " ").title(), value=1, step=1)
    else:
        input_data[col] = st.number_input(col.replace("_", " ").title(), value=0.0, step=0.1, format="%.6f")

# ------------------------------
# 4️⃣ إدخال القيم One-Hot (Checkbox)
# ------------------------------
st.subheader("Vendor & Ratecode Selection:")
for col in onehot_cols:
    input_data[col] = int(st.checkbox(col, value=False))

# ------------------------------
# 5️⃣ تحويل الإدخال لـ DataFrame
# ------------------------------
input_df = pd.DataFrame([input_data])
st.write("Input Data Preview:", input_df)

# ------------------------------
# 6️⃣ زر التنبؤ
# ------------------------------
if st.button("Predict Fare"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Fare: ${prediction[0]:.2f}")

if st.button("Predict"):
    X = np.array([[distance, passengers]])
    pred = model.predict(X)
    st.write("Price:", pred[0])

