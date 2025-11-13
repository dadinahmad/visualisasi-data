import streamlit as st

st.title("COLUMN")
st.write("KELOMPOK 22")
st.markdown("""
Nama Anggota :

- Dadin Ahmad Jamaludin - 0110222111
- Dea Amnesty - 0110122209
- Muhammad Maulana - 0110221114
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("C:/Users/Solit/Documents/SEMESTER7/visdat/praktikum01/assets/harimau.jpg")
col2.write("Ini adalah kolom kedua")
col1.image("C:/Users/Solit/Documents/SEMESTER7/visdat/praktikum01/assets/harimau.jpg")