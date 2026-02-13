class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        # Directions for 8 neighbors
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        ]

        # First pass: mark transitions
        for i in range(rows):
            for j in range(cols):
                live_neighbors = 0

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        # Count original live cells
                        if abs(board[ni][nj]) == 1:
                            live_neighbors += 1

                # Rule 1 & 3: live → dead
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1   # was live, now dead

                # Rule 4: dead → live
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2    # was dead, now live

        # Second pass: finalize states
        for i in range(rows):
            for j in range(cols):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
