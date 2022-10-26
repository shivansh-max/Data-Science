# Importing with an alias
import numpy as np

# Creating a basic python list and then converting it to an array
my_list = [1, 2, 3]
arr = np.array(my_list)
print(arr)

# Creating a matrix printing it then converting it to numpy matrix then printing it and telling the difference
my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_mat)
print(np.array(my_mat))

# Testing the arange function
print(np.arange(0, 10))
# adding another value will show the steps

# np fuction for zeros
print(np.zeros(10))
print(np.zeros((2, 3)))
# Ones also work like zeros

# This will make an array of 6 characters a that are evenly spaced between 0 and 5
print(np.linspace(0, 5, 6))

# Identity matrix is a square matrix
print(np.eye(4))

# This will give you a matrix with specified size and also random numbers
print(np.random.rand(2))
print(np.random.rand(2, 2))
print(np.random.randint(4, 9, (3, 5)))

# array options
arr = np.arange(25)
ranarr = np.random.randint(0, 50,10)

# Reshapes the array
arr.reshape(5,5)

# Prints max and min value, prefixing the function nave with arg will give the index
print(ranarr.max(), ranarr.min())
print(ranarr.argmax(), ranarr.argmin())

# How to get the shape of an array
print(arr.shape)

# Getting the type
print(arr.dtype)