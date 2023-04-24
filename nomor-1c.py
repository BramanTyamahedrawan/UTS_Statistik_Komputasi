import pandas as pd
import numpy as np

# membaca file CSV
data = pd.read_csv('E:/Program/Python/uts-statistik/pop1.csv')

# menghitung nilai kuartil
q1 = np.percentile(data['height'], 25, method='midpoint')
q3 = np.percentile(data['height'], 75, method='midpoint')

# menghitung IQR
iqr = q3 - q1

# menentukan batas bawah dan batas atas
batas_bawah = q1 - 1.5 * iqr
batas_atas = q3 + 1.5 * iqr

# menghitung jumlah outlier
outlier = data[(data['height'] < batas_bawah) | (data['height'] > batas_atas)]
num_outlier = len(outlier)

# mencetak hasil
if num_outlier > 0:
    print("Jumlah outlier:", num_outlier)
else:
    print("Tidak terdapat outlier pada data")
