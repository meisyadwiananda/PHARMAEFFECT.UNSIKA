import streamlit as st
import pandas as pd
import time

# Membaca dataset
file_path = "PHARMAEFFECT.csv"
df = pd.read_csv(file_path)

# Fungsi untuk menentukan keterangan efektivitas
def kategori_efektivitas(skor):
    if skor <= 1.0:
        return "Tidak efektif"
    elif 1.1 <= skor <= 2.0:
        return "Kurang efektif"
    elif 2.1 <= skor <= 3.0:
        return "Cukup efektif"
    elif 3.1 <= skor <= 4.0:
        return "Efektif"
    elif 4.1 <= skor <= 5.0:
        return "Sangat efektif"

# Menambahkan kolom kategori efektivitas
df["Keterangan Efektivitas"] = df["Efektivitas Obat (1.0-4.8)"].apply(kategori_efektivitas)

# UI Streamlit dengan tampilan lebih menarik
st.set_page_config(page_title="PHARMAEFFECT", page_icon="💊", layout="wide")

# Header dengan animasi loading
st.markdown("""
    <style>
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .fade-in {
            animation: fadeIn 2s;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            color: #2E86C1;
        }
    </style>
    <div class='fade-in title'>💊 PHARMAEFFECT 💊</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Search bar untuk mencari gejala
search_query = st.text_input("🔍 Masukkan gejala yang ingin dicari:", placeholder="Contoh: Batuk, Demam, Sakit kepala")

if search_query:
    with st.spinner("Mencari data..."):
        time.sleep(1)  # Efek loading
        hasil = df[df["Gejala"].str.contains(search_query, case=False, na=False)]
        
        if not hasil.empty:
            for _, row in hasil.iterrows():
                with st.expander(f"🔹 {row['Gejala']}"):
                    st.write(f"**🦠 Penyakit:** {row['Penyakit']}")
                    st.write(f"**💊 Obat yang Direkomendasikan:** {row['Obat yang Direkomendasikan']}")
                    st.write(f"**📊 Efektivitas Obat:** {row['Efektivitas Obat (1.0-4.8)']} ({row['Keterangan Efektivitas']})")
        else:
            st.warning("⚠️ Tidak ada hasil yang ditemukan.")

# Footer
st.markdown("""
    <br>
    <p style='text-align: center; color: gray;'>
        Dibuat dengan ❤️ oleh Kelompok 6B Farmasi 2022 UNSIKA
    </p>
""", unsafe_allow_html=True)
