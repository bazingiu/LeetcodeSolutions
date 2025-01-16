def is_valid_parentheses(self, s):
    """
    Determine if the input string of parentheses is valid.
    A string of parentheses is valid if all types of parentheses are closed and opened in the correct order.
    :param s: A string containing only the characters '(', ')', '{', '}', '[' and ']'.
    :return: True if the input string is valid, False otherwise.
    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(n), where n is the length of the input string.
    """
    stack = []
    matching_bracket = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in matching_bracket:  # Closing bracket
            if stack and stack[-1] == matching_bracket[char]:  # Match top of stack
                stack.pop()
            else:
                return False  # No match or empty stack
        else:
            stack.append(char)  # Opening bracket

    return not stack  # Valid if stack is empty
