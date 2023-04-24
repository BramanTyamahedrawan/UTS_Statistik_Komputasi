import pandas as pd
from scipy.stats import norm

# membaca file CSV
data = pd.read_csv('E:/Program/Python/uts-statistik/pop1.csv')

# menghitung nilai z-score
mean = 170.035
std = 11.231990696221219
tinggi = 175
z_score = (tinggi - mean) / std

# menghitung peluang menggunakan fungsi distribusi normal
prob = 1 - norm.cdf(z_score)

print("Peluang memiliki tinggi > 175cm: {:.3f}".format(prob))
