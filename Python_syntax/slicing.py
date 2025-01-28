# data_structures_and_loops.py

# -------------------- 1. Working with Lists -------------------- #
# Reversing a list
xa = [4, 5, 6, 2]
reversed_xa = xa[::-1]  # Reverse the entire list
print("Reversed list:", reversed_xa)  # Output: [2, 6, 5, 4]

# Skipping elements while reversing
b = xa[::-2]  # Reverse the list and take every second element
print("Reversed list with step 2:", b)  # Output: [2, 5]

# Multiplying list elements
aa = [3] * 10  # Creates a list with 10 elements, all equal to 3
print("List with repeated elements:", aa)  # Output: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

# -------------------- 2. Accessing Elements in Nested Structures -------------------- #
a = [(2, 10), (2, 5)]
print("Access element a[1][0]:", a[1][0])  # Output: 2

# -------------------- 3. Enumerating Elements in Lists -------------------- #
# Enumerate over a list of tuples
print("\nEnumerate over nested tuples:")
for i, val in enumerate(a):
    print(f"Index {i}, Value {val}")

# Enumerate over a simple list
a = [1, 2, 3, 4]
print("\nEnumerate over a simple list:")
for i, val in enumerate(a):
    print(f"Index {i}, Value {val}")

# -------------------- 4. Working with Dictionaries -------------------- #
# Accessing and modifying dictionary elements
a = {"2": 3}
a["casa"] = 3
print("\nDictionary keys:", a.keys())  # Output: dict_keys(['2', 'casa'])

# Iterating over dictionary keys
print("\nIterating over dictionary keys:")
for key in a:
    print(key)  # Output: '2', 'casa'

# Iterating over key-value pairs
print("\nIterating over dictionary items:")
for key, value in a.items():
    print(f"Key: {key}, Value: {value}")  # Output: Key-Value pairs

# -------------------- 5. List Comprehensions -------------------- #
# Creating a list using a list comprehension
c = [x for x in range(0, 10)]
print("\nList comprehension result:", c)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# -------------------- 6. Combining Lists Using zip() -------------------- #
# Combining two lists element by element
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]  # Example list for zip
print("\nZipping two lists:")
for i, val in zip(a, b):
    print(f"From list a: {i}, From list b: {val}")
# Output: 
# From list a: 1, From list b: 10
# From list a: 2, From list b: 20
# From list a: 3, From list b: 30
# From list a: 4, From list b: 40

print("Original list a:", a)  # Output: [1, 2, 3, 4]

# -------------------- Additional Examples -------------------- #
# Nested List Comprehensions
nested_comprehension = [[x * y for x in range(1, 4)] for y in range(1, 4)]
print("\nNested list comprehension result:")
print(nested_comprehension)
# Output:
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Iterating with enumerate and conditional logic
print("\nUsing enumerate with conditions:")
for i, val in enumerate(a):
    if val % 2 == 0:
        print(f"Index {i} has an even number: {val}")
# Output:
# Index 1 has an even number: 2
# Index 3 has an even number: 4

# Combining zip with enumerate
print("\nUsing zip with enumerate:")
for idx, (x_val, y_val) in enumerate(zip(a, b)):
    print(f"Index {idx}: a = {x_val}, b = {y_val}")
# Output:
# Index 0: a = 1, b = 10
# Index 1: a = 2, b = 20
# Index 2: a = 3, b = 30
# Index 3: a = 4, b = 40
