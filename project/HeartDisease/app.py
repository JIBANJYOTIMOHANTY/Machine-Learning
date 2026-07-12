# pyrefly: ignore [missing-import]
import streamlit as st
import pandas as pd
import joblib

model = joblib.load('./pklFiles/Logistic_Heart_Model.pkl')
scaler = joblib.load('./pklFiles/scaler.pkl')
columns = joblib.load('./pklFiles/columns.pkl')

st.title('Heart Disease Prediction')

st.header('Enter your details')

age = st.slider('Age', min_value=18, max_value=100, value=25)
sex = st.selectbox('Sex', ['Male', 'Female'])
chest_pain = st.selectbox('Chest Pain', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic', 'ATA'])
blood_pressure = st.number_input('Blood Pressure (mm Hg)', min_value=0, max_value=200, value=120)
target_cholestoral = st.number_input('Target Cholestoral (mg/dl)', min_value=100, max_value=600, value=200)
fasting_bs = st.selectbox('Fasting Blood Sugar', ['Yes', 'No'])
fasting_ecg = st.selectbox('Resting ECG', ['Normal', 'ST-T Wave Abnormality', 'Ventricular Hypertrophy'])
max_hr = st.slider('Maximum Heart Rate', min_value=60, max_value=220, value=150)
exercise_anagia = st.selectbox("Exercise Included Anagia", ["Yes", "No"])
old_peak = st.slider("Old Peak ", min_value=0.0, max_value=6.2, value=0.0)
st_slope = st.selectbox("ST Slope", ["UP", "Flat", "Down"])

if(st.button('Predict')):
    # Map user inputs to training features
    cp_map = {
        'Typical Angina': 'TA',
        'Atypical Angina': 'ATA',
        'Non-anginal Pain': 'NAP',
        'Asymptomatic': 'ASY',
        'ATA': 'ATA'
    }
    ecg_map = {
        'Normal': 'Normal',
        'ST-T Wave Abnormality': 'ST',
        'Ventricular Hypertrophy': 'LVH'
    }
    
    cp_val = cp_map[chest_pain]
    ecg_val = ecg_map[fasting_ecg]
    
    raw_input = {
        'Age': age,
        'RestingBP': blood_pressure,
        'Cholesterol': target_cholestoral,
        'FastingBS': 1 if fasting_bs == 'Yes' else 0,
        'MaxHR': max_hr,
        'Oldpeak': old_peak,
        'Sex_M': 1 if sex == 'Male' else 0,
        'ChestPainType_ATA': 1 if cp_val == 'ATA' else 0,
        'ChestPainType_NAP': 1 if cp_val == 'NAP' else 0,
        'ChestPainType_TA': 1 if cp_val == 'TA' else 0,
        'RestingECG_Normal': 1 if ecg_val == 'Normal' else 0,
        'RestingECG_ST': 1 if ecg_val == 'ST' else 0,
        'ExerciseAngina_Y': 1 if exercise_anagia == 'Yes' else 0,
        'ST_Slope_Flat': 1 if st_slope == 'Flat' else 0,
        'ST_Slope_Up': 1 if st_slope == 'UP' else 0
    }
    
    input_df = pd.DataFrame([raw_input])
    input_df = input_df[columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]
    
    if(prediction == 1):
        st.write("You have heart disease")
    else:
        st.write("You don't have heart disease")