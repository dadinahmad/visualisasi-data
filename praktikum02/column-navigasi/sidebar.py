import streamlit as st

st.write("KELOMPOK 22")
st.markdown("""
Nama Anggota :

- Dadin Ahmad Jamaludin - 0110222111
- Dea Amnesty - 0110122209
- Muhammad Maulana - 0110221114
""")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)