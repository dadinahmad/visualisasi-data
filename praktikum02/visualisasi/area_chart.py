import streamlit as st
import pandas as pd
import numpy as np

st.title("Area Chart")
st.write("KELOMPOK 22")
st.markdown("""
Nama Anggota :

Dadin Ahmad Jamaludin - 0110222111

Dea Amnesty - 0110122209

Muhammad Maulana - 0110221114
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.area_chart(df)