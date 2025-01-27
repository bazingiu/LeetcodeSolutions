def palindrome_partitioning (s):
    def is_palindrome (s):
        return s == s[::-1]
    
    res = []
    
    def backtrack (start, path):
        if start == len(s):
            res.append(path)
            return
        for i in range(start, len(s)):
            if is_palindrome(s[start:i+1]):
                res.append(s[start:i+1])
                backtrack(i+1)