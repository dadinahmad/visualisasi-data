import streamlit as st

# text elemen
st.header("ini header")
st.subheader("ini subheader")
st.text("ini text tanpa format")
st.markdown("**ini teks bold** dan *ini tekx italic*")
st.markdown("""
- baris 1
1. baris 2
* baris 3
""")
st.caption("ini caption") #untuk penjelasan dibawah elemen
st.title("ini judul")


st.title("PRAKTIKUM 1 VISUAL DATA")
st.subheader("Bagian 1 : Teks Elemen")
st.markdown("""
Nama Anggota :

Dadin Ahmad Jamaludin

Dea Amnesty

Muhammad Maulana
""")


st.header("Displaying LaTex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''')
st.latex(r''' (a+b)^2 = a^2 + b^2 +2ab ''')


st.header("Displaying Code")
st.subheader("Python Code")
code = '''
def hello():
    print("Hello, Streamlit!)
'''
st.code(code, language='python') #menampilkan kode dengan rapih dan syntax highlighting

st.subheader("JavaScript Code")
st.code("""
    public class GFG {
        public static void main(String arg[]) {
            System.out.printIn("Hello, Streamlit);
        }
    }
""", language='java')

st.subheader("JavaScript Code")
st.code("""
<p id="demo"></p>
<script>
try {
    addalert("Welcome Guest!); // kesalahan ketik (addalert)
    sengaja untuk menimbulkan error
}
catch(err) {
    document.getElementById("demo").innerHTML = err.messege; //
    menampilkan pesan error di elemen HTML dengan id 'demo'
}
</script>
""", language="JavaSript"
)