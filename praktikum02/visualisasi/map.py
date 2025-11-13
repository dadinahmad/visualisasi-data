import streamlit as st
import pandas as pd
import numpy as np

st.title("MAP")

st.write("KELOMPOK 22")
st.markdown("""
Nama Anggota :

Dadin Ahmad Jamaludin - 0110222111

Dea Amnesty - 0110122209

Muhammad Maulana - 0110221114
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)