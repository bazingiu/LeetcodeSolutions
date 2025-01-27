# Time complexity: O(m * n)
# Space complexity: O(m * n)
def longest_increasing_path_in_a_matrix(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    # Memoization table to store the length of the longest path starting from each cell
    memo = [[0] * n for _ in range(m)]

    # Directions for moving up, down, left, and right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(x, y):
        # If the result is already computed, return it
        if memo[x][y] != 0:
            return memo[x][y]

        max_length = 1  # At least the cell itself counts

        # Explore all four possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if the next cell is within bounds and strictly greater than the current cell
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                max_length = max(max_length, 1 + dfs(nx, ny))

        # Store the result in the memoization table
        memo[x][y] = max_length
        return max_length

    # Iterate over all cells in the matrix to find the global maximum
    global_max = 0
    for i in range(m):
        for j in range(n):
            global_max = max(global_max, dfs(i, j))

    return global_max