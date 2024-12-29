# another 3d array

import numpy as np

print("question 5")
my_3d_array = np.arange(27).reshape(3, 3, 3)

# Image 1
print(my_3d_array[[0, 1, 2], [1, 2, 0], [1, 2, 0]])

# Image 2
print(my_3d_array[[1], [0, 2], [0, 2]])