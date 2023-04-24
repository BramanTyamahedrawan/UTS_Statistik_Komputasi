import pandas as pd

# membaca file CSV
data = pd.read_csv('E:/Program/Python/uts-statistik/pop1.csv')

# menghitung jumlah total data
total = data.shape[0]

# menghitung jumlah data "MALE"
male_count = data[data['sex'] == 'MALE'].shape[0]

# menghitung jumlah data "FEMALE"
female_count = data[data['sex'] == 'FEMALE'].shape[0]

# menghitung peluang "MALE"
male_prob = male_count / total

# menghitung peluang "FEMALE"
female_prob = female_count / total

print("Peluang MALE: {:.6}".format(male_prob))
print("Peluang FEMALE: {:.6f}".format(female_prob))
