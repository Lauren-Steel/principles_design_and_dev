# ELEC 390 Lab 04
# Lauren Steel (20218337)
# Saman Saeidi (20217992)
# Nicholas Seegobin (20246787)
# Zeerak Asim (20237955)

#Import Statements
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler   #q8 & q9
from sklearn.decomposition import PCA              #q8 & q9
from sklearn.manifold import TSNE                  #q8 & q9

# Question 1
dataset = pd.read_csv('lab-4/heart.csv')
data = dataset.iloc[1:1026, 0:12]
labels = dataset.iloc[0, 0:12]

fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20,10))
data.hist(ax=ax.flatten()[0:12])

fig.tight_layout()
plt.show()

# Question 2 answered on word document.

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

# Question 4
dataset = pd.read_csv('lab-4/heart.csv')
data = dataset.iloc[1:1026, 0:12]
labels = dataset.iloc[0, 0:12]
fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20,10))

data.plot(ax=ax.flatten()[0:12], kind='density', subplots=True, sharex=False)

fig.tight_layout()
plt.show()

# Question 5
dataset = pd.read_csv('lab-4/heart.csv')
data = dataset.iloc[1:1026, 0:12]
labels = dataset.iloc[0, 0:12]
fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20,10))
data.plot(ax=ax.flatten()[0:12], kind='box', subplots=True, sharex=False, sharey=False)

fig.tight_layout()
plt.show()

#Question 6
dataset = pd.read_csv('lab-4/heart.csv')
data = dataset.iloc[:, :-1]
labels = dataset.iloc[:, -1]
fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20,10))
fig, ax = plt.subplots(ncols=13, nrows=13, figsize=(30,30))

pd.plotting.scatter_matrix(data, ax=ax)
fig.tight_layout()
plt.show()

# Question 7 answered on word document.

# Question 8
dataset = pd.read_csv("lab-4/winequalityN.csv")
sc = StandardScaler()

for i in range(len(dataset['quality'])):
    if dataset["quality"][i] <= 7:
        dataset["quality"][i] = 0
    else:
        dataset["quality"][i] = 1
data = dataset.iloc[:, 1:]
labels = dataset.iloc[:, -1]
datasne = data

data = sc.fit_transform(data)
datasne = sc.fit_transform(datasne)

pca_c = PCA(n_components= 2)
data = pca_c.fit_transform(data)
tsne_ = TSNE(n_components= 2, perplexity= 30, learning_rate="auto", init='pca')
datasne = tsne_.fit_transform(datasne)

fig, ax = plt.subplots(figsize=(10, 10))
fig_tsne, ax_tsne = plt.subplots(figsize=(10, 10))
colors = ['pink', 'red']
legend = ['Low-Quality', 'Quality']

for i in range(len(legend)):
    ax.scatter(data[labels == i, 0], data[labels == i, 1], c=colors[i], s=60)
    ax_tsne.scatter(datasne[labels == i, 0], datasne[labels == i, 1], c=colors[i], s=60)

ax.set_xlabel('Principal Component - 1', fontsize=14)
ax.set_ylabel('Principal Component - 2', fontsize=14)
ax.set_title('PCA Wine Quality', fontsize=18)
ax.legend(legend, fontsize=14)

ax_tsne.set_title('t-SNE Wine Quality', fontsize=18)
ax_tsne.legend(legend, fontsize=14)
plt.show()

# Question 9
dataset = pd.read_csv("lab-4/winequalityN.csv")
sc = StandardScaler()

for i in range (len(dataset['quality'])):
    if dataset["quality"][i]<=7:
        dataset["quality"][i]=0
    else:
        dataset["quality"][i]=1
data = dataset.iloc[:, 1:-1]
labels = dataset.iloc[:, -1]

data = sc.fit_transform(data)

pca = PCA(n_components=11)
data = pca.fit_transform(data)

data = data[:, 7:9]
print(data)

fig, ax = plt.subplots(figsize=(10,10))
colors = ['pink', 'red']
legend = ['Low-Quality', 'Quality']

for i in range(len(legend)):
    ax.scatter(data[labels == i, 0], data[labels == i, 1], c=colors[i], s=60)

ax.set_xlabel('Principal Component - 8', fontsize=14)
ax.set_ylabel('Principal Component - 9', fontsize=14)
ax.set_title('PCA Wine Quality Dataset', fontsize=18)
ax.legend(legend, fontsize=14)
plt.show()

# Question 10 answered on word document.