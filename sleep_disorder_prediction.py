import numpy as np
import pickle
import streamlit as st

# Load the saved model
loaded_model = pickle.load(open("sleep_disorder_prediction.pkl", "rb"))

# Streamlit App
st.title("Sleep Disorder Prediction App")

# Input fields
sleep_duration = st.number_input("Sleep Duration", value=0.0)
quality_of_sleep = st.number_input("Quality of Sleep", value=0.0)
physical_activity_level = st.number_input("Physical Activity Level", value=0.0)
stress_level = st.number_input("Stress Level", value=0.0)
heart_rate = st.number_input("Heart Rate", value=0.0)
daily_steps = st.number_input("Daily Steps", value=0.0)
systolic_bp = st.number_input("Systolic BP", value=0.0)
diastolic_bp = st.number_input("Diastolic BP", value=0.0)
bmi_score = st.number_input("BMI Score", value=0.0)
health_risk_score = st.number_input("Health Risk Score", value=0.0)
sti = st.number_input("STI", value=0.0)
sleep_disorder_cod = st.number_input("Sleep Disorder Code", value=0)
bmi_category_cod = st.number_input("BMI Category Code", value=0)
gender_cod = st.number_input("Gender Code", value=0)
occupation_cod = st.number_input("Occupation Code", value=0)

# Prediction function
def predict_sleep_disorder():
    input_values = np.array([
        sleep_duration, quality_of_sleep, physical_activity_level,
        stress_level, heart_rate, daily_steps, systolic_bp,
        diastolic_bp, bmi_score, health_risk_score, sti,
        sleep_disorder_cod, bmi_category_cod, gender_cod,
        occupation_cod
    ]).reshape(1, -1)
    
    prediction = loaded_model.predict(input_values)
    
    if prediction[0] == 0:
        return "Patient has no sleep disorder."
    elif prediction[0] == 1 or prediction[0] == 2:
        return "Patient has a sleep disorder."

# Prediction button
if st.button("Predict"):
    result = predict_sleep_disorder()
    st.success(f"Prediction: {result}")
