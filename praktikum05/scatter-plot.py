# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd

# st.title("COLUMN")
# st.write("KELOMPOK 22")
# st.markdown("""
# Nama Anggota :

# - Dadin Ahmad Jamaludin - 0110222111
# - Dea Amnesty - 0110122209
# - Muhammad Maulana - 0110221114
# """)

# # dataset utama
# suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
# penjualan = [50, 60, 70, 80, 90, 100, 130, 150, 170]

# # dataset penjualan
# penjualan_weekdays = [50, 60, 70, 80, 90, 100, 110, 120, 130]
# penjualan_weekend = [60, 70, 80, 100, 110, 120, 140, 160, 200]

# # data untuk analisis
# data = {
#     'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
#     'Penjualan_Coklat': [40, 45, 50, 55, 60, 65, 70, 75, 80],
#     'Penjualan_Vanila': [82, 80, 78, 76, 77, 80, 82, 85, 88],
#     'Penjualan_Stroberi': [55, 50, 55, 60, 65, 60, 65, 70, 72],
#     'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
# }

# # konversi ke dataframe
# df = pd.DataFrame(data)

# # layout utama
# st.title('Visualisasi Scatter Plot Penjualan Es Krim')
# st.sidebar.header("Pengaturan Visualisasi")

# # menu di sidebar
# option = st.sidebar.selectbox(
#     "Pilih contoh scatter plot",
#     (
#         "Basic Scatter Plot",
#         "Kustomisasi Scatter Plot"
#         ""
#         ""
#     )

# )

# # 1. basic scatter plot
# def basic_scatter():
#     st.subheader("1. Basic Scatter Plot")
#     fig, ax = plt.subplot()
#     ax.scatter(suhu, penjualan)
#     ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
#     ax.set_xlabel('Suhu')
#     ax.set_ylabel('Penjualan Es Krim')
#     st.pyplot(fig)

# # 2. kustomisasi scatter plot
# def custom_scatter():
#     st.subheader("2. Kustomisasi Scatter Plot")
#     fig, ax = plt.subplot()
#     ax.scatter(suhu, penjualan, color="orange", s=100, edgecolor='black', alpha=0.7)
#     ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
#     ax.set_xlabel('Suhu')
#     ax.set_ylabel('Penjualan Es Krim')
#     ax.grid(True)
#     st.pyplot(fig)

# # 3. Multiple Scatter Plot
# def multiple_scatter():
#     st.subheader("3. Multiple Scatter Plot")
#     fig, ax = plt.subplot()
#     plt.scatter(suhu, penjualan_weekdays, color='green', label='Hari Kerja', s=80)
#     ax.scatter(suhu, penjualan_weekend, color='purple', label='Akhir Pekan', s=80)
#     ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
#     ax.set_xlabel('Suhu')
#     ax.set_ylabel('Penjualan Es Krim')
#     ax.grid(True)
#     st.pyplot(fig)

# # 4. Analisis

#     st.subheader("4. Analisis Scatter Plot")
#     # opsi jenis eskrim
#     jenis_eskrim = st.selectbox('Pilih Jenis Es krim', ['Coklat', 'Vanila', 'Stroberi'])

#     if jenis_eskrim == 'Coklat':
#         penjualan = df['Penjualan_Coklat']
#     elif jenis_eskrim == 'Vanila':
#         penjualan = df['Penjualan_Vanila']
#     elif jenis_eskrim == 'Stroberi':
#         penjualan = df['Penjualan_Stroberi']
        

#     st.subheader("Data Penjualan dan Suhu")
#     st.dataframe(df)

#     # scatter plot
#     fig, ax = plt.subplots()
#     scatter = ax.scatter(df['suhu'], penjualan, c=df['Kelembapan'], s=100, cmap='coolwarm', alpha=0.7)

#     # styling
#     ax.set_title(f'Hubungan Penjualan {jenis_eskrim} vs Suhu dan Kelembapan')
#     ax.set_xlabel('Suhu')
#     ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')
#     fig.colorbar(scatter, label='Kelembapan (%)')

#     st.pyplot(fig)

#     # ringkasan hubungan
#     st.subheader('Analisis Hubungan')
#     st.write(f'Grafik Menunjukan Hubungan antara suhu, kelembapan, dan penjualan eskrim jenis **
# {jenis_eskrim}**')

# # routing berdasarkan menu sidebar
# if option == "Basic Scatter Plot":
#     basic_scatter()
# elif option == "Kustomisasi Scatter Plot"
#     custom_scatter()
# elif option == "Multiple Scatter Plot"
#     multiple_scatter()
# elif option == "Analisis Scatter Plot"
#     scatter_3_variabel()

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("COLUMN")
st.write("KELOMPOK 22")
st.markdown("""
Nama Anggota :

- Dadin Ahmad Jamaludin - 0110222111
- Dea Amnesty - 0110122209
- Muhammad Maulana - 0110221114
""")

# dataset utama
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 80, 90, 100, 130, 150, 170]

# dataset penjualan
penjualan_weekdays = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_weekend = [60, 70, 80, 100, 110, 120, 140, 160, 200]

# data untuk analisis (sudah diperbaiki menggunakan {})
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Coklat': [40, 45, 50, 55, 60, 65, 70, 75, 80],
    'Penjualan_Vanila': [82, 80, 78, 76, 77, 80, 82, 85, 88],
    'Penjualan_Stroberi': [55, 50, 55, 60, 65, 60, 65, 70, 72],
    'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
}

# konversi ke dataframe
df = pd.DataFrame(data)

# layout utama
st.title('Visualisasi Scatter Plot Penjualan Es Krim')
st.sidebar.header("Pengaturan Visualisasi")

# menu di sidebar
option = st.sidebar.selectbox(
    "Pilih contoh scatter plot",
    (
        "Basic Scatter Plot",
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis Scatter Plot"
    )

)

# 1. basic scatter plot
def basic_scatter():
    st.subheader("1. Basic Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)

# 2. kustomisasi scatter plot
def custom_scatter():
    st.subheader("2. Kustomisasi Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color="orange", s=100, edgecolor='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# 3. Multiple Scatter Plot
def multiple_scatter():
    st.subheader("3. Multiple Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color='green', label='Hari Kerja', s=80)
    ax.scatter(suhu, penjualan_weekend, color='purple', label='Akhir Pekan', s=80)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.legend() # Tambahkan legend agar label Hari Kerja/Akhir Pekan muncul
    ax.grid(True)
    st.pyplot(fig)

# 4. Analisis (Scatter Plot 3 Variabel)
def scatter_3_variabel(): # Dibungkus ke dalam fungsi yang dipanggil di routing
    st.subheader("4. Analisis Scatter Plot")
    # opsi jenis eskrim (sudah diperbaiki koma)
    jenis_eskrim = st.selectbox('Pilih Jenis Es krim', ['Coklat', 'Vanila', 'Stroberi'])

    if jenis_eskrim == 'Coklat':
        penjualan = df['Penjualan_Coklat']
    elif jenis_eskrim == 'Vanila':
        penjualan = df['Penjualan_Vanila']
    elif jenis_eskrim == 'Stroberi':
        penjualan = df['Penjualan_Stroberi']
        

    st.subheader("Data Penjualan dan Suhu")
    st.dataframe(df)

    # scatter plot
    fig, ax = plt.subplots()
    # Menggunakan df['Suhu'] (huruf besar S) karena key di dictionary 'data' menggunakan 'Suhu'
    scatter = ax.scatter(df['Suhu'], penjualan, c=df['Kelembapan'], s=100, cmap='coolwarm', alpha=0.7)

    # styling
    ax.set_title(f'Hubungan Penjualan {jenis_eskrim} vs Suhu dan Kelembapan')
    ax.set_xlabel('Suhu')
    ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')
    fig.colorbar(scatter, label='Kelembapan (%)')

    st.pyplot(fig)

    # ringkasan hubungan (sudah diperbaiki f-string)
    st.subheader('Analisis Hubungan')
    st.write(f'Grafik Menunjukan Hubungan antara suhu, kelembapan, dan penjualan eskrim jenis **{jenis_eskrim}**')

# routing berdasarkan menu sidebar (sudah diperbaiki titik dua)
if option == "Basic Scatter Plot":
    basic_scatter()
elif option == "Kustomisasi Scatter Plot": # Perbaikan: Tambahkan ':'
    custom_scatter()
elif option == "Multiple Scatter Plot": # Perbaikan: Tambahkan ':'
    multiple_scatter()
elif option == "Analisis Scatter Plot":
    scatter_3_variabel() # Perbaikan: Panggil fungsi yang sudah didefinisikan