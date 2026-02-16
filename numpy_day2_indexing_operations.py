import numpy as np

# 1D array
arr = np.array([10, 20, 30, 40, 50])

print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing
print("First three elements:", arr[:3])
print("Last two elements:", arr[3:])

# 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("Element at row 1 col 2:", arr2[0, 1])

# Row slicing
print("First row:", arr2[0])
print("Second column:", arr2[:, 1])

# Mathematical operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Square:", a ** 2)

# Broadcasting
print("Add 5 to each element:", a + 5)
