def word_search(board, word):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, cols = len(board), len(board[0])

    def search(x, y, index):
        if index == len(word):
            return True
        if not (0 <= x < rows and 0 <= y < cols) or board[x][y] != word[index]:
            return False
        
        temp, board[x][y] = board[x][y], '#'
        for dx, dy in directions:
            if search(x + dx, y + dy, index + 1):
                return True
        board[x][y] = temp
        return False

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and search(i, j, 0):
                return True
    return False
