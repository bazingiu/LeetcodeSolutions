# matrix_operations.py

# -------------------- 1. Creating a Matrix -------------------- #
# Creating a 3x5 matrix where each row contains numbers from 0 to 4
matrix = [[i for i in range(5)] for j in range(3)]
print("Matrix:")
print(matrix)  # Output: [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

# Manually defining a 3x3 matrix
matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nManually defined matrix:")
print(matrix_1)

# Accessing a specific row
print("\nSecond row of the matrix:", matrix_1[1])  # Output: [4, 5, 6]

# Copying rows into a new list
risultato = [row for row in matrix_1]
print("\nCopied matrix rows:")
print(risultato)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# -------------------- 2. Accessing Elements -------------------- #
# Accessing specific elements
print("\nAccessing specific elements:")
print("Element at (1,1):", matrix_1[1][1])  # Output: 5 (row 2, column 2)
print("Element at (0,2):", matrix_1[0][2])  # Output: 3 (row 1, column 3)

# -------------------- 3. Updating Elements -------------------- #
# Updating an element in the matrix
matrix_1[2][1] = 10
print("\nMatrix after updating element at (2,1):")
print(matrix_1)  # Output: [[1, 2, 3], [4, 5, 6], [7, 10, 9]]

# -------------------- 4. Iterating Over Matrices -------------------- #
# Iterating over rows
print("\nIterating over rows:")
for row in matrix_1:
    print(row)

# Iterating over each element
print("\nIterating over each element:")
for row in matrix_1:
    for element in row:
        print(element, end=" ")
    print()

# -------------------- 5. Matrix Transposition -------------------- #
# Transpose a matrix
transposed = [[matrix_1[j][i] for j in range(len(matrix_1))] for i in range(len(matrix_1[0]))]
print("\nTransposed matrix:")
print(transposed)  # Output: [[1, 4, 7], [2, 5, 10], [3, 6, 9]]

# -------------------- 6. Matrix Operations -------------------- #
# Adding two matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

sum_matrix = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
print("\nSum of two matrices:")
print(sum_matrix)  # Output: [[10, 10, 10], [10, 10, 10], [10, 10, 10]]

# -------------------- 7. Identity Matrix -------------------- #
# Create an identity matrix of size n
def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

identity = identity_matrix(3)
print("\nIdentity matrix (3x3):")
print(identity)

# -------------------- 8. Flattening a Matrix -------------------- #
# Convert a 2D matrix into a 1D list
flattened = [element for row in matrix_1 for element in row]
print("\nFlattened matrix:")
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 10, 9]

# -------------------- 9. Checking Dimensions -------------------- #
# Get the number of rows and columns
rows = len(matrix_1)
cols = len(matrix_1[0])
print("\nMatrix dimensions:")
print(f"Rows: {rows}, Columns: {cols}")  # Output: Rows: 3, Columns: 3

# -------------------- 10. Advanced Matrix Operations -------------------- #
# Scalar multiplication
scalar = 2
scalar_multiplied = [[scalar * element for element in row] for row in matrix_1]
print("\nMatrix after scalar multiplication by 2:")
print(scalar_multiplied)

# Matrix multiplication
def matrix_multiply(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])

    if cols_a != rows_b:
        raise ValueError("Incompatible matrices for multiplication")

    result = [[sum(a[i][k] * b[k][j] for k in range(cols_a)) for j in range(cols_b)] for i in range(rows_a)]
    return result

matrix_c = [
    [1, 2],
    [3, 4],
    [5, 6]
]
matrix_d = [
    [7, 8],
    [9, 10]
]

product = matrix_multiply(matrix_c, matrix_d)
print("\nMatrix multiplication result:")
print(product)  # Output: [[25, 28], [57, 64], [89, 100]]

# -------------------- Additional Notes -------------------- #
# - Matrices in Python are represented as nested lists.
# - Libraries like NumPy offer better performance and more functionality for matrix operations.
# - Always ensure consistent dimensions for operations like addition and multiplication.
