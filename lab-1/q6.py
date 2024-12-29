# creating a matrix 

import numpy as np 

print("question 6")

my_2d_array = np.arange(-11, 19, 1).reshape(5, 6)
sum_of_col = my_2d_array.sum(axis=0)
indexing_array = (sum_of_col%10==0)
print(my_2d_array[:, indexing_array])