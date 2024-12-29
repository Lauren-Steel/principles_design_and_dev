#Import Statements
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler   #q8 & q9
from sklearn.decomposition import PCA              #q8 & q9
from sklearn.manifold import TSNE                  #q8 & q9

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