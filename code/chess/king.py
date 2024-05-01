from chess.rook import Rook
from utils import BLACK, WHITE
from chess.figure import Figure


class King(Figure):
    """ Король """

    def __init__(self, color: [WHITE, BLACK]):
        super().__init__(color)
        self.flag = 1

    def score(self) -> int:
        return 0

    def char(self) -> str:
        return 'K'

    def can_move(self, row: int, col: int, row1: int, col1: int, fl: int = 1) -> bool:
        from vars import board
        if (abs(row - row1) <= 1 and abs(col - col1) <= 1 and
                not board.is_under_attack(row1, col1, self.color)):
            if fl:
                self.flag = 0
            return True

        fig = board.get_piece(7, 0)
        if (row == row1 == 7 and col - 2 == col1 == 2 and
                self.flag and type(fig) is Rook and
                fig.color == self.color == BLACK and
                fig.flag):
            for i in range(1, 4):
                if board.get_piece(7, i) is not None:
                    return False
            for i in range(2, 5):
                if board.is_under_attack(7, i, self.color):
                    return False
            if fl:
                board.field[7][0].sprite.rect.center = board.get_coords(7, 3)
                board.move_piece(7, 0, 7, 3)
                board.color = board.opponent(board.color)
            return True

        fig = board.get_piece(7, 7)
        if (row == row1 == 7 and col + 2 == col1 == 6 and
                self.flag and type(fig) is Rook and
                fig.color == self.color == BLACK and
                fig.flag):
            for i in range(6, 4, -1):
                if board.get_piece(7, i) is not None:
                    return False
            for i in range(6, 3, -1):
                if board.is_under_attack(7, i, self.color):
                    return False
            if fl:
                board.field[7][7].sprite.rect.center = board.get_coords(7, 5)
                board.move_piece(7, 7, 7, 5)
                board.color = board.opponent(board.color)
            return True

        fig = board.get_piece(0, 0)
        if (row == row1 == 0 and col - 2 == col1 == 2 and
                self.flag and type(fig) is Rook and
                fig.color == self.color == WHITE and
                fig.flag):
            for i in range(1, 4):
                if board.get_piece(0, i) is not None:
                    return False
            for i in range(2, 5):
                if board.is_under_attack(0, i, self.color):
                    return False
            if fl:
                board.field[0][0].sprite.rect.center = board.get_coords(0, 3)
                board.move_piece(0, 0, 0, 3)
                board.color = board.opponent(board.color)
            return True

        fig = board.get_piece(0, 7)
        if (row == row1 == 0 and col + 2 == col1 == 6 and
                self.flag and type(fig) is Rook and
                fig.color == self.color == WHITE and
                fig.flag):
            for i in range(6, 4, -1):
                if board.get_piece(0, i) is not None:
                    return False
            for i in range(6, 3, -1):
                if board.is_under_attack(0, i, self.color):
                    return False
            if fl:
                board.field[0][7].sprite.rect.center = board.get_coords(0, 5)
                board.move_piece(0, 7, 0, 5)
                board.color = board.opponent(board.color)
            return True
        return False
