# set_operations.py

# -------------------- 1. Creating and Adding Elements to a Set -------------------- #
# Create an empty set
x = set()

# Add elements to the set
x.add(3)
x.add('ciao')
print("Set after adding elements:", x)  # Output: {3, 'ciao'}

# -------------------- 2. Removing Elements from a Set -------------------- #
# Remove an element using remove()
x.remove(3)  # Raises KeyError if the element does not exist
print("Set after removing 3:", x)  # Output: {'ciao'}

# Remove an element using discard() (does not raise an error if the element is missing)
x.discard('nonexistent')
print("Set after discard (no error for missing element):", x)  # Output: {'ciao'}

# -------------------- 3. Checking Membership -------------------- #
print("Is 'ciao' in the set?", 'ciao' in x)  # Output: True
print("Is 3 in the set?", 3 in x)           # Output: False

# -------------------- 4. Set Operations -------------------- #
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (all unique elements from both sets)
union_set = set_a | set_b
print("Union of sets:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
intersection_set = set_a & set_b
print("Intersection of sets:", intersection_set)  # Output: {3, 4}

# Difference (elements in set_a but not in set_b)
difference_set = set_a - set_b
print("Difference of sets (A - B):", difference_set)  # Output: {1, 2}

# Symmetric Difference (elements in either set, but not both)
symmetric_difference_set = set_a ^ set_b
print("Symmetric difference of sets:", symmetric_difference_set)  # Output: {1, 2, 5, 6}

# -------------------- 5. Working with Subsets and Supersets -------------------- #
set_c = {1, 2}
set_d = {1, 2, 3, 4}

# Check if one set is a subset of another
print("Is C a subset of D?", set_c.issubset(set_d))  # Output: True

# Check if one set is a superset of another
print("Is D a superset of C?", set_d.issuperset(set_c))  # Output: True

# -------------------- 6. Creating a Set with Unique Elements -------------------- #
# Convert a list with duplicate elements to a set
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)
print("Unique elements from the list:", unique_nums)  # Output: {1, 2, 3, 4, 5}

# -------------------- 7. Set Comprehensions -------------------- #
# Create a set with square of numbers from 0 to 4
squares = {x ** 2 for x in range(5)}
print("Set of squares:", squares)  # Output: {0, 1, 4, 9, 16}

# -------------------- Additional Notes -------------------- #
# - Sets are mutable, but the elements within a set must be immutable.
# - You cannot add lists or other sets to a set directly, but you can add tuples or frozensets.
# - Sets are highly efficient for membership tests and mathematical operations.

# Example with frozensets (immutable sets)
frozen_set = frozenset([1, 2, 3])
print("Frozenset:", frozen_set)  # Output: frozenset({1, 2, 3})
