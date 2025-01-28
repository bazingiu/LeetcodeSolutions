# max_min_examples.py

from math import prod

# -------------------- 1. Finding the longest string -------------------- #
words = ["cat", "elephant", "giraffe", "lion"]
longest_word = max(words, key=len)
print("Longest word:", longest_word)  # Output: "elephant"

# -------------------- 2. Finding the number closest to 0 -------------------- #
numbers = [-10, -3, 7, 2, -1]
closest_to_zero = min(numbers, key=abs)
print("Number closest to zero:", closest_to_zero)  # Output: -1

# -------------------- 3. Finding the oldest person in a list of dictionaries -------------------- #
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
oldest_person = max(data, key=lambda x: x["age"])
print("Oldest person:", oldest_person)  # Output: {"name": "Charlie", "age": 35}

# -------------------- 4. Comparing tuples based on a custom function -------------------- #
tuples = [(1, 5), (2, 2), (3, 10)]
max_tuple = max(tuples, key=lambda x: abs(x[0] - x[1]))
print("Tuple with the largest difference:", max_tuple)  # Output: (3, 10)

# -------------------- 5. Using `prod` to compare lists based on product of their elements -------------------- #
lists = [[1, 2], [3, 4], [2, 5]]
largest_product_list = max(lists, key=prod)
print("List with the largest product:", largest_product_list)  # Output: [3, 4]

# -------------------- 6. Finding the largest odd number -------------------- #
nums = [2, 3, 13, 20]
largest_odd = max(nums, key=lambda x: x % 2 != 0)
print("Largest odd number:", largest_odd)  # Output: 13

# -------------------- 7. Finding the longest word in a phrase -------------------- #
phrase = "ciao mamma sono una fraseeee"
words_in_phrase = phrase.split()
longest_word_in_phrase = max(words_in_phrase, key=len)
print("Longest word in phrase:", longest_word_in_phrase)  # Output: "fraseeee"

# -------------------- 8. Finding the shortest string ignoring spaces -------------------- #
def length_without_spaces(s):
    return len(s.replace(" ", ""))

words = ["hello world", "python", "AI"]
shortest = min(words, key=length_without_spaces)
print("Shortest string ignoring spaces:", shortest)  # Output: "AI"

# -------------------- Additional Notes -------------------- #
# The `max()` and `min()` functions in Python are powerful tools for finding
# the largest or smallest item in a collection based on a given criterion.
# You can pass a custom function to the `key` parameter to define how elements
# should be compared.

# Examples of other use cases:
# - Finding the string with the most vowels
# - Comparing objects with multiple attributes
# - Using `key=lambda` for advanced comparisons
