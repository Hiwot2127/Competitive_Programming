class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_unit(unit):
            seen = set()
            for digit in unit:
                if digit != '.':
                    if digit in seen:
                        return False
                    seen.add(digit)
            return True

        for row in board:
            if not is_valid_unit(row):
              return False

        for col in zip(*board):
            if not is_valid_unit(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not is_valid_unit(sub_box):
                    return False

        return True

   