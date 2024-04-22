from chess.figure import Figure
from utils import BLACK, WHITE


class Pawn(Figure):
    """ Пешка """

    def __init__(self, color: [WHITE, BLACK]):
        super().__init__(color)
        self.flag = 0

    def score(self) -> int:
        return 1

    def char(self) -> str:
        return 'P'

    def can_move(self, row: int, col: int, row1: int, col1: int, fl: int = 1) -> bool:
        from vars import board
        if col != col1:
            direction = 1 if (self.color == WHITE) else -1
            if (self.can_attack(row, col, row1, col1, fl) and
                    type(board.field[row1 - direction][col1]) is Pawn and
                    board.field[row1 - direction][col1].color != self.color and
                    board.field[row1 - direction][col1].flag == board.NUM - 1):
                if fl:
                    board.field[row1 - direction][col1].sprite.kill()
                    board.field[row1 - direction][col1] = None
                return True
            return False

        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        if row + direction == row1:
            return True

        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            self.flag = board.NUM
            return True

        return False

    def can_attack(self, row: int, col: int, row1: int, col1: int, fl: int = 1) -> bool:
        direction = 1 if (self.color == WHITE) else -1
        if (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1)):
            return True
        return False
