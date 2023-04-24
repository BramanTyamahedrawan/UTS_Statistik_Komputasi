import pandas as pd

# membaca file CSV
data = pd.read_csv('E:/Program/Python/uts-statistik/pop1.csv')

# menghitung nilai z-score
mean = 170.035
std = 11.231990696221219
tinggi = 175
z_score = (tinggi - mean) / std

print(
    "Nilai z-score untuk orang dengan tinggi hingga 175cm: {:.2f}".format(z_score))
