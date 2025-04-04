import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction of Disease Outbreaks",
                   layout="wide",
                   page_icon="❤️")

# Load trained models
diabetes_model = pickle.load(
    open(r'C:\Users\agark\OneDrive\Desktop\streamlit\diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(
    open(r'C:\Users\agark\OneDrive\Desktop\streamlit\heart_disease_model.sav', 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreaks System',
                           ['Diabetes Prediction', 'Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart'],
                           default_index=0)

# ---------------- DIABETES PREDICTION ----------------
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    demo_options = {
        "📗 Healthy": {
            "Pregnancies": "1", "Glucose": "85", "BloodPressure": "66",
            "SkinThickness": "29", "Insulin": "0", "BMI": "26.6",
            "DiabetesPedigreeFunction": "0.351", "Age": "31"
        },
        "🟠 Borderline": {
            "Pregnancies": "2", "Glucose": "125", "BloodPressure": "70",
            "SkinThickness": "32", "Insulin": "0", "BMI": "30.1",
            "DiabetesPedigreeFunction": "0.58", "Age": "33"
        },
        "🔴 Diabetic": {
            "Pregnancies": "7", "Glucose": "160", "BloodPressure": "72",
            "SkinThickness": "38", "Insulin": "130", "BMI": "41.3",
            "DiabetesPedigreeFunction": "0.720", "Age": "50"
        }
    }

    demo_choice = st.selectbox(
        "Choose a Demo Case", options=list(demo_options.keys()))

    if st.button("📥 Load Selected Demo"):
        for key, val in demo_options[demo_choice].items():
            st.session_state[key] = val

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', key="Pregnancies")

    with col2:
        Glucose = st.text_input('Glucose Level', key="Glucose")

    with col3:
        BloodPressure = st.text_input(
            'Blood Pressure value', key="BloodPressure")

    with col1:
        SkinThickness = st.text_input(
            'Skin Thickness value', key="SkinThickness")

    with col2:
        Insulin = st.text_input('Insulin Level', key="Insulin")

    with col3:
        BMI = st.text_input('BMI value', key="BMI")

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            'Diabetes Pedigree Function value', key="DiabetesPedigreeFunction")

    with col2:
        Age = st.text_input('Age of the Person', key="Age")

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(BloodPressure),
                          float(SkinThickness), float(Insulin), float(BMI),
                          float(DiabetesPedigreeFunction), float(Age)]

            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = '✅ The person is diabetic'
            else:
                diab_diagnosis = '✅ The person is not diabetic'
        except:
            diab_diagnosis = '❌ Please enter valid numeric values.'

    st.success(diab_diagnosis)

# ---------------- HEART DISEASE PREDICTION ----------------
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    heart_demo_options = {
        "📗 Healthy": {
            "age": "58", "sex": "1", "cp": "2", "trestbps": "140", "chol": "230",
            "fbs": "0", "restecg": "1", "thalach": "150", "exang": "1",
            "oldpeak": "2.3", "slope": "0", "ca": "1", "thal": "2"
        },
        "🟠 Borderline": {
            "age": "50", "sex": "1", "cp": "1", "trestbps": "130", "chol": "245",
            "fbs": "0", "restecg": "1", "thalach": "140", "exang": "0",
            "oldpeak": "1.5", "slope": "1", "ca": "0", "thal": "1"
        },
        "🔴 Heart Disease": {
            "age": "35","sex": "0","cp": "0","trestbps": "90","chol": "180",           
            "fbs": "0","restecg": "0","thalach": "100","exang": "0",            
            "oldpeak": "0.0","slope": "1","ca": "0","thal": "1"
        }
    }

    heart_demo_choice = st.selectbox(
        "Choose a Demo Case", options=list(heart_demo_options.keys()))

    if st.button("📥 Load Selected Heart Demo"):
        for key, val in heart_demo_options[heart_demo_choice].items():
            st.session_state[key] = val

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age', key="age")

    with col2:
        sex = st.text_input('Sex (0 = Female, 1 = Male)', key="sex")

    with col3:
        cp = st.text_input('Chest Pain Type (0–3)', key="cp")

    with col1:
        trestbps = st.text_input('Resting Blood Pressure', key="trestbps")

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', key="chol")

    with col3:
        fbs = st.text_input(
            'Fasting Blood Sugar > 120 mg/dl (1 = True; 0 = False)', key="fbs")

    with col1:
        restecg = st.text_input('Resting ECG results (0–2)', key="restecg")

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', key="thalach")

    with col3:
        exang = st.text_input(
            'Exercise Induced Angina (1 = yes; 0 = no)', key="exang")

    with col1:
        oldpeak = st.text_input(
            'ST depression induced by exercise', key="oldpeak")

    with col2:
        slope = st.text_input(
            'Slope of the peak exercise ST segment (0–2)', key="slope")

    with col3:
        ca = st.text_input(
            'Major vessels colored by flourosopy (0–3)', key="ca")

    with col1:
        thal = st.text_input(
            'Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', key="thal")

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            user_input = [float(age), float(sex), float(cp), float(trestbps), float(chol),
                          float(fbs), float(restecg), float(
                              thalach), float(exang),
                          float(oldpeak), float(slope), float(ca), float(thal)]

            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = '✅ The person is having heart disease'
            else:
                heart_diagnosis = '✅ The person does not have any heart disease'
        except:
            heart_diagnosis = '❌ Please enter valid numeric values.'

    st.success(heart_diagnosis)
