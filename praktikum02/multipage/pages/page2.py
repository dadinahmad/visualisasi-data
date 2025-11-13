import streamlit as st

st.write("KELOMPOK 22")
st.markdown("""
Nama Anggota :

- Dadin Ahmad Jamaludin - 0110222111
- Dea Amnesty - 0110122209
- Muhammad Maulana - 0110221114
""")

st.set_page_config(page_title="Page 2")

st.title("Page 2")
st.write("Kamu sedang berada di halaman kedua.")

# Navigasi balik
st.page_link("main_page.py", label="Kembali ke Main Page")
st.page_link("pages/page3.py", label="Ke Page 3")
