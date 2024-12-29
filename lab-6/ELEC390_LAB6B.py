# ELEC 390 Lab 6
# Lauren Steel (20218337)
# Saman Saeidi (20217992)
# Nicholas Seegobin (20246787)
# Zeerak Asim (20237955)

# Question 2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, RocCurveDisplay
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.decomposition import PCA

# reading the dataset
dataset = pd.read_csv("winequalityN-lab6.csv")

# Convert quality column to binary classifiers
dataset['quality'] = dataset['quality'].apply(lambda x: 1 if x >= 6 else 0)

# drop the first column
dataset.drop(dataset.columns[0], axis=1, inplace=True)

# assign data and labels
data = dataset.iloc[:, :-1]
labels = dataset.iloc[:, -1]

#assigning 20% of the data to the test set
X_train, X_test, Y_train, Y_test = \
    train_test_split(data, labels, test_size=0.2, shuffle=True, random_state=0)

#defining the calssifier
StandardScaler()
l_reg = LogisticRegression(max_iter=1000)
pca = PCA(n_components=2)

pca_pipe = make_pipeline(StandardScaler(), pca)

x_train_pca = pca_pipe.fit_transform(X_train)
x_test_pca = pca_pipe.fit_transform(X_test)

clf = make_pipeline(l_reg)

clf.fit(x_train_pca, Y_train)

y_pred_pca = clf.predict(x_test_pca)

acc = accuracy_score(Y_test, y_pred_pca)

print('Accuracy is: ', acc)

disp = DecisionBoundaryDisplay.from_estimator(
    clf, x_train_pca, response_method="predict",
    xlabel='X1', ylabel='X2',
    alpha=0.5
)

disp.ax_.scatter(x_train_pca[:, 0], x_train_pca[:,1], c=Y_train)
plt.show()