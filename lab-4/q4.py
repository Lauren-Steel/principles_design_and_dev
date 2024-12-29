import matplotlib.pyplot as plt
import pandas as pd

# Question 4
dataset = pd.read_csv('heart.csv')
data = dataset.iloc[1:1026, 0:12]
labels = dataset.iloc[0, 0:12]
fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20,10))

data.plot(ax=ax.flatten()[0:12], kind='density', subplots=True, sharex=False)

fig.tight_layout()
plt.show()