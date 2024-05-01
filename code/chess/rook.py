from chess.figure import Figure
from utils import BLACK, WHITE


class Rook(Figure):
    """ Ладья """

    def __init__(self, color: [BLACK, WHITE]):
        super().__init__(color)
        self.flag = 1

    def score(self) -> int:
        return 5

    def char(self) -> str:
        return 'R'

    def can_move(self, row: int, col: int, row1: int, col1: int, fl: int = 1) -> bool:
        from vars import board
        if row != row1 and col != col1:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            if not (board.get_piece(row, c) is None):
                return False
        if fl:
            self.flag = 0
        return True
