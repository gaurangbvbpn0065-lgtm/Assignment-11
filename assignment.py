import numpy as np

# ==========================================
# 1. Combining a 1D and a 2D NumPy Array
# ==========================================

arr1 = np.array([1, 2, 3])
arr2 = np.array([[4, 5, 6],
                 [7, 8, 9]])

# Add 1D array to every row of 2D array
combined = arr2 + arr1

print("1D Array:")
print(arr1)

print("\n2D Array:")
print(arr2)

print("\nCombined Array:")
print(combined)


# ==========================================
# 2. Flatten a 2D NumPy Array into 1D Array
# ==========================================

array2d = np.array([[1, 2, 3],
                    [4, 5, 6]])

flattened = array2d.flatten()

print("\nFlattened Array:")
print(flattened)


# ==========================================
# 3. Reverse a NumPy Array
# ==========================================

arr = np.array([10, 20, 30, 40, 50])

reverse = arr[::-1]

print("\nOriginal Array:")
print(arr)

print("Reversed Array:")
print(reverse)


# ==========================================
# 4. Practice Operations
# ==========================================

arr = np.array([[5, 8, 2],
                [9, 1, 7]])

# Maximum value
print("\nMaximum Value:", np.max(arr))

# Minimum value
print("Minimum Value:", np.min(arr))

# Number of rows and columns
rows, cols = arr.shape
print("Rows:", rows)
print("Columns:", cols)

# Select each element
print("\nEach Element:")
for row in arr:
    for element in row:
        print(element, end=" ")
print()

# Select specific element
print("Specific Element (Row 2, Column 3):", arr[1, 2])

# Sum using for loop
sum_value = 0

for i in range(rows):
    for j in range(cols):
        sum_value += arr[i][j]

print("Sum using for loop:", sum_value)

# Array Operations

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# ==========================================
# 5. Iterate 3D Array using for loop and nditer
# ==========================================

array3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("\nIteration using for loops:")

for x in array3d:
    for y in x:
        for z in y:
            print(z, end=" ")
print()

print("\nIteration using nditer:")

for value in np.nditer(array3d):
    print(value, end=" ")
print()


# ==========================================
# 6. Average, Mean, Median, Mode of Two 2D Arrays
# ==========================================

arr1 = np.array([[2, 4, 6],
                 [8, 10, 12]])

arr2 = np.array([[1, 3, 5],
                 [7, 9, 11]])

# Element-wise average
average = (arr1 + arr2) / 2

print("\nArray 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

print("\nElement-wise Average:")
print(average)

# Combine both arrays into one 1D array
combined = np.concatenate((arr1.flatten(), arr2.flatten()))

# Mean
mean = np.mean(combined)

# Median
median = np.median(combined)

# Mode
values, counts = np.unique(combined, return_counts=True)
mode = values[np.argmax(counts)]

print("\nMean:", mean)
print("Median:", median)
print("Mode:", mode)