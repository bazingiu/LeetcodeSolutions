def lengthOfLongestSubstring(self, s):
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring without repeating characters.

    Example:
        >>> lengthOfLongestSubstring("abcabcbb")
        3
        >>> lengthOfLongestSubstring("bbbbb")
        1
    Note:
        - The function uses a sliding window approach to keep track of the current substring without repeating characters.
        - A dictionary is used to store the last seen index of each character.

    # Time Complexity: O(n), where n is the length of the input string.
    # Space Complexity: O(min(n, m)), where n is the length of the input string and m is the size of the character set.
    """
    seen_chars = {}
    start = 0
    longest = 0
    for end, c in enumerate(s):
        if c in seen_chars and seen_chars[c] >= start:
            start = seen_chars[c] + 1
        seen_chars[c] = end
        longest = max(longest, end - start + 1)
    return longest
