def letter_combinations(digits):
    if not digits:
        return []
    
    digit_to_chars = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    combinations = []
    
    def backtrack(index, path):
        if index == len(digits):
            combinations.append("".join(path))
            return
        current_digit = digits[index]
        for char in digit_to_chars[current_digit]:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()
    
    backtrack(0, [])
    return combinations

print(letter_combinations("34"))

# n = digit
# temporal complexity: O(n *4^n) because we have 4 possible characters for each digit
#spatial complexity: O(4^n + n) beacuse of the recursion stack and the output list

# iterative solution
from typing import List

def letterCombinations(digits):
    if not digits:
        return []

    # Mapping digits to characters
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",  # Corretto
        "8": "tuv",
        "9": "wxyz",
    }

    # Start with an initial result of an empty string
    res = [""]

    # Iterate over each digit in the input string
    for digit in digits:
        tmp = []
        for curStr in res:
            for c in digitToChar[digit]:
                tmp.append(curStr + c)
        res = tmp
    return res