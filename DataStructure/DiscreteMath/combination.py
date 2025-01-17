def combination(array):
    res = []
    def backtrack(start, path):
        res.append(path)
        for i in range(start, len(array)):
            backtrack(i + 1, path + [array[i]])
            
    backtrack(0, [])
    return res

array = [2,4,5]
print(combination( array)) 
# [[2], [2, 4], [2, 4, 5], [2, 5], [4], [4, 5], [5]]