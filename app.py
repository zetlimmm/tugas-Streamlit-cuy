
import streamlit as st
import pandas as pd
import numpy as np
import requests

# Menambahkan elemen navigasi dengan dropdown di Sidebar
st.sidebar.header("Navigasi")
selection = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Tentang", "Galeri", "Kontak"])

# Konten berdasarkan pilihan
if selection == "Beranda":
    st.title("Beranda")
    st.write("Ini adalah halaman beranda.")
elif selection == "Tentang":
    st.title("Tentang")
    st.write("Ini adalah halaman tentang.")
elif selection == "Galeri":
    st.title("Galeri")
    st.write("Ini adalah halaman galeri.")
else:
    st.title("Kontak")
    st.write("Ini adalah halaman kontak.")

# 1 ELEMEN TEXT
st.title("Aplikasiku Ces" )
st.video("https://www.youtube.com/watch?v=VqLdt2LkW64&pp=ygUOdGltb3RoeSByb25hbGQ%3D")
st.header("Bitcoin to the Moon")
st.subheader("Saya :")
st.caption("NAMA = NUR ALIM")
st.caption("NIM = 240907501030")
st.caption("KELAS = B / 24")
st.code("import string as ammo")
st.text("Rumus :")
st.latex('einstein  ' r'E=mc²')
st.latex('Satoshi  ' r'1 BTC = 1 BTC')
st.divider()
st.markdown(" Ini Bagian Markdown")

# 2 DATAFRAME INPUT
# 2.1 API 
st.subheader("Lembar Kerja Belajar API")
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df)
else:
    print(f"Error: {response.status_code}")
    st.error("gagalki di fetch datanya dari API")

st.subheader("Lembar Kerja Belajar Upload CSV")

# 2.2 CSV UPLOAD FILE
uploaded_file = st.file_uploader("Upload a CSV file", type=("csv"))
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
else:
    st.write("Ndd file ta upload")

# 2.3 Simple Data
st.subheader("Lembar Kerja Belajar Simple Data")
data = {
    'Name': ['Lim', 'Pati', 'pazel'],
    'Age': [18, 20, 19],
    'City': ['Sinjai', 'Batua Raya', 'Ablam']
}

df = pd.DataFrame(data)
st.dataframe(df)

st.subheader("Price Market")
# 3 Metrix Streamlit
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("BTC", "$96k", "0,2%")

with col2:
    st.metric("XAU", "$3k", "0.1%")

with col3:
    st.metric("SOL", "$148", "0.1%")

# 4 CHARTS
## 4.1 LINE CHART

st.subheader("Chart")
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
)

## 4.3 Map Chart
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(df)

# 5 INPUT FORM
st.subheader("Form Input")
with st.form("my_form"):
    name = st.text_input("Name", placeholder="Kasih masuk nama ta")
    alamat = st.text_area("Alamat", placeholder="Kasih masuk alamat ta")
    usia = st.slider("Usia", 0, 100, 25)
    tanggal_lahir = st.date_input("Tanggal Lahir")
    warna_favorit = st.color_picker("Warna Kesukaan ta")
    foto_kamera = st.camera_input("Foto Kamera")
    rating = st.slider("Rating", 1, 5, 3)
    jenis_kelamin = st.radio("Jenis Kelamin", ["cwk", "cwk"])
    hobi = st.multiselect("Hobi", ["Membantu Sesama", "Pabusur", "Mencuri"])
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Name: {name}")
        st.write(f"Alamat: {alamat}")
        st.write(f"Usia: {usia}")
        st.write(f"Tanggal Lahir: {tanggal_lahir}")

if submitted:
    st.success("Form submitted!")