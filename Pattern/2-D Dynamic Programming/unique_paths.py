def unique_paths(rows: int, cols: int) -> int:
    """
    Calculate the number of unique paths in a grid of size rows x cols.
    This function uses dynamic programming to compute the number of unique paths
    from the top-left corner to the bottom-right corner of a grid. You can only
    move either down or right at any point in time.
    Args:
        rows (int): The number of rows in the grid.
        cols (int): The number of columns in the grid.
    Returns:
        int: The number of unique paths from the top-left to the bottom-right of the grid.
    Time Complexity: O(rows * cols)
    Space Complexity: O(rows * cols)
    """
    grid = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        grid[i][0] = 1
    for j in range(cols):
        grid[0][j] = 1
        
    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[rows - 1][cols - 1]
