# Using np.arange and .reshape create a 3D array

import numpy as np

print("question 4")

my_3d_array = np.arange(27).reshape(3, 3, 3)

# Image 1
print(my_3d_array[0:, 0:, 0])

# Image 2
print(my_3d_array[1, 1, 0:])

# Image 3
print(my_3d_array[0:, 0::2, 0::2])