import streamlit as st

st.write("KELOMPOK 22")
st.markdown("""
Nama Anggota :

- Dadin Ahmad Jamaludin - 0110222111
- Dea Amnesty - 0110122209
- Muhammad Maulana - 0110221114
""")

st.set_page_config(page_title="Main Page")

st.title("Main Page")
st.write("Selamat datang di aplikasi multipage Streamlit dengan navigasi manual!")

# Navigasi antar halaman
st.page_link("main_page.py", label="Main Page")
st.page_link("pages/page2.py", label="Page 2")
st.page_link("pages/page3.py", label="Page 3")

st.markdown("""
Gunakan tautan di atas untuk berpindah antar halaman.
""")
