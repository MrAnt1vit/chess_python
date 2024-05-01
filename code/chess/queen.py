from chess.figure import Figure
from chess.rook import Rook
from chess.bishop import Bishop


class Queen(Figure):
    """ Ферзь """

    def score(self) -> int:
        return 8

    def char(self) -> str:
        return 'Q'

    def can_move(self, row: int, col: int, row1: int, col1: int, fl: int = 1) -> bool:
        return (Rook(self.color).can_move(row, col, row1, col1, fl) or
                Bishop(self.color).can_move(row, col, row1, col1, fl))
