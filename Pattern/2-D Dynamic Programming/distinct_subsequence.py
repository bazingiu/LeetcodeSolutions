# Time complexity = O(len(s) * len(t))
def count_distinct_subsequences(source, target):
    # Memoization dictionary
    memo = {}
    
    def find_subsequences(source_idx, target_idx):
        # Base case: all characters of target are matched
        if target_idx == len(target):
            return 1
        # Base case: source is exhausted without fully matching target
        if source_idx == len(source):
            return 0
        
        # Check if the result is already computed
        if (source_idx, target_idx) in memo:
            return memo[(source_idx, target_idx)]
        
        # Recursive case
        count = 0
        # If characters match, move both pointers forward
        if source[source_idx] == target[target_idx]:
            count += find_subsequences(source_idx + 1, target_idx + 1)
        # Always consider skipping the current character in source
        count += find_subsequences(source_idx + 1, target_idx)
        
        # Store the result in memo
        memo[(source_idx, target_idx)] = count
        return count
    
    # Start the recursion from the beginning of both strings
    return find_subsequences(0, 0)
