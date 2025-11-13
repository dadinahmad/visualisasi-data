import streamlit as st
from PIL import Image

st.write("KELOMPOK 22")
st.markdown("""
Nama Anggota :

- Dadin Ahmad Jamaludin - 0110222111
- Dea Amnesty - 0110122209
- Muhammad Maulana - 0110221114
""")

img = Image.open("C:/Users/Solit/Documents/SEMESTER7/visdat/praktikum01/assets/harimau.jpg")
st.title("Padding")
# Defining Padding with columns
col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)