import pickle
import streamlit as st
import pandas as pd

def penjumlahan():
    angka1 = st.number_input("Masukkan angka pertama:", 0)
    angka2 = st.number_input("Masukkan angka kedua:", 0)
    hitung = st.button("Jumlahkan")
    
    if hitung:
        jawaban = angka1 + angka2
        st.write("Penjumlahan antara angka {:.0f} dan {:.0f} adalah: {:.0f}".format(angka1, angka2, jawaban))
        st.success("Jadi, Jawabannya adalah: {:.0f}".format(jawaban))
        st.balloons()

def pengurangan():
    angka1 = st.number_input("Masukkan angka pertama:", 0)
    angka2 = st.number_input("Masukkan angka kedua:", 0)
    hitung = st.button("Kurangkan")

    if hitung:
        jawaban = angka1 - angka2
        st.write("Pengurangan antara angka {:.0f} dan {:.0f} adalah: {:.0f}".format(angka1, angka2, jawaban))
        st.success("Jadi, Jawabannya adalah: {:.0f}".format(jawaban))
        st.balloons()

def perkalian():
    angka1 = st.number_input("Masukkan angka pertama:", 0)
    angka2 = st.number_input("Masukkan angka kedua:", 0)
    hitung = st.button("Kalikan")

    if hitung:
        jawaban = angka1 * angka2
        st.write("Perkalian antara angka {:.0f} dan {:.0f} adalah: {:.0f}".format(angka1, angka2, jawaban))
        st.success("Jadi, Jawabannya adalah: {:.0f}".format(jawaban))
        st.balloons()

def pembagian():
    angka1 = st.number_input("Masukkan angka pertama:", 0)
    angka2 = st.number_input("Masukkan angka kedua:", 0)
    hitung = st.button("Bagikan")

    if angka2 == 0:
        if hitung:
            st.write("Error!!! Tidak bisa dibagi dengan angka 0!!!")
    elif hitung:
        jawaban = angka1 / angka2
        st.write("Pembagian antara angka {:.0f} dan {:.0f} adalah: {:.0f}".format(angka1, angka2, jawaban))
        st.success("Jadi, Jawabannya adalah: {:.0f}".format(jawaban))
        st.balloons()
        
def main():
    st.title("Program Kalkulator Sederhana")
    pilihan = st.selectbox("Apa yang ingin Anda lakukan?", ("Penjumlahan", "Pengurangan", "Perkalian", "Pembagian", "Keluar"), index=0)

    if pilihan == "Penjumlahan":
        penjumlahan()
    elif pilihan == "Pengurangan":
        pengurangan()
    elif pilihan == "Perkalian":
        perkalian()
    elif pilihan == "Pembagian":
        pembagian()
    else:
        st.write("Terima kasih telah menggunakan program ini, sampai jumpa lagi :)")

if __name__ == "__main__":
    main()
