
# ELEC 390 Lab 1
# Lauren Steel (20218337)
# Saman Saeidi (20217992)
# Nicholas Seegobin (20246787)
# Zeerak Asim (20237955)



# all questions were written as if they could be their own file
# (import numpy as np is repeated along with array set up for questions 4/5


# Question 1
list_1 = [-1, 2, 3, 9, 0]
list_2 = [1, 2, 7, 10, 14]
print(list_1 + list_2)


# Question 2
list_1 = [-1, 2, 3, 9, 0]
list_2 = [1, 2, 7, 10, 14]
added_list = []
for i in range (0, len(list_1)):
    added_list.append(list_1[i] + list_2[i])
print(added_list)


# Question 3
import numpy as np
my_4d_array = np.array([[[[1],[2]],[[3],[4]],[[5],[6]]],[[[1],[2]],[[3],[4]],[[5],[6]]]])
print(my_4d_array.shape)


# Question 4
my_3d_array = np.arange(27).reshape(3, 3, 3)

# Image 1
print(my_3d_array[0:, 0:, 0])

# Image 2
print(my_3d_array[1, 1, 0:])

# Image 3
print(my_3d_array[0:, 0::2, 0::2])



# Question 5
my_3d_array = np.arange(27).reshape(3, 3, 3)

# Image 1
print(my_3d_array[[0, 1, 2], [1, 2, 0], [1, 2, 0]])

# Image 2
print(my_3d_array[[1], [0, 2], [0, 2]])


# Question 6
my_2d_array = np.arange(-11, 19, 1).reshape(5, 6)
sum_of_col = my_2d_array.sum(axis=0)
indexing_array = (sum_of_col%10==0)
print(my_2d_array[:, indexing_array])
