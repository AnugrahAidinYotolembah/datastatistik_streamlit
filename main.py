import streamlit as st
import pandas as pd
import numpy as np

# Data dummy untuk tujuan demonstrasi
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [4, 7, 1, 8, 5]
})

# Judul aplikasi
st.title('Dashboard Statistik')

# Tampilkan data statistik
st.header('Data Statistik')
st.dataframe(data)

# Tampilkan ringkasan statistik
st.subheader('Ringkasan Statistik')
st.write(data.describe())

# Tampilkan diagram batang
st.subheader('Diagram Batang')
st.bar_chart(data.set_index('Category')['Value'])

# Tampilkan diagram lingkaran
st.subheader('Diagram Lingkaran')
st.pie_chart(data.set_index('Category')['Value'])

# Tampilkan histogram
st.subheader('Histogram')
st.hist(data['Value'], bins=10, edgecolor='black')

# Tampilkan scatter plot
st.subheader('Scatter Plot')
st.scatter_chart(data)

# Tampilkan statistik tambahan
st.subheader('Statistik Tambahan')
st.write(f"Jumlah data: {len(data)}")
st.write(f"Rata-rata nilai: {np.mean(data['Value'])}")

# Footer
st.sidebar.markdown('Dibuat oleh [didi]')
