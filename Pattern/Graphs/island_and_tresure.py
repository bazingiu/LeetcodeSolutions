from collections import deque
from typing import List

class Solution:
    def calculateDistances(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        cells_to_process = deque()

        # Aggiungi tutte le celle con valore 0 (tesori) alla coda
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    cells_to_process.append((row, col))

        # Direzioni per il movimento: alto, basso, sinistra, destra
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS per calcolare le distanze
        while cells_to_process:
            current_row, current_col = cells_to_process.popleft()
            for delta_row, delta_col in directions:
                neighbor_row, neighbor_col = current_row + delta_row, current_col + delta_col
                # Verifica che la cella vicina sia valida e non ancora visitata
                if (0 <= neighbor_row < rows and 
                    0 <= neighbor_col < cols and 
                    grid[neighbor_row][neighbor_col] == 2147483647):  # Inizialmente non visitata
                    grid[neighbor_row][neighbor_col] = grid[current_row][current_col] + 1
                    cells_to_process.append((neighbor_row, neighbor_col))

        return grid
     
# Time complexity: O(n * m)
# Space complecity: O(n * m) 