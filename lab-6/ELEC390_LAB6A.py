# ELEC 390 Lab 6
# Lauren Steel (20218337)
# Saman Saeidi (20217992)
# Nicholas Seegobin (20246787)
# Zeerak Asim (20237955)

# Question 1
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, RocCurveDisplay
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay 
from sklearn.metrics import roc_curve, roc_auc_score

# reading the dataset
dataset = pd.read_csv("winequalityN-lab6.csv")
sc = StandardScaler()

# Convert quality column to binary classifiers
dataset['quality'] = dataset['quality'].apply(lambda x: 1 if x >= 6 else 0)

# drop the first column
dataset.drop(dataset.columns[0], axis=1, inplace=True)

# assign data and labels
data = dataset.iloc[:, :-1]
labels = dataset.iloc[:, -1]

#assigning 20% of the data to the test set
X_train, X_test, Y_train, Y_test = \
    train_test_split(data, labels, test_size=0.2, shuffle=True)

#defining the calssifier
l_reg = LogisticRegression(max_iter=1000)
clf = make_pipeline(StandardScaler(), l_reg)

# training
clf.fit(X_train, Y_train)

#obtain the predictions and probabilities
y_pred = clf.predict(X_test)
y_clf_prob = clf.predict_proba(X_test)
print('y_pred is: ', y_pred)
print('y_clf_prob is:', y_clf_prob)

# find the accuracy score
accuracy = accuracy_score(Y_test, y_pred)
print("Accuracy:", accuracy)

# confusion matrix
cm = confusion_matrix(Y_test, y_pred)
cm_display = ConfusionMatrixDisplay(cm).plot()
plt.show()

# compute F1 score
TN, FP, FN, TP = confusion_matrix(Y_test, y_pred).ravel()
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1_score = 2 * (precision * recall) / (precision + recall)
print("F1 score:", f1_score)

# plotting the ROC curve
fpr, tpr, _ = roc_curve(Y_test, y_clf_prob[:, 1], pos_label=clf.classes_[1])
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
plt.show()

# calculating the AUC
auc = roc_auc_score(Y_test, y_clf_prob[:, 1])
print('the AUC is: ', auc)