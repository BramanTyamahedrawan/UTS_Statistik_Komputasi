import pandas as pd
import scipy.stats as stats

# membaca file CSV
data = pd.read_csv('E:/Program/Python/uts-statistik/pop1.csv')

# menghitung jumlah total data
total = data.shape[0]

# menghitung jumlah data "MALE"
male_count = data[data['sex'] == 'MALE'].shape[0]

# menghitung peluang "MALE"
male_prob = male_count / total

# menghitung peluang terpilihnya 3 laki-laki dari 10 orang yang dipilih secara acak
prob_3_male = stats.hypergeom.pmf(k=3, M=total, n=10, N=male_count)

print(
    "Peluang terpilihnya 3 laki-laki dari 10 orang yang diambil secara acak: {:.19f}".format(prob_3_male))
