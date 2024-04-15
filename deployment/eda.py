# Import Library
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

# membuat title page
st. set_page_config(
    page_title= 'DIABETES PREDICTION'
)

def run():
    # membuat judul
    st.title('**DIABETES PREDICTION**')

    # membuat subheader
    st.subheader('EDA Dataset Prediksi Penyakit Diabetes')

    # tambahkan gambar
    image = Image.open('gambar.jpg')
    st.image(image, caption = '"Jangan biarkan gula menghancurkan hidupmu yang sudah manis :)"')

    # Membuat deskripsi
    st.write('**Selamat datang di page buatan Nailina Farah. Silahkan melihat visualisasi data tentang Diabetes pada halaman "EDA" dan silahkan cek kesehatanmu pada halaman "Prediction".**')
    st.write('_Diabetes adalah kondisi serius yang memengaruhi jutaan orang di seluruh dunia. Menjaga kesehatan tubuh adalah langkah penting untuk mencegah diabetes, mengingat dampak serius yang dapat ditimbulkannya. Diabetes dapat meningkatkan risiko penyakit jantung, stroke, gagal ginjal, kehilangan penglihatan, kerusakan saraf, dan komplikasi lainnya. Oleh karena itu, penting untuk menghindari diabetes dengan menerapkan gaya hidup sehat, termasuk makan makanan seimbang, berolahraga secara teratur, dan mengelola stres. Dengan mencegah diabetes, Anda dapat mempertahankan kualitas hidup yang baik dan mengurangi risiko komplikasi yang serius._')

    # membuat garis pemisah
    st.markdown('---')

    # membuat deskripsi dataset
    st.write('Berikut adalah Dataset Prediksi Diabetes yang diambil dari Kaggle: https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset.')
    # show dataframe
    df = pd.read_csv('diabetes_prediction_dataset.csv')
    st.dataframe(df)

    # Penjelasan Dataframe
    st.write('Dataset ini merupakan data mengenai prediksi diabetes yang terdiri dari 100000 baris data dan 9 kolom dimana 3 kolom bertipe float, 4 kolom bertipe integer, dan 2 kolom bertipe object')

    # VISUALISASI 1
    # Membuat dictionary untuk memetakan nama kolom asli ke nama yang ingin ditampilkan
    column_names = {
        'gender': 'Jenis Kelamin',
        'hypertension': 'Riwayat Hipertensi',
        'heart_disease': 'Riwayat Penyakit Jantung',
        'smoking_history': 'Status Merokok'
    }
    # Menambahkan penjelasan untuk visualisasi
    st.write('### Visualisasi Feature Kategorik')
    st.write('Visualisasi ini menampilkan frekuensi kategori pada kolom yang Anda pilih. Anda dapat memilih kolom untuk divisualisasikan dari dropdown di bawah.')
    # Memilih kolom untuk divisualisasikan
    option = st.selectbox('Pilih kolom: ', list(column_names.values()))
    # Mengambil nama kolom asli berdasarkan nama yang ditampilkan
    selected_column = [key for key, value in column_names.items() if value == option][0]
    # Hitung frekuensi masing-masing kategori
    value_counts = df[selected_column].value_counts()
    # Buat bar plot
    fig = plt.figure(figsize=(10, 6))
    sns.barplot(x=value_counts.index, y=value_counts.values)
    plt.xlabel(option)
    plt.ylabel('Frequency')
    plt.title('Bar Plot of ' + option)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # VISUALISASI 2
    # Menambahkan penjelasan untuk visualisasi
    st.write('### Plotly plot - Hubungan antara Usia dan BMI')
    st.write('Visualisasi ini menampilkan hubungan antara Usia dan Indeks Massa Tubuh (BMI), dengan informasi tambahan tentang gender, riwayat merokok, kadar gula darah, dan status diabetes saat mengarahkan kursor ke titik plot.')
    # Membuat plotly plot
    fig = px.scatter(df, x='age', y='bmi', hover_data=['gender', 'smoking_history', 'bmi', 'blood_glucose_level', 'diabetes'])
    st.plotly_chart(fig)
    st.write('Dari scatterplot terlihat bahwa sebagian besar orang memiliki BMI > 25 yang menunjukkan kelebihan berat badan dan masih banyak juga yang memiliki BMI > 30 sehingga termasuk obesitas. Dimana hal tersebut menandakan ukuran lemak tubuh diatas ambang normal dan dapat menyebabkan berbagai penyakit termasuk diabetes.')


    # VISUALISASI 3
    # Filter hanya penderita diabetes
    df_diabetes = df[df['diabetes'] == 1]
    # Hitung proporsi hipertensi pada penderita diabetes
    hypertension_counts_diabetes = df_diabetes['hypertension'].value_counts()
    # Membuat pie chart interaktif
    st.write('## Proporsi Hipertensi pada Penderita Diabetes')
    # Deskripsi Visualisasi
    st.write('Visualisasi ini menampilkan proporsi penderita diabetes yang memiliki riwayat penyakit hipertensi.')
    st.write('Keterangan:\n'
         '0 = Tidak Hipertensi,\n'
         '1 = Hipertensi')
    # membuat pie chart
    fig_hypertension_diabetes = px.pie(values=hypertension_counts_diabetes.values, 
                                    names=hypertension_counts_diabetes.index, 
                                    labels={0: 'Tanpa Hipertensi', 1: 'Hipertensi'})
    st.plotly_chart(fig_hypertension_diabetes)
    # Deskripsi Informasi visualisasi
    st.write('Pada penderita diabetes, hanya 24,6% yang menderita hipertensi. Meskipun hipertensi seringkali menjadi faktor risiko yang terkait dengan diabetes, hanya sebagian kecil dari penderita diabetes yang juga menderita hipertensi. Ini menunjukkan bahwa tidak semua penderita diabetes memiliki hipertensi, meskipun hubungan keduanya cukup erat.')

    # VISUALISASI 4
    # Hitung proporsi diabetes berdasarkan jenis kelamin
    diabetes_counts_gender = df['gender'].groupby(df['diabetes']).value_counts().unstack()

    # Membuat bar chart interaktif
    st.write('## Hubungan Gender dengan Diabetes')
    st.write('Visualisasi bar chart ini menunjukkan proporsi penyakit diabetes berdasarkan jenis kelamin.')
    fig_gender_diabetes = px.bar(diabetes_counts_gender, 
                                x=diabetes_counts_gender.index, 
                                y=['Male', 'Female'], 
                                labels={'diabetes': 'Diabetes', 'value': 'Jumlah Individu'},
                                title='Jumlah Individu Diabetes Berdasarkan Jenis Kelamin',
                                barmode='group')
    st.plotly_chart(fig_gender_diabetes)
    # informasi visualisasi
    st.write('Data menunjukkan bahwa jumlah perempuan yang menderita diabetes lebih tinggi daripada jumlah laki-laki yang menderita yaitu 4461 wanita dibandingkan 4039 laki-laki. Hal ini mengindikasikan bahwa faktor-faktor tertentu yang mungkin lebih umum di antara perempuan dapat meningkatkan risiko terkena diabetes.')

    # VISUALISASI 5
    # Membuat scatter plot interaktif
    st.write('## Hubungan BMI dan Blood Glucose Level')
    st.write('Visualisasi ini menunjukkan scatter hubungan BMI dengan level gula darah serta dibedakan warnanya antara diabetes dan tidak diabetes')
    fig_bmi_glucose = px.scatter(df, 
                                x='bmi', 
                                y='blood_glucose_level', 
                                color='diabetes', 
                                hover_data=['gender'],
                                labels={'bmi': 'BMI', 'blood_glucose_level': 'Blood Glucose Level', 'diabetes': 'Diabetes'})
    st.plotly_chart(fig_bmi_glucose)
    # informasi visualisasi
    st.write('Hubungan antara tingkat glukosa darah dan diabetes cukup kuat, di mana semakin tinggi tingkat glukosa darah, semakin tinggi pula risiko terkena diabetes. Selain itu, data menunjukkan bahwa bahkan pada BMI rendah, terdapat frekuensi cukup tinggi pada individu yang memiliki tingkat glukosa darah tinggi. Hal tersebut menunjukkan kompleksitas faktor risiko yang terlibat dalam diabetes.')

    # VISUALISASI 6
    st.write('## Distribusi Heart Disease pada Penderita Diabetes')
    # Deskripsi Visualisasi
    st.write('Visualisasi ini menampilkan proporsi penderita diabetes yang memiliki riwayat penyakit jantung.')
    st.write('Keterangan:\n'
         '0 = Tidak Penyakit Jantung,\n'
         '1 = Penyakit Jantung')
    # Mengelompokkan data berdasarkan diabetes dan heart disease
    heart_disease_diabetes = df[df['diabetes'] == 1]['heart_disease'].value_counts()
    # Membuat pie chart
    fig_pie_chart = px.pie(values=heart_disease_diabetes.values, 
                        names=heart_disease_diabetes.index, 
                        labels={'0': 'Tidak memiliki Heart Disease', '1': 'Memiliki Heart Disease'}, 
                        title='Distribusi Heart Disease pada Penderita Diabetes')
    st.plotly_chart(fig_pie_chart)
    # informasi visualisasi
    st.write('Mirip dengan hasil hubungan antara hipertensi dan diabetes. Meskipun penyakit jantung dan diabetes memiliki korelasi, data menunjukkan bahwa proporsi penderita diabetes yang juga memiliki riwayat penyakit jantung relatif kecil. Ini menunjukkan bahwa meskipun keduanya berhubungan dengan faktor risiko yang serupa, tidak semua penderita diabetes juga memiliki riwayat penyakit jantung.')

    # VISUALISASI 7
    # Judul visualisasi
    st.write('## Interaksi antara Age dan Diabetes')
    # Deskripsi visualisasi
    st.write('Visualisasi ini menampilkan scatterplot rentang usia dimana titik tersebut diberi warna. Warna kuning menunjukkan diabetes dan ungu menunjukkan tidak diabetes')
    # Membuat scatter plot interaktif
    fig_interaksi = px.scatter(df, 
                                x='age', 
                                color='diabetes', 
                                labels={'age': 'Age', 'diabetes': 'Diabetes'},
                                title='Interaksi antara Age dan Diabetes',
                                color_continuous_scale=px.colors.sequential.Viridis)
    st.plotly_chart(fig_interaksi)
    # informasi visualisasi
    st.write('Terdapat tren yang jelas bahwa risiko diabetes meningkat seiring bertambahnya usia. Ini menunjukkan pentingnya pemantauan kesehatan dan pencegahan terhadap diabetes, terutama pada kelompok usia yang lebih tua.')

    # membuat garis pemisah
    st.markdown('---')

    # membuat kesimpulan dari EDA
    st.write('**KESIMPULAN**')
    st.write('_Diabetes merupakan kondisi kompleks yang dipengaruhi oleh berbagai faktor seperti glukosa darah, hipertensi, penyakit jantung, usia, dan jenis kelamin, menunjukkan perbedaan prevalensi antara laki-laki dan perempuan, serta peningkatan risiko dengan bertambahnya usia. Oleh karena itu, pentingnya pendekatan holistik dalam pencegahan dan pengelolaan diabetes, termasuk pengawasan terhadap kadar glukosa darah, kontrol tekanan darah, pemeriksaan penyakit jantung, serta penerapan gaya hidup sehat yang meliputi pola makan seimbang dan aktivitas fisik secara teratur, terutama pada populasi yang rentan seperti usia lanjut dan individu dengan riwayat keluarga._')

    # membuat garis pemisah
    st.markdown('---')

    # Kalimat penutup
    st.write('***SALAM SEHAT SELALU ~***')

# untuk running
if __name__ == '__main__':
    run()
