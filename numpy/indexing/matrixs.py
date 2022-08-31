import numpy as np

# Trying to make the grid in a complected fashion to test numpy knowledge
arr =np.arange(5, 50, 5).reshape(3,3) 
print(arr)

print(arr[1, 1], arr[2][2] ) #2 different ways of accessing arrays

# Printing operation
print(arr[1:])

# New Array
newArr = np.arange(11)

# returns an array with booleans that compare each value with five it is greater than then it will be true and then vice versa
bool_arr = newArr > 5 
print(bool_arr)
print(arr[arr > 5]) # Only return values bigger than five

#Challange
arr_2d = np.arange(50).reshape(5, 10)
print(arr_2d)

# Grab [13,14,15], [23,24,25]
print(arr_2d[1:3, 3:6])
