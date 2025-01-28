# dfs solurtion
# Time complexity: o(m*n)
# Space complexity: o(m*n) bad case of recursion stack
from collections import deque

def count_islands(grid):
    # Directions for moving up, down, left, and right
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def explore_island(x, y):
        # If the current cell is water or already visited, return
        if grid[x][y] == 0:
            return
        # Mark the current cell as visited
        grid[x][y] = 0
        # Explore all neighboring cells
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols:
                explore_island(new_x, new_y)

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found an unvisited land cell
                island_count += 1
                explore_island(i, j)  # Explore the entire island

    return island_count

# bfs solution
# Time complexity: o(m*n)
# Space complexity: O(min(rows,cols)) for the baddest case of the queue
def count_islands(grid):
    # Directions for moving up, down, left, and right
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found an unvisited land cell
                island_count += 1
                # Explore the entire island using BFS
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    if grid[x][y] == 0:
                        continue
                    grid[x][y] = 0  # Mark the current cell as visited
                    for dx, dy in directions:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x < rows and 0 <= new_y < cols:
                            queue.append((new_x, new_y))

    return island_count