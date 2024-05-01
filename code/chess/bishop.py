from chess.figure import Figure


class Bishop(Figure):
    """ Слон """

    def score(self) -> int:
        return 3

    def char(self) -> str:
        return 'B'

    def can_move(self, row: int, col: int, row1: int, col1: int, fl: int = 1) -> bool:
        from vars import board
        i, j = row + 1, col + 1
        while i < 8 and j < 8:
            if i == row1 and j == col1:
                return True
            if board.field[i][j] is None:
                i, j = i + 1, j + 1
            else:
                break
        i, j = row - 1, col + 1
        while i >= 0 and j < 8:
            if i == row1 and j == col1:
                return True
            if board.field[i][j] is None:
                i, j = i - 1, j + 1
            else:
                break
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if i == row1 and j == col1:
                return True
            if board.field[i][j] is None:
                i, j = i - 1, j - 1
            else:
                break
        i, j = row + 1, col - 1
        while i < 8 and j >= 0:
            if i == row1 and j == col1:
                return True
            if board.field[i][j] is None:
                i, j = i + 1, j - 1
            else:
                break
        return False
