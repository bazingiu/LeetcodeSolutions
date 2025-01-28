#Time complexity: O(N log N)
#Space complexity: O(N)
def minimum_absolute_distance_optimized(arr):
    arr.sort()
    min_diff = float("inf")
    result = []
    
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff < min_diff:
            min_diff = diff
            result = [[arr[i-1], arr[i]]]  # Reset result for new min_diff
        elif diff == min_diff:
            result.append([arr[i-1], arr[i]])
    
    return result
