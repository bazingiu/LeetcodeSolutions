from collections import defaultdict

# -------------------- 1. Basic usage of defaultdict -------------------- #
# A defaultdict can use various default factories like int, list, or set.
prova = defaultdict(int)

# If the key "dog" doesn't exist, it is initialized to 0 and incremented to 1
prova["dog"] += 1

# Assign the value 20 to the key 1 (integer key)
prova[1] = 20

# Print keys, values, and items
print("Keys:", prova.keys())      # Output: ['dog', 1]
print("Values:", prova.values())  # Output: [1, 20]
print("Items:", prova.items())    # Output: [('dog', 1), (1, 20)]

# -------------------- 2. Using list as the default factory -------------------- #
prova_list = defaultdict(list)

# Append an element to the list associated with the key "frutta"
prova_list["frutta"].append("mela")
print("prova_list:", prova_list)  # Output: {'frutta': ['mela']}

# -------------------- 3. Using a custom default factory -------------------- #
def default_value():
    return "default_value"

prova_custom = defaultdict(default_value)

# Accessing a missing key initializes it with the custom default value
print("Missing key value:", prova_custom["chiave_mancante"])  # Output: "default_value"

# -------------------- 4. Iterating over items in a defaultdict -------------------- #
print("\nIterating over items in 'prova':")
for key, value in prova.items():
    print(f"Key: {key}, Value: {value}")

# -------------------- 5. Comparison with a standard dictionary -------------------- #
normal_dict = {}

# Accessing a missing key in a normal dictionary raises a KeyError
# Uncomment the following line to see the error:
# print(normal_dict["missing_key"])

# Add a key-value pair to the standard dictionary
normal_dict["name"] = "Alice"
print("\nA standard dictionary raises KeyError for missing keys, unlike defaultdict.")
print("Standard dictionary:", normal_dict)  # Output: {'name': 'Alice'}
