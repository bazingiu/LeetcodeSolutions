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
# k = number of characters associated with the digit
# n^k possibilities 
# temporal complexity: O(n^k)
#spatial complexity: O(k^n + n) beacuse of the recursion stack and the output list