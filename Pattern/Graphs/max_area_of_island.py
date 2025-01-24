from collections import deque

def max_area_of_island(grid):
    # Directions for moving up, down, left, and right
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def bfs(x, y):
        queue = deque([(x, y)])
        area = 0
        while queue:
            cx, cy = queue.popleft()
            if grid[cx][cy] == 0:
                continue
            grid[cx][cy] = 0  # Mark as visited
            area += 1
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    queue.append((nx, ny))
        return area

    rows, cols = len(grid), len(grid[0])
    max_area = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found unvisited land
                max_area = max(max_area, bfs(i, j))

    return max_area

# Time complexity: o(m*n)
# Space complexity: o(m*n) bad case of recursion stack