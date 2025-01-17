def base_operation(str1, str2):
    # Concatenation
    print("Concatenation with str1:", str1)
    print(str1 + str2 + "\n")
    
    # Repetition
    print("Repetition with str1:", str1)
    print(str1 * 4 + "\n")
    
    # Slicing
    print("Slicing with str1:", str1)
    print(str1[0:2] + "\n")
    
    # Membership
    print("Membership with str1:", str1)
    print("H" in str1, "\n")
    
    # Iteration
    print("Iteration with str1:", str1)
    for i in str1:
        print(i)
    print("\n")
    
    # Count
    str1.count("l")

def modify_string(str1):
    # Capitalize 
    print("Capitalize with str1:", str1)
    print(str1.capitalize())
    
    # Lowercase
    print("Lowercase with str1:", str1)
    print(str1.lower())
    
    # Uppercase
    print("Uppercase with str1:", str1)
    print(str1.upper())
    
    # Swapcase
    print("Swapcase with str1:", str1)
    print(str1.swapcase())
    
    # Title
    print("Title with str1:", str1)
    print(str1.title())
    
def string_manipulation(str1, delimiter=" "):
   
    print("Original string:", str1)
    
    # Split
    split_str = str1.split(delimiter)
    print("Split string:", split_str)
    
    # Join
    joined_str = delimiter.join(split_str)
    print("Joined string:", joined_str)
    
    # Replace
    replaced_str = joined_str.replace(delimiter, "cccc")
    print("Replaced string:", replaced_str)
    
    # Strip
    # Rimuovere spazi all'inizio e alla fine della stringa
    stripped_str = str1.strip()
    print("Stripped string:", stripped_str)
    
    # Rimuovere caratteri specifici
    stripped_str = str1.strip("H")

def search_and_compare(str1, substring):
    # Find index of a substring
    print("Index of substring in str1:", str1)
    print(str1.find(substring))
    
    # Search for a substring
    print("Search for substring in str1:", str1)
    try:
        print(str1.index(substring))
    except ValueError:
        print("Substring not found")
    
    # Startswith
    print("Startswith with str1:", str1)
    print(str1.startswith("H"))
    
    # Endswith
    print("Endswith with str1:", str1)
    print(str1.endswith("n"))
    
#base_operation("Hello", "World")
#modify_string("Hello i like python")
#string_manipulation("Hello i like python ", " ")
search_and_compare("Hello i like python", "i")