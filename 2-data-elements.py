import streamlit as st
import pandas as pd # mengelola data dalam bentuk tabel
import numpy as np # membuat data numerik acak
import altair as alt # membuat chart interaktif
# import streamlit as st
# import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np

st.title("PRAKTIKUM 1 VISUAL DATA")
st.subheader("Bagian 1 : Teks Elemen")
st.markdown("""
Nama Anggota :
1. Dadin Ahmad Jamaludin - 0110222111
2. Dea Amnesty - 0110
3. Muhammad Maulana - 0110
""")

st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

st.dataframe(df) # menampilkan data frame

# highlight nilai minimum
st.subheader("Highlight Minimun Value di DataFrame")

# hightlight nilai terkecil disetiap kolom dataframe
# axis=0 bekerja perkolom
st.dataframe(df.style.highlight_min(axis=0))

# Tabel Statis
st.subheader("Tabel Statis")

# df = pd.DataFrame(
#     np.random.randn(30,10),
#     columns=('col_no %d' % i for i in range (10))
# )

# st.table(df)
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)

st.table(df)

# Metrics : komponen tampilan angka penting
st.subheader("Metrics")

st.metric(label="Temperature", value="31 °C", delta="1.2 °C")

# Metrics : komponen tampilan angka penting
st.subheader("Metrics")

# st.metric(label="Temperature", value="31 °C, delta="1.2 °C")

# col1, col2, col3 = st.columns(3)

# col1.metric("Curah Hujan", "100 cm", "10 cm")
# col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar"),
# delta_color="inverse")
# col3.metric(label="Pelanggan", value=100, delta=10,
# delta_color="off")

# st. metric(label="Speed", Value=None, delta=0)
# st.metric("Trees", "91456", "-1132649")

st.metric(label="Temperature", value="31 °C", delta="1.2 °C")

col1, col2, col3 = st.columns(3)

col1.metric("Curah Hujan", "100 cm", "10 cm")
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse")
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off")

st.metric(label="Speed", value="0", delta="0")
st.metric("Trees", "91456", "-1132649")


# --- Math calculations with no functions defined ---
st.write("Adding 5 & 4 =", 5 + 4)

# --- Displaying variable 'a' and its value ---
a = 5
st.write("'a' =", a)

# --- Markdown with Magic ---
st.markdown("""
### Magic Feature  
Markdown works even without explicitly defining its function.
""")

# --- DataFrame using magic ---
df = pd.DataFrame({'col': [1, 2]})
st.write("DataFrame:", df)

# --- Magic working on Charts ---
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)

# --- Display chart in Streamlit ---
st.pyplot(chart)