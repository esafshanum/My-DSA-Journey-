class Solution(object):
    def isValidSudoku(self, board):
        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]

                    if ((num, i) in seen or
                        (j, num) in seen or
                        (i // 3, j // 3, num) in seen):
                        return False

                    seen.add((num, i))
                    seen.add((j, num))
                    seen.add((i // 3, j // 3, num))

        return True