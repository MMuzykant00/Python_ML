
import pandas as pd

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie plików z walutami
df = pd.read_csv("wykresik2.csv", delimiter=';', decimal='.', encoding='latin1')


 #usuwanie pustych wartości
df2 = df.dropna(how='all')




df2['CAD/JEN'] = df2['CAD/JEN'].str.replace(',', '.')
df2['CAD/EURO'] = df2['CAD/EURO'].str.replace(',', '.')

df2['PSZENICA'] = df2['PSZENICA'].str.replace(',', '.')
df2['GAZ'] = df2['GAZ'].str.replace(',', '.')
df2['ROPA'] = df2['ROPA'].str.replace(',', '.')


df2['CAD/JEN'] = pd.to_numeric(df2['CAD/JEN'])

df2['CAD/EURO'] = pd.to_numeric(df2['CAD/EURO'])


df2['PSZENICA'] = pd.to_numeric(df2['PSZENICA'])

df2['GAZ'] = pd.to_numeric(df2['GAZ'])

df2['ROPA'] = pd.to_numeric(df2['ROPA'])




print(df2.describe())




sns.heatmap(df2.corr(numeric_only=True), annot=True, cmap='RdYlGn',vmin=-1, vmax=1, fmt='.2f', linewidths= 1, annot_kws=

{

'fontsize':11

} )
plt.title("Tablica korelacji")
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.show()




