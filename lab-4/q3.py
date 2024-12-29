import matplotlib.pyplot as plt
import pandas as pd

# Question 3
dataset = pd.read_csv('lab-4/heart.csv')
data = dataset.iloc[1:1026, 0:12]
labels = dataset.iloc[0, 0:12]

fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20,10))

for i in range(0, 12):
   ax.flatten()[i].hist(data.iloc[:,i])
   ax.flatten()[i].set_title(data.columns[i], fontsize=15)

fig.tight_layout()
plt.show()