import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('E:/Program/Python/uts-statistik/pop1.csv')

# Mengubah orientasi plot menjadi horizontal
sns.boxplot(x='height', orient='h', data=data)
plt.show()
