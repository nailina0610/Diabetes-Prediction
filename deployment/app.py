# import library
import streamlit as st
import eda
import prediction

# membuat pilihan halaman
page = st.sidebar.selectbox('Pilih Halaman: ', ('EDA', 'Prediction'))

# running sesuai pilihan halaman
if page == 'EDA':
    eda.run()
else:
    prediction.run()