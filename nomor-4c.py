import pandas as pd
import matplotlib.pyplot as plt

# Baca data dari file CSV
data = pd.read_csv('E:/Program/Python/uts-statistik/pop1.csv')

# Hitung jumlah laki-laki
male_count = len(data[data['sex'] == 'MALE'])

# Hitung probabilitas terpilihnya n laki-laki dari 10 kali pemilihan acak


def probability_of_n_male(n):
    return (male_count/len(data))**n * ((len(data)-male_count)/len(data))**(10-n) * len(data)/2524.0


# Buat daftar probabilitas terpilihnya laki-laki dari 0 hingga 10
probabilities = [probability_of_n_male(n) for n in range(11)]

# Buat diagram batang
x_values = range(11)
plt.bar(x_values, probabilities)
plt.xlabel('Jumlah Laki-laki Terpilih')
plt.ylabel('Probabilitas')
plt.title('Distribusi Terpilihnya Laki-laki dari 10 Kali Pemilihan Acak')
plt.show()
