# sorting_examples.py

# -------------------- 1. Sorting a Dictionary in Multiple Ways -------------------- #
def sort_dict_variants(input_dict):
    # Sorting dictionary keys
    sorted_keys = sorted(input_dict.keys())  # Output: ['a', 'b', 'c']

    # Sorting dictionary values
    sorted_values = sorted(input_dict.values())  # Output: [1, 2, 3]

    # Sorting dictionary items (key-value pairs) by keys
    sorted_items_by_key = sorted(input_dict.items(), key=lambda x: x[0])
    # Output: [('a', 2), ('b', 3), ('c', 1)]

    # Sorting dictionary items (key-value pairs) by values
    sorted_items_by_value = sorted(input_dict.items(), key=lambda x: x[1])
    # Output: [('c', 1), ('a', 2), ('b', 3)]

    return {
        "sorted_keys": sorted_keys,
        "sorted_values": sorted_values,
        "sorted_items_by_key": sorted_items_by_key,
        "sorted_items_by_value": sorted_items_by_value,
    }


# Example dictionary
input_dict = {'b': 3, 'a': 2, 'c': 1}
result = sort_dict_variants(input_dict)
print("Sorted dictionary variants:")
print(result)

# -------------------- 2. Sorting Lists -------------------- #
# Sorting a list in descending order
xa = ["p", "a"]
xa.sort(reverse=True)
print("\nList sorted in reverse order:", xa)  # Output: ['p', 'a']

# -------------------- 3. Sorting Strings by Length -------------------- #
words = ["cat", "elephant", "giraffe", "lion"]
sorted_words = sorted(words, key=len)
print("\nStrings sorted by length:", sorted_words)
# Output: ['cat', 'lion', 'giraffe', 'elephant']

# -------------------- 4. Sorting Numbers with a Custom Key -------------------- #
num_list = [1, 5, 2, 1, 1]

# Sorting in reverse order
sorted_desc = sorted(num_list, reverse=True)
print("\nNumbers sorted in descending order:", sorted_desc)  # Output: [5, 2, 1, 1, 1]

# Sorting with a custom key (if > 1, keep original; otherwise, set to 0)
sorted_custom = sorted(num_list, key=lambda x: x if x > 1 else 0)
print("Numbers sorted with a custom key:", sorted_custom)
# Output: [1, 1, 1, 2, 5]

# -------------------- 5. Sorting Tuples by a Specific Element -------------------- #
tuple_list = [(1, 3), (7, 1), (1, 2)]

# Sort by the second element in each tuple
sorted_tuples = sorted(tuple_list, key=lambda x: x[1])
print("\nTuples sorted by the second element:", sorted_tuples)
# Output: [(7, 1), (1, 2), (1, 3)]

# -------------------- Additional Examples -------------------- #
# 6. Sorting Strings Alphabetically and Reverse Alphabetically
strings = ["banana", "apple", "cherry"]
sorted_strings = sorted(strings)
sorted_strings_reverse = sorted(strings, reverse=True)
print("\nStrings sorted alphabetically:", sorted_strings)  # Output: ['apple', 'banana', 'cherry']
print("Strings sorted reverse alphabetically:", sorted_strings_reverse)  # Output: ['cherry', 'banana', 'apple']

# 7. Sorting Nested Lists by Specific Index
nested_list = [[1, 4], [2, 3], [3, 2], [4, 1]]
sorted_nested = sorted(nested_list, key=lambda x: x[1])
print("\nNested lists sorted by the second element:", sorted_nested)
# Output: [[4, 1], [3, 2], [2, 3], [1, 4]]

# 8. Sorting Dictionaries by Key or Value Directly
sorted_dict_by_key = dict(sorted(input_dict.items(), key=lambda x: x[0]))
sorted_dict_by_value = dict(sorted(input_dict.items(), key=lambda x: x[1]))
print("\nDictionary sorted by keys:", sorted_dict_by_key)  # Output: {'a': 2, 'b': 3, 'c': 1}
print("Dictionary sorted by values:", sorted_dict_by_value)  # Output: {'c': 1, 'a': 2, 'b': 3}

# 9. Using `sorted()` on a Range
sorted_range = sorted(range(10), key=lambda x: x % 3)
print("\nRange sorted by modulus 3:", sorted_range)
# Output: [0, 3, 6, 9, 1, 4, 7, 2, 5, 8]
