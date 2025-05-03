
import streamlit as st
import pandas as pd
import numpy as np
import requests

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
st.latex('einstein' r'E=mc²')
st.latex('Satoshi' r'1 BTC = 1 BTC')
st.divider()
st.markdown("Aplikasi Streamlit App - Ini Markdown")

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
    st.error("datanya gagal di fetch dari API")

st.subheader("Lembar Kerja Belajar Upload CSV")

# 2.2 CSV UPLOAD FILE
uploaded_file = st.file_uploader("Upload a CSV file", type=("csv"))
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
else:
    st.write("No file uploaded yet")

# 2.3 Simple Data
st.subheader("Lembar Kerja Belajar Simple Data")
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)
st.dataframe(df)

st.subheader("Lembar Kerja Belajar Simple Data 2")
# 3 Metrix Streamlit
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Temperature", "70 °F", "1.2 °F")

with col2:
    st.metric("Wind Speed", "10 mph", "-8%")

with col3:
    st.metric("Humidity", "60%", "4%")

# 4 CHARTS
## 4.1 LINE CHART

st.subheader("Lembar Kerja CHARTS")
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
st.bar_chart(chart_data, color=['#ff0000', '#00ff00', '#0000ff'])

## 4.3 Map Chart
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(df)

# 5 INPUT FORM


st.subheader("Lembar Kerja Belajar Form Input")
with st.form("my_form"):
    name = st.text_input("Name", placeholder="Enter your name")
    alamat = st.text_area("Alamat", placeholder="Enter your address")
    usia = st.slider("Usia", 0, 100, 25)
    tanggal_lahir = st.date_input("Tanggal Lahir")
    warna_favorit = st.color_picker("Warna Favorit")
    foto_kamera = st.camera_input("Foto Kamera")
    rating = st.slider("Rating", 1, 5, 3)
    jenis_kelamin = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    hobi = st.multiselect("Hobi", ["Membaca", "Menulis", "Menggambar", "Mengaji"])
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Name: {name}")
        st.write(f"Alamat: {alamat}")
        st.write(f"Usia: {usia}")
        st.write(f"Tanggal Lahir: {tanggal_lahir}")

if submitted:
    st.success("Form submitted!")

# Upload Media di Streamlit video
st.subheader("Lembar Kerja Belajar Upload Media yt")
st.video("https://www.youtube.com/watch?v=QK4BVh2aSAA")
# st.video('.video.mp4')

st.subheader("Lembar Kerja Belajar Upload Media mp3")
# st.audio('.audio.mp3')


# Menambahkan elemen navigasi di Sidebar
st.sidebar.header("Navigasi")
selection = st.sidebar.radio("Pilih Halaman", ["Beranda", "Tentang", "Kontak"])

# Konten berdasarkan pilihan
if selection == "Beranda":
    st.title("Beranda")
    st.write("Ini adalah halaman beranda.")
elif selection == "Tentang":
    st.title("Tentang")
    st.write("Ini adalah halaman tentang.")
else:
    st.title("Kontak")
    st.write("Ini adalah halaman kontak.")

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

# Menambahkan tombol untuk navigasi di Sidebar
st.sidebar.header("Navigasi")
if st.sidebar.button("Beranda"):
    st.title("Beranda")
    st.write("Ini adalah halaman beranda.")
elif st.sidebar.button("Tentang"):
    st.title("Tentang")
    st.write("Ini adalah halaman tentang.")
elif st.sidebar.button("Kontak"):
    st.title("Kontak")
    st.write("Ini adalah halaman kontak.")

# Menambahkan tautan navigasi di Sidebar
st.sidebar.header("Navigasi")
st.sidebar.markdown("[Beranda](#beranda)")
st.sidebar.markdown("[Tentang](#tentang)")
st.sidebar.markdown("[Kontak](#kontak)")

# Konten halaman berdasarkan tautan
st.title("Beranda")
st.write("Ini adalah halaman beranda.")

st.title("Tentang")
st.write("Ini adalah halaman tentang.")

st.title("Kontak")
st.write("Ini adalah halaman kontak.")  