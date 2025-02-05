def palindrome_partitioning (s):
    def isPali(self, s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
    
    res = []
    
    def backtrack (start, path):
        if start == len(s):
            res.append(path)
            return
        for i in range(start, len(s)):
            if isPali(s[start:i+1]):
                res.append(s[start:i+1])
                backtrack(i+1)