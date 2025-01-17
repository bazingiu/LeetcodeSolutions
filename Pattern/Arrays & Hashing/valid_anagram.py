# Time complexity: O(n), where n is the length of the strings
# Space complexity: O(1), since the count list has a fixed size of 26

def isAnagram(self, s: str, t: str) -> bool:
    # If the lengths of the strings are not equal, they cannot be anagrams
    if len(s) != len(t):
        return False

    # Initialize a list to count the frequency of each character in the alphabet
    count = [0] * 26

    # Iterate over both strings simultaneously
    for char_s, char_t in zip(s, t):
        # Increment the count for the character in s
        count[ord(char_s) - ord('a')] += 1
        # Decrement the count for the character in t
        count[ord(char_t) - ord('a')] -= 1

    # Check if all counts are zero, meaning both strings have the same characters with the same frequency
    return all(frequency == 0 for frequency in count)

# stiamo mappando le lettere dell'alfabeto in un array di 26 elementi
# ord('a') = 97

# char_b = ord('b') = 98
# ord(char_b) - ord('a') = 1

# char_z = ord('z') = 122
# ord(char_z) - ord('a') = 25