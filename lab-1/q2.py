# using for loops

print("question 2")
list_1 = [-1, 2, 3, 9, 0]
list_2 = [1, 2, 7, 10, 14]
added_list = []
for i in range (0, len(list_1)):
    added_list.append(list_1[i] + list_2[i])
print(added_list)