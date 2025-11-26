import streamlit as st
import matplotlib.pyplot as plt

# Buat data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Des']
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

# Data sample tambahan untuk plot lainnya
product_C_sales = [18, 2, 25, 28, 32, 38, 42, 45, 48, 52, 56, 60]
product_D_sales = [7, 8, 9, 14, 23, 25, 30, 45, 50, 61, 52, 55]

# Layout Streamlit
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", 
    ("Single Line Plot",
     "Multiple & Customizations", 
     "Jenis Garis untuk Menunjukan Tren",
     "Subplot")
)

st.caption("Praktikum 3 - Matplotlib Line Chart - KELOMPOK 22")
st.markdown("""
Nama Anggota :

- Dadin Ahmad Jamaludin - 0110222111
- Dea Amnesty - 0110122209
- Muhammad Maulana - 0110221114
""")

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A')
    ax.set_title('Penjualan Produk A per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.grid(True)
    st.pyplot(fig) # Tampilkan plot

# Multiple Line Plot & Customizations
def customize_plot(): # Nama fungsi asli
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', linestyle="--", marker='o')
    ax.plot(months, product_B_sales, label='Product B', color='red', linestyle="-.", marker='x')
    
    ax.set_title('Penjualan Produk A & B per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig) # Tampilkan plot

# Jenis Garis untuk Menunjukan Tren
def tren_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_C_sales, label='Product C', color='green', linestyle="--", marker='o')
    ax.plot(months, product_D_sales, label='Product D', color='purple', linestyle="-", marker='x')
    
    ax.set_title('Penjualan Produk C & D per Bulan (Tren)')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Subplot
def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8)) 
    
    # Plot pertama untuk Product C
    axs[0].plot(months, product_C_sales, label='Product C', color='green', marker='d')
    axs[0].set_title('Penjualan Produk C per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    # Plot kedua untuk Product D
    axs[1].plot(months, product_D_sales, label='Product D', color='blue', marker='s')
    axs[1].set_title('Penjualan Produk D per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

# Logika untuk menampilkan visualisasi sesuai menu
if option == "Single Line Plot":
    line_plot()
elif option == "Multiple & Customizations":
    customize_plot()
elif option == "Jenis Garis untuk Menunjukan Tren":
    tren_line_plot()
elif option == "Subplot":
    subplots()