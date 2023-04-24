import pandas as pd
import numpy as np

# membaca file CSV
# Menggunakan tanda forward slash
data = pd.read_csv('E:/Program/Python/uts-statistik/pop1.csv')

# menghitung nilai mean
mean_height = np.mean(data['height'])

# menghitung nilai varians
var_height = np.var(data['height'])

# menghitung nilai simpangan baku
simpangan_height = np.std(data['height'])

# mencetak hasil
print("Mean:", mean_height)
print("Varians:", var_height)
print("Simpangan Baku:", simpangan_height)
