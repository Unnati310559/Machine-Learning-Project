import streamlit as st
import joblib
import numpy as np

# -----------------------------
# Load Model (JOBLIB)
# -----------------------------
model = joblib.load("diabetes_model (1).pkl")   # <-- Change name if needed

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🩺 Diabetes Prediction App")
st.write("Fill the details below to check diabetes risk.")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=85)
bp = st.number_input("Blood Pressure", min_value=0, max_value=200, value=66)
skin = st.number_input("Skin Thickness", min_value=0, max_value=100, value=29)
insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=0)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=26.6)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=5.0, value=0.351)
age = st.number_input("Age", min_value=1, max_value=120, value=31)

# Prediction button
if st.button("Predict"):
    # Arrange inputs for prediction
    features = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])

    # Predict using model
    prediction = model.predict(features)[0]

    # Output
    if prediction == 1:
        st.error("🔴 High Risk: Patient is likely diabetic.")
    else:
        st.success("🟢 Low Risk: Patient is NOT likely diabetic.")

