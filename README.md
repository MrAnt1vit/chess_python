# Графическое приложение "Шахматы"

<h3> Общее описание и задачи: </h3>

Реализация всем известной игры "Шахматы" с использованием графического интерфейса.
Приложение должно давать возможность играть между пользователями на одном устройстве (локально).

<h1></h1>

<h2> Функционал: </h2>

```
> Игра между двумя игроками в шахматы по стандартным правилам
> Возможность указывать имена игроков перед партией
> Корректное отображение всех фигур на поле, а также "съеденных"
```

<h2> Стек технологий </h2>

> Библиотеки

```
pygame
os - встроенная
sys - встроенная
```

<h2> Архитектура: </h2>

<h3> Окна и перемещение между ними: </h3>

```
Стартовое окно <-> Окно ввода имен и выбора варианта игры
Окно ввода имен и выбора варианта игры <-> Игра (основное окно)
Основное окно -> Окно итога игры (завершающее) -> Окно выбора
```

<h3> Классы, файлы и их функции: </h3>

<h5> ~/code/ - папка с кодом </h5>

```python
''' main.py - запуск кода и задание переменных '''

if __name__ == '__main__':
    ''' Запуск '''
```

```python
''' utils.py - вспомогательные классы и функции'''

def terminate():
    '''Выход из программы'''

def load_image(): 
    '''Загрузка изображения (фон, фигуры и тп)'''


class Button:
    '''Класс кнопки для использования в окнах'''
    
    def __init__(self, text : str, x : int, y : int):
        ''' Инициализация '''
    
    def render(self, screen):
        ''' Отображение на экране'''
    
    def check_click(self, coords):
        ''' Проверка на нажатие '''
        
    def swap_window(self):
        ''' Смена окна '''
    
    def get_click(self, mouse_position):
        ''' Обработать клик '''


class InputName:
    ''' Поле ввода слов (имени игрока) '''
    def __init__(self, text : str, x : int, y : int):
        ''' Инициализация '''

    def render(self, screen):
        ''' Отображение на экране '''

    def check_click(self, coords):
        ''' Проверка на то, что кнопка нажата '''

    def get_click(self, mouse_position):
        ''' Обработка клика '''


class RadioButton(Button):
    ''' Кнопка, когда из нескольких можно выбрать лишь одну '''
    def __init__(self, text : str, x : int, y : int, active : bool):
        ''' Инициализация '''
        super().__init__(text, x, y)

    def render(self, screen):
        ''' Отображение на экране '''

    def get_click(self, mouse_position):
        ''' Обработка клика '''
```

```python
''' finish.py - финальное окно '''
import pygame

class Final:
    def __init__(self, screen : pygame.Surface, clock : pygame.time.Clock, winner : str, names : tuple):
        ''' Инициализация '''

    def write(self):
        ''' Вывод текста на экран '''

    def main(self):
        ''' Обработка событий и отображение на экране '''

    def back(self):
        ''' Возврат в окно выбора '''
```

```python
''' game.py - Основное окно '''
import pygame


class Game:
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock, names: tuple):
        ''' Инициализация '''

    def main(self):
        ''' Обработка событий и отображение на экране '''

    def move_figure(self):
        ''' Передвижение фигуры '''

    def recount(self):
        ''' Подсчет очков игроков '''

    def print_text(self):
        ''' Вывод текста на экран '''

    def render(self):
        ''' Отрисовка поля '''

    def get_cell(self, mouse_position):
        ''' Узнать клетку по нажатию мыши '''

    def on_click(self):
        ''' Обработка клика игрока (на поле) '''

    def get_click(self):
        ''' Обработка клика (на экране) '''

    def back(self):
        ''' Переход в основное окно '''

    def finish(self):
        ''' Переход в финальное окно '''
```

```python
''' menu.py - Окно выбора '''
import pygame

class Menu:
    def __init__(self, screen: pygame.Surface, clock : pygame.time.Clock):
        ''' Инициализация '''

    def main(self):
        ''' Обработка событий и отображение на экране '''

    def start_game(self):
        ''' Старт игры и переход в основное окно '''

    def back(self):
        ''' Переход в стартовое окно '''
```

```python
''' start.py - Стартовое окно '''
import pygame

class Start:
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock):
        ''' Инициализация '''

    def write(self):
        ''' Вывод текста на экран '''

    def main(self):
        ''' Обработка событий и отображение на экране '''

    def start(self):
        ''' Переход в стартовое окно '''
```

<h5> ~/code/chess - Поле, фигуры и тп </h5>

```python
''' board.py - Поле и расстановка фигур на нем. Основной класс для игры.'''


class Board:
    def __init__(self, width: int, height: int, left: int, top: int, cell_size: int, width_frame: int):
        ''' Инициализация '''

    def get_coords(self, x, y):
        ''' Получить координаты клетки на поле '''

    def is_under_attack(self, row, col, color):
        ''' Проверка, под атакой ли клетка '''

    def get_piece_string(self, row, col):
        ''' Получить фигуру в текстовом формате (обозначение) '''

    def get_piece(self, row, col):
        ''' Получить фигуру по клетке '''

    def move_piece(self, row, col, row1, col1):
        ''' Попробовать подвинуть фигуру '''

    def check_mate(self):
        ''' Проверка на мат/пат '''

    def opponent(self, color):
        ''' Получить цвет оппонента '''
```

```python
''' figure.py - класс Фигуры (шаблон) '''

class Figure:
    def __init__(self, color : int):
        ''' Инициализация '''
        
    def get_color(self):
        ''' Узнать цвет фигуры '''

    def score(self):
        ''' Текущая цена фигуры '''

    def char(self):
        ''' Текстовое обозначение фигуры '''

    def can_move(self, borad, row, col, row1, col1):
        ''' Может ли фигура так походить? '''

    def can_attack(self, board, row, col, row1, col1):
        ''' Может ли фигура так съесть? '''
```

```python
class Figure:
    pass

''' rook.py - файл ладьи '''
class Rook(Figure):
    ''' Ладья '''

''' pawn.py - файл пешка '''
class Pawn(Figure):
    ''' Пешка '''

''' Knight.py - файл коня '''
class Knight(Figure):
    ''' Конь '''

''' King.py - файл короля '''
class King(Figure):
    ''' Король '''

''' queen.py - файл ферзя '''
class Queen(Figure):
    ''' Ферзь '''

''' bishop.py - файл слона '''
class Bishop(Figure):
    ''' Слон '''
```

<h5> ~/img - необходимые картинки/фотки (фон, фигуры и тп.) </h5>

> Фоны

> Фигуры

<h2> Дополнительная часть (детали, которые не обязательно будут реализованны) </h2>

<h3> Дополнительный функционал: </h3>

```
> Возможность играть в нестандартные шахматы, напрмиер:
>> Шахматы Фишера - они же Шахматы-960
>> Вольные шахматы, они же Шахматы-5039
>>> (числа исторически появились из количества вариантов начальной расстановки)
>> Боевые шахматы
> Игра по сети с разных ПК
> Отслеживание статистики
> Анимация ходов (не "телепортирование" фигур)
> Отображение возможных ходов (подсветка полей)
```

<h3> Окна и перемещение между ними: </h3>

```
Дополнительно:
Окно выбора <-> Окно статистики
Окно выбора -> Расстановка фигур
Расстановка фигур -> Основное окно
```
