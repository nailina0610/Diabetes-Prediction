# import library
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load Files
with open('model_DT.pkl', 'rb') as  file_1: 
  model_DT = pickle.load(file_1)

def run():
    # buat form imputan
    with st.form('form_diabetes'):
        gender = st.selectbox('Jenis Kelamin', ('Female', 'Male', 'Other'))
        age = st.slider('Usia', min_value=0, max_value=80),  
        hypertension_options = {'0': 'Tidak hipertensi', '1': 'Hipertensi'}
        hypertension = st.selectbox('Hipertensi', options=list(hypertension_options.keys()), format_func=lambda x: hypertension_options[x])
        heart_disease_options = {'0': 'Tidak ada penyakit jantung', '1': 'Ada penyakit jantung'}
        heart_disease = st.selectbox('Penyakit Jantung', options=list(heart_disease_options.keys()), format_func=lambda x: heart_disease_options[x])
        smoking_history = st.selectbox('Riwayat Merokok', ('never', 'No Info', 'current', 'former', 'ever', 'not current'))
        bmi = st.slider('BMI', min_value=10.01, max_value=95.69)
        HbA1c_level = st.slider('Tingkat HbA1c', min_value=3.50, max_value=9.00)
        blood_glucose_level = st.slider('Tingkat Glukosa Darah', min_value=80, max_value=300)

        # submit button
        submitted = st.form_submit_button('Predict')

    data_inf = {
        'gender': 'Male',
        'age': 34.0,
        'hypertension': 0,
        'heart_disease': 0,
        'smoking_history': 'current',
        'bmi': 28.73,
        'HbA1c_level': 4.0,
        'blood_glucose_level': 100
    }

    data_inf = pd.DataFrame([data_inf])
    data_inf

    if submitted:
        # predict
        y_pred_inf = model_DT.predict(data_inf)
        # predict akan dishow sesuai hasil
        if y_pred_inf == 1:
            st.write('**Prediksi menunjukkan kemungkinan terjadinya diabetes**')
        else:
            st.write('**Prediksi menunjukkan kemungkinan tidak terjadinya diabetes**')

    # membuat garis pemisah
    st.markdown('---')
    
    # Kalimat penutup
    st.write('_Semoga hasil prediksinya menunjukkan kamu sehat yaa. Tetap jaga kesehatan:)_')
    st.write('***SALAM SEHAT SELALU ~***')
    
# untuk running
if __name__ == '__main__':
   run()