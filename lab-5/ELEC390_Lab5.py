# ELEC 390 Lab 04
# Lauren Steel (20218337)
# Saman Saeidi (20217992)
# Nicholas Seegobin (20246787)
# Zeerak Asim (20237955)

#Import Statements
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
# from sklearn.manifold import TSNE

# Question 1
# Part A
dataset = pd.read_csv('lab-5/unclean-wine-quality.csv')
data = dataset.iloc[1:1026, 0:12]
labels = dataset.iloc[0, 0:12]

#Checks for any missing values in the csv file, sums up the amount of missing data with NaN's and -'s.
missing_data = data.isna().sum().sum()
print(missing_data)

# Part B
replaceDemVals = data.isna().sum()
print(replaceDemVals)
condition = dataset = "-"

dataset.mask(condition, other = np.nan, inplace = True)
dataset = dataset.astype('float64')