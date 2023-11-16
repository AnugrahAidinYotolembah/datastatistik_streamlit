# -*- coding: utf-8 -*-
"""Proyek Analisis Data-notebook

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10VQ0HOWD59jglUZqj6ajRXCn12G8zGY-

# Proyek Analisis Data: Hour.csv dan Day.csv
- Nama:Moh. Abied Rabbani
- Email:abiedrabbani90@gmail.com
- Id Dicoding:Moh. Abied Rabbani

## Menentukan Pertanyaan Bisnis

- Apakah jumlah penyewaan sepeda berbeda pada hari libur dibandingkan dengan hari kerja biasa?
- Bagaimana korelasi antara kondisi cuaca dan jumlah sepeda yang disewa?

## Menyiapkan semua library yang dibutuhkan
"""

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

"""## Data Wrangling

### Gathering Data
"""

from google.colab import drive
drive.mount('/content/gdrive')

df_day = pd.read_csv('/content/gdrive/My Drive/data/Bike-sharing-dataset/day.csv')
df_hour = pd.read_csv('/content/gdrive/My Drive/data/Bike-sharing-dataset/hour.csv')

"""### Assessing Data"""

df_day.head()

df_hour.head()

df_day.info()

df_hour.info()

df_day.describe()

df_hour.describe()

df_day.isna().sum()

df_hour.isna().sum()

"""### Cleaning Data"""

df_day.drop(['dteday','instant','season','yr','mnth','weekday','workingday','weathersit','temp','atemp','hum', 'windspeed'	,'casual', 'registered'], axis=1, inplace=True)
df_hour.drop(['instant',	'dteday',	'season',	'yr',	'mnth',	'hr',	'holiday',	'weekday',	'workingday',	'temp',	'atemp',	'hum',	'windspeed',	'casual',	'registered'], axis=1, inplace=True)

df_day.head()

df_hour.head()

"""## Exploratory Data Analysis (EDA)

### Explore ...
"""

rentals_per_day_type = df_day.groupby('holiday')['cnt'].sum()
print(rentals_per_day_type)

correlation_matrix = df_hour[['weathersit', 'cnt']].corr()
print(correlation_matrix)

"""## Visualization & Explanatory Analysis

### Apakah jumlah penyewaan sepeda berbeda pada hari libur dibandingkan dengan hari kerja biasa?
"""

plt.figure(figsize=(8, 5))
sns.barplot(x=rentals_per_day_type.index, y=rentals_per_day_type.values)
plt.title('Jumlah Penyewaan Sepeda pada Hari Libur dan Hari Kerja')
plt.xlabel('Jenis Hari (0: Hari Kerja, 1: Hari Libur)')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.show()

"""### Bagaimana korelasi antara kondisi cuaca dan jumlah sepeda yang disewa?"""

corr_numerical = df_hour.corr('pearson')[['weathersit','cnt']].sort_values(by='weathersit', ascending=False)
fig, data = plt.subplots(figsize = (8,5))
sns.heatmap(corr_numerical, ax = data, annot=True)
plt.title('Korelasi antara Weathersit dan Jumlah Penyewaan Sepeda')

"""## Conclusion

- Jumlah penyewaan sepeda pada hari kerja lebih banyak dari pada hari libur
- Hasil korelasi menunjukkan adanya hubungan yang signifikan antara kondisi cuaca dan jumlah sepeda yang disewa.
"""

