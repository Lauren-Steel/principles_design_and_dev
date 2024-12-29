#Import Statements
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler   #q8 & q9
from sklearn.decomposition import PCA              #q8 & q9
from sklearn.manifold import TSNE                  #q8 & q9

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