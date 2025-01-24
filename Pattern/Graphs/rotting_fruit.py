from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        time_elapsed = 0
        fresh_oranges = 0

        # Conta le arance fresche e individua le posizioni di quelle marce
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        # Direzioni di movimento: destra, sinistra, sotto, sopra
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Funzione per marcare un'arancia come marcia e aggiornarne lo stato
        def mark_rotten(r: int, c: int):
            nonlocal fresh_oranges
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 2  # Marca l'arancia come marcia
                queue.append((r, c))  # Aggiungi alla coda per ulteriore espansione
                fresh_oranges -= 1  # Riduci il conteggio delle arance fresche

        # BFS per espandere la marciatura delle arance
        while queue and fresh_oranges > 0:
            for _ in range(len(queue)):
                current_row, current_col = queue.popleft()
                for dr, dc in directions:
                    mark_rotten(current_row + dr, current_col + dc)
            time_elapsed += 1

        # Se rimangono arance fresche, restituisci -1, altrimenti il tempo trascorso
        return time_elapsed if fresh_oranges == 0 else -1

# Time complexity = O(m * n)
# Space complexity = O(m * n)