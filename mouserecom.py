from sqlite3 import DatabaseError
from turtle import color
from matplotlib.backends.backend_agg import RendererAgg
from regex import D
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import pylab as pl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import shuffle
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.model_selection import cross_val_score, GridSearchCV

#TITLE
st.title('Sistem Rekomendasi Mouse Gaming Berdasarkan Profil Pengguna')

#HEADER
st.header("Dashboard Rekomendasi Mouse")

#WRITE
st.write("Memuat Dataset")
Data = pd.read_csv(r"C:\Users\USER\Documents\mousetypeset1.csv")

# CHECKBOX
show_Data = st.checkbox("Tampilkan Dataset")
if show_Data:
    st.write(Data)

st.subheader('Price')
st.write("Harga mouse < 50 termasuk kelas low budget, 50 < 100 termasuk kelas mid budget dan > 100 tergolong kelas high budget atau kelas enthusiast. Semua harga dalam dollar.")

st.subheader('Design')
st.write("Design mouse terdiri dari dua bagian yakni ambidextrous dan ergonomic. Secara kuantitas mouse ambidextrous lebih banyak ditemui daripada ergonomic. ")
cnt_pro = Data['Design'].value_counts()
fig2 = px.bar(cnt_pro, color=['Ambidextrous', 'Ergonomic'], labels={'index':'Design', 'value':'Number of Data'})
st.plotly_chart(fig2, use_container_width=False)

st.subheader('Size')
st.write("Ukuran mouse menyesuaikan ukuran tangan pengguna. Ukuran XL = > 19 cm, L = > 18 cm, M = 18 cm, S = < 18 cm, XS = < 17 cm.")
cnt_pro = Data['Size'].value_counts()
fig3 = px.bar(cnt_pro, color=['L','M','S','XL','XS'], labels={'index':'Size', 'value':'Number of Data'})
st.plotly_chart(fig3, use_container_width=False)

st.subheader('Grip')
st.write("""
Cara memegang mouse memengaruhi kenyamanan saat menggunakan mouse. Grip yang paling populer, yakni palm dengan kontak paling banyak dengan mouse, biasanya untuk mouse ukuran besar dan berat. 
Berikutnya, claw merupakan cara memegang mouse dengan lebih sedikit kontak, biasanya untuk mouse ukuran sedang. 
Dan terakhir, fingertip dengan kontak yang paling sedikit dengan mouse hanya pada ujung jari saja, biasanya untuk mouse ukuran kecil dan ringan.""")  

cnt_pro = Data['Grip_Style'].value_counts()
fig4 = px.bar(cnt_pro, color=['Palm','Claw','Claw','Fingertip'], labels={'index':'Grip', 'value':'Number of Data'})
st.plotly_chart(fig4, use_container_width=False)

st.subheader('Rekomendasi berdasarkan profil pengguna')

name = st.text_input("Enter Your Design", "Type here")
name1 = st.text_input("Enter Your Size", "Type here")
name2 = st.text_input("Enter Your Grip", "Type here")

if(st.button('Submit')):
	result = name.title(),name1.title(),name2.title()
	st.success(result)

def recommend_mouse(x):
    y = Data[["Model","Size","Design","Grip_Style"]][Data["Design" "Size" and "Grip_Style"] == x]
    y = y.sort_values(by="Model",ascending=False)
    return y.head(1)

recommend_mouse("Ambidextrous" "S" and "Fingertip")

st.success("That's Your Mouse Recommender")
