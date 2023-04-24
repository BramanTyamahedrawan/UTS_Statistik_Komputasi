import pandas as pd
import matplotlib.pyplot as plt

# membaca file CSV
data = pd.read_csv('E:/Program/Python/uts-statistik/pop1.csv')

# membuat histogram
plt.hist(data['height'], bins=100, color='#576CBC', alpha=0.7)

# menambahkan judul dan label pada sumbu-sumbu
plt.title("Distribusi Tinggi Badan")
plt.xlabel("Tinggi Badan (cm)")
plt.ylabel("Frekuensi")

# menampilkan histogram
plt.show()
