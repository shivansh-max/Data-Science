import numpy as np

# making a default array
arr = np.arange(0, 11)

# specific value
print(arr[2])

# index values in range
print(arr[0:5])

# returns a everything up to index six
print(arr[:6])

# returns everything after index six
print(arr[6:])

#  changes every value in the given places to 100
arr[0:5] = 100
print(arr)

# Resetting the array
arr = np.arange(0, 11)
