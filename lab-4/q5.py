import matplotlib.pyplot as plt
import pandas as pd

# Question 5
dataset = pd.read_csv('lab-4/heart.csv')
data = dataset.iloc[1:1026, 0:12]
labels = dataset.iloc[0, 0:12]
fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20,10))
data.plot(ax=ax.flatten()[0:12], kind='box', subplots=True, sharex=False, sharey=False)

fig.tight_layout()
plt.show()