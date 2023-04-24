import pandas as pd
import numpy as np

# membaca file CSV
data = pd.read_csv('E:/Program/Python/uts-statistik/pop1.csv')

# menghitung nilai kuartil
q1 = np.percentile(data['height'], 25, method='midpoint')
q2 = np.percentile(data['height'], 50, method='midpoint')
q3 = np.percentile(data['height'], 75, method='midpoint')

# mencetak hasil
print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
