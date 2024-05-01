from utils import WHITE, BLACK

class Figure:
    ''' Базовый класс фигуры '''
    def __init__(self, color: [WHITE, BLACK]):
        ''' Инициализация '''
        self.color = color

    def get_color(self) -> [WHITE, BLACK]:
        ''' Узнать цвет фигуры '''
        return self.color

    def score(self) -> int:
        ''' Текущая цена фигуры '''

    def char(self) -> str:
        ''' Текстовое обозначение фигуры '''

    def can_move(self, row: int, col: int, row1: int, col1: int, fl: int) -> bool:
        ''' Может ли фигура так походить? '''

    def can_attack(self, row: int, col: int, row1: int, col1: int, fl: int) -> bool:
        ''' Может ли фигура так съесть? '''
        return self.can_move(row, col, row1, col1, fl)
