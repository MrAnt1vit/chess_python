from chess.figure import Figure


class Knight(Figure):
    """ Конь """

    def score(self) -> int:
        return 3

    def char(self) -> str:
        return 'N'

    def can_move(self, row: int, col: int, row1: int, col1: int, fl: int = 1):
        return abs(row - row1) * abs(col - col1) == 2
