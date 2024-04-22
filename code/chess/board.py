from utils import WHITE, BLACK
from chess.imports import *


class Board:
    ''' Поле и расстановка фигур на нем. Основной класс для игры. '''

    def __init__(self, width: int = 8, height: int = 8, left: int = 10, top: int = 10, cell_size: int = 10,
                 width_frame: int = 2):
        ''' Инициализация '''
        self.NUM = 0
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.width_frame = width_frame
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def get_coords(self, x: int, y: int) -> tuple[int, int]:
        ''' Получить координаты клетки на поле '''
        return (self.left + int(self.cell_size * (y + 0.5)), self.left + int(
            self.cell_size * (7 - x + 0.5)))

    def is_under_attack(self, row: int, col: int, color: [WHITE, BLACK]) -> bool:
        ''' Проверка, под атакой ли клетка '''
        for i in range(8):
            for j in range(8):
                if (self.field[i][j] is not None and
                        (i != row or j != col) and
                        self.field[i][j].color != color and
                        self.field[i][j].can_attack(i, j, row, col, 0)):
                    return True
        return False

    def cell(self, row: int, col: int) -> str:
        ''' Получить фигуру на клетке (текстовый формат) '''
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row: int, col: int):
        ''' Получить фигуру в текстовом формате (обозначение) '''
        return self.field[row][col]

    def move_piece(self, row: int, col: int, row1: int, col1: int, fl: bool = True) -> bool:
        ''' Попробовать подвинуть фигуру '''
        pred = [[j for j in i] for i in self.field]
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(row, col, row1, col1, fl):
                return False
        elif self.field[row1][col1].get_color() == self.opponent(piece.get_color()):
            if not piece.can_attack(row, col, row1, col1, fl):
                return False
        else:
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        x, y = 0, 0
        for i in range(8):
            for j in range(8):
                p = self.get_piece(i, j)
                if type(p) is King and p.color == self.color:
                    x, y = i, j
                    break
        if self.is_under_attack(x, y, self.color):
            self.field = pred[:]
            return False
        if fl:
            self.color = self.opponent(self.color)
        else:
            self.field = pred[:]
        return True

    def check_mat(self) -> int:
        ''' Проверка на мат/пат '''
        x, y = -1, -1
        now = [[j for j in i] for i in self.field]
        for i in range(8):
            for j in range(8):
                fig = self.get_piece(i, j)
                if fig is not None and fig.color == self.color:
                    if type(fig) is King:
                        x, y = i, j
                    for i1 in range(8):
                        for j1 in range(8):
                            if self.move_piece(i, j, i1, j1, False):
                                self.field = [[kk for kk in k] for k in now]
                                return 0
                            self.field = [[kk for kk in k] for k in now]
        if self.is_under_attack(x, y, self.color):
            return 1
        return 2

    def opponent(self, color: [WHITE, BLACK]) -> [BLACK, WHITE]:
        ''' Получить цвет оппонента '''
        if color == WHITE:
            return BLACK
        else:
            return WHITE
