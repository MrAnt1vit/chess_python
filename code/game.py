from random import shuffle, randint
import pygame, finish, menu
from chess.imports import *
from utils import fps, load_image, terminate, Button, WHITE, BLACK
from vars import board


class Game:
    ''' Основное окно '''

    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock, name_w: str, name_b: str, flag: bool = False):
        ''' Инициализация '''
        if flag:
            self.gen()
        board.width_frame = 3
        self.screen = screen
        self.size = self.width, self.height = screen.get_width(), screen.get_height()
        self.clock = clock
        self.name_b = name_b
        self.name_w = name_w
        self.scores = [0, 0]
        self.player_b_color = 'blue'
        self.player_w_color = 'green'
        self.x = self.y = -1
        self.images = {
            'bB': load_image('kit_figures1/bishop_black.png'),
            'wB': load_image('kit_figures1/bishop_white.png'),
            'bK': load_image('kit_figures1/king_black.png'),
            'wK': load_image('kit_figures1/king_white.png'),
            'bN': load_image('kit_figures1/knight_black.png'),
            'wN': load_image('kit_figures1/knight_white.png'),
            'bP': load_image('kit_figures1/pawn_black.png'),
            'wP': load_image('kit_figures1/pawn_white.png'),
            'bQ': load_image('kit_figures1/queen_black.png'),
            'wQ': load_image('kit_figures1/queen_white.png'),
            'bR': load_image('kit_figures1/rook_black.png'),
            'wR': load_image('kit_figures1/rook_white.png')
        }
        pygame.display.set_caption("Шахматы")
        self.all_sprites = pygame.sprite.Group()
        self.chooze_white_sprites = pygame.sprite.Group()
        self.chooze_black_sprites = pygame.sprite.Group()
        self.white = []
        self.black = []
        a = ['wQ', 'wR', 'wB', 'wN']
        b = ['bQ', 'bR', 'bB', 'bN']
        for i in range(4):
            self.white.append(pygame.sprite.Sprite(self.chooze_white_sprites))
            img = self.images[a[i]]
            koeff = (board.cell_size - 5) / img.get_height()
            self.white[i].image = pygame.transform.scale(
                self.images[a[i]], (img.get_width() * koeff, img.get_height() * koeff))

            self.white[i].rect = self.white[i].image.get_rect()

            self.white[i].rect.center = 630 + int(board.cell_size * (i + 0.5)), \
                                        300 + int(board.cell_size * 0.5)

            self.black.append(pygame.sprite.Sprite(self.chooze_black_sprites))
            img = self.images[b[i]]
            koeff = (board.cell_size - 5) / img.get_height()
            self.black[i].image = pygame.transform.scale(
                self.images[b[i]], (img.get_width() * koeff, img.get_height() * koeff))

            self.black[i].rect = self.black[i].image.get_rect()

            self.black[i].rect.center = 630 + int(board.cell_size * (i + 0.5)), \
                                        300 + int(board.cell_size * 0.5)
        for i in range(board.width):
            for j in range(board.height):
                if board.cell(i, j) != '  ':
                    board.field[i][j].sprite = pygame.sprite.Sprite(self.all_sprites)
                    img = self.images[board.cell(i, j)]
                    koeff = (board.cell_size - 5) / img.get_height()
                    board.field[i][j].sprite.image = pygame.transform.scale(
                        self.images[board.cell(i, j)], (
                            img.get_width() * koeff, img.get_height() * koeff))

                    board.field[i][j].sprite.rect = board.field[i][
                        j].sprite.image.get_rect()

                    board.field[i][j].sprite.rect.center = board.left + int(
                        board.cell_size * (j + 0.5)), board.left + int(
                        board.cell_size * (
                                7 - i + 0.5))
        self.pawn_x = self.pawn_y = -1
        self.chooze_fig_fl = 0
        self.move_x = self.move_y = self.move_to_x = self.move_to_y = self.v_x = self.v_y = -1
        self.v = 350
        self.move_fl = False
        self.buttons = pygame.sprite.Group()
        Button('Назад', 20, 20, self.buttons)
        Button('Сдаться', 790, 530, self.buttons)
        self.main()

    def gen(self) -> None:
        ''' Генерация поля для шахмат-960 '''
        a = [0, 1, 2, 3, 4, 5, 6, 7]
        shuffle(a)
        x, y, z = sorted(a[:3])
        for i in range(8):
            board.field[0][i] = None
            board.field[7][i] = None
        board.field[0][x] = Rook(WHITE)
        board.field[7][x] = Rook(BLACK)
        board.field[0][y] = King(WHITE)
        board.field[7][y] = King(BLACK)
        board.field[0][z] = Rook(WHITE)
        board.field[7][z] = Rook(BLACK)
        b, c = [], []
        for i in a[3:]:
            if i % 2 == 0:
                b.append(i)
            else:
                c.append(i)
        i = randint(0, len(b) - 1)
        x = b[i]
        del b[i]
        i = randint(0, len(c) - 1)
        y = c[i]
        del c[i]
        board.field[0][x] = Bishop(WHITE)
        board.field[7][x] = Bishop(BLACK)
        board.field[0][y] = Bishop(WHITE)
        board.field[7][y] = Bishop(BLACK)
        for i in c:
            b.append(i)
        shuffle(b)
        x, y, z = b
        board.field[0][x] = Knight(WHITE)
        board.field[7][x] = Knight(BLACK)
        board.field[0][y] = Knight(WHITE)
        board.field[7][y] = Knight(BLACK)
        board.field[0][z] = Queen(WHITE)
        board.field[7][z] = Queen(BLACK)

    def main(self) -> None:
        ''' Обработка событий и отображение на экране '''
        next_window = None
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos)
                    for obj in self.buttons:
                        new = obj.get_click(event.pos)
                        if new:
                            next_window = new
                            running = False
            if self.move_fl:
                self.move_fig()
            self.screen.fill((0, 0, 0))
            self.render()
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(fps)
        if next_window == 'Назад':
            self.back()
        elif next_window == 'Сдаться':
            self.finish(3)

    def move_fig(self) -> None:
        ''' Передвижение фигуры (анимация) '''
        x, y = board.field[self.move_to_x][self.move_to_y].sprite.rect.center
        to_x, to_y = board.get_coords(self.move_to_x, self.move_to_y)
        if x > to_x:
            x = max(x - int(self.v_x / fps), to_x)
        else:
            x = min(x + int(self.v_x / fps), to_x)
        if y > to_y:
            y = max(y - int(self.v_y / fps), to_y)
        else:
            y = min(y + self.v_y / fps, to_y)
        if (x, y) == (to_x, to_y):
            x, y = self.move_to_x, self.move_to_y
            board.field[x][y].sprite.rect.center = board.get_coords(x, y)
            pygame.sprite.spritecollide(board.field[x][y].sprite,
                                        self.all_sprites, True)
            fl = board.check_mat()
            if fl:
                self.finish(fl)
            fin = 7 if board.color == BLACK else 0
            if fin == x and type(board.get_piece(x, y)) is Pawn:
                clr = board.opponent(board.color)
                self.pawn_x, self.pawn_y = x, y
                self.chooze_fig_fl = clr + 1
                board.field[x][y].sprite = pygame.sprite.Sprite(self.all_sprites)
                img = self.images[board.cell(x, y)]
                koeff = (board.cell_size - 5) / img.get_height()
                board.field[x][y].sprite.image = pygame.transform.scale(
                    self.images[board.cell(x, y)], (
                        img.get_width() * koeff, img.get_height() * koeff))

                board.field[x][y].sprite.rect = board.field[x][
                    y].sprite.image.get_rect()

                board.field[x][y].sprite.rect.center = board.get_coords(x, y)
            else:
                self.all_sprites.add(board.field[x][y].sprite)
            self.x = self.y = -1
            self.move_x = self.move_y = self.move_to_x = self.move_to_y = -1
            self.move_fl = False
            self.recount()
            return
        board.field[self.move_to_x][self.move_to_y].sprite.rect.center = x, y

    def recount(self) -> None:
        ''' Подсчет очков игроков '''
        cnt_w, cnt_b = 0, 0
        for i in board.field:
            for j in i:
                if j is not None:
                    if j.get_color() == WHITE:
                        cnt_w += j.score()
                    else:
                        cnt_b += j.score()
        self.scores = [38 - cnt_w, 38 - cnt_b]

    def print_text(self, text: str, x: int, y: int, size: int, color: [WHITE, BLACK]) -> None:
        ''' Вывод текста на экран '''
        self.text = text
        self.font = pygame.font.Font(None, size)
        self.text_r = self.font.render(self.text, True, pygame.Color(color))
        self.rect = pygame.rect.Rect(*[x, y, self.text_r.get_width(), self.text_r.get_height()])
        self.screen.blit(self.text_r, (self.rect.x, self.rect.y))

    def render(self) -> None:
        ''' Отрисовка поля '''
        pygame.draw.rect(self.screen, 'white',
                         [board.left - board.width_frame,
                          board.top - board.width_frame,
                          board.cell_size * board.width + board.width_frame * 2,
                          board.cell_size * board.height + board.width_frame * 2])
        colors = [(240, 218, 181), (181, 131, 99), (242, 130, 116), (212, 89, 74), (245, 236, 115),
                  (216, 194, 74)]
        for i in range(board.width):
            for j in range(board.height):
                x = 7 - i
                y = j
                r, g, b = colors[(i + j) % 2]
                if (self.x != -1 and (x == self.x and y == self.y) or
                        board.move_piece(self.x, self.y, x, y, 0) and
                        not board.field[x][y]):
                    if (i + j) % 2:
                        r, g, b = colors[5]
                    else:
                        r, g, b = colors[4]
                elif (self.x != -1 and (x != self.x or y != self.y) and
                      board.move_piece(self.x, self.y, x, y, 0) and
                      board.field[x][y] and
                      board.field[x][y].color != board.field[self.x][self.y].color):
                    if (i + j) % 2:
                        r, g, b = colors[3]
                    else:
                        r, g, b = colors[2]
                pygame.draw.rect(self.screen, (r, g, b),
                                 [board.left + board.cell_size * j,
                                  board.top + board.cell_size * i,
                                  board.cell_size, board.cell_size])
        if self.chooze_fig_fl:
            self.draw_chooze_fig()
        for obj in self.buttons:
            obj.render(self.screen)

        self.print_text('Текущий игрок:', 525, 100, 45, 'red')
        self.print_text('Текущий цвет:', 525, 150, 45, 'red')
        if board.color == BLACK:
            now_player = self.name_b
            now_color = 'Черный'
            player_color = self.player_b_color
        else:
            now_player = self.name_w
            now_color = 'Белый'
            player_color = self.player_w_color
        self.print_text(now_player, 800, 100, 40, player_color)
        self.print_text(now_color, 800, 150, 40, 'white' if board.color == WHITE else 'grey')

        self.print_text('Очки', 690, 375, 45, 'red')
        self.print_text(self.name_w, 550, 425, 40, self.player_w_color)
        self.print_text(self.name_b, 830, 425, 40, self.player_b_color)
        self.print_text(str(self.scores[1]), 575, 475, 40, self.player_w_color)
        self.print_text(str(self.scores[0]), 855, 475, 40, self.player_b_color)

    def draw_chooze_fig(self) -> None:
        ''' Отрисовка выбора фигуры (превращение) '''
        top, left = 630, 300
        pygame.draw.rect(self.screen, (181, 131, 99),
                         [top - board.width_frame,
                          left - board.width_frame,
                          board.cell_size * 4 + board.width_frame * 2,
                          board.cell_size + board.width_frame * 2])
        pygame.draw.rect(self.screen, 'white',
                         [top, left, board.cell_size * 4, board.cell_size])
        if self.chooze_fig_fl == 2:
            self.chooze_white_sprites.draw(self.screen)
        else:
            self.chooze_black_sprites.draw(self.screen)

    def get_cell(self, mouse_pos: list[int, int]) -> [tuple[int, int], None]:
        ''' Узнать клетку по нажатию мыши '''
        cell_x = (mouse_pos[0] - board.left) // board.cell_size
        cell_y = (mouse_pos[1] - board.top) // board.cell_size
        if cell_x < 0 or cell_x >= board.width or cell_y < 0 or cell_y >= board.height:
            return None
        return cell_x, 7 - cell_y

    def on_click(self, cell: tuple[int, int]) -> None:
        ''' Обработка клика игрока (на поле) '''
        if self.chooze_fig_fl or self.move_fl:
            return
        y, x = cell
        if self.x != -1:
            if board.move_piece(self.x, self.y, x, y):
                self.move_fl = True
                self.move_x = self.x
                self.move_y = self.y
                self.move_to_x = x
                self.move_to_y = y
                board.NUM += 1
                st_x, st_y = board.get_coords(self.move_x, self.move_y)
                to_x, to_y = board.get_coords(self.move_to_x, self.move_to_y)
                if to_x != st_x and to_y != st_y:
                    kf = abs((to_x - st_x) / (to_y - st_y))
                    kf1 = abs((to_y - st_y) / (to_x - st_x))
                    v_y = ((self.v * self.v) / (kf * kf + 1)) ** 0.5
                    v_x = ((self.v * self.v) / (kf1 * kf1 + 1)) ** 0.5
                elif to_x == st_x:
                    v_y = self.v
                    v_x = 0
                else:
                    v_x = self.v
                    v_y = 0
                self.v_x = v_x
                self.v_y = v_y
            else:
                piece = board.get_piece(x, y)
                if piece is not None and piece.color == board.color:
                    self.x, self.y = x, y
                else:
                    self.x = self.y = -1
        elif board.cell(cell[1], cell[0]) != '  ':
            piece = board.get_piece(x, y)
            if piece is not None and piece.color == board.color:
                self.x, self.y = x, y
            else:
                self.x = self.y = -1
        else:
            self.x = self.y = -1

    def get_click(self, mouse_pos: list[int, int]) -> None:
        ''' Обработка клика '''
        if self.chooze_fig_fl:
            cell_x = (mouse_pos[0] - 630) // board.cell_size
            cell_y = (mouse_pos[1] - 300) // board.cell_size
            if cell_x < 0 or cell_x >= 4 or cell_y < 0 or cell_y >= 1:
                return None
            board.field[self.pawn_x][self.pawn_y].sprite.kill()
            if cell_x == 3:
                board.field[self.pawn_x][self.pawn_y] = Knight(self.chooze_fig_fl - 1)
            elif cell_x == 2:
                board.field[self.pawn_x][self.pawn_y] = Bishop(self.chooze_fig_fl - 1)
            elif cell_x == 1:
                board.field[self.pawn_x][self.pawn_y] = Rook(self.chooze_fig_fl - 1)
            elif cell_x == 0:
                board.field[self.pawn_x][self.pawn_y] = Queen(self.chooze_fig_fl - 1)
            board.field[self.pawn_x][self.pawn_y].sprite = pygame.sprite.Sprite(
                self.all_sprites)
            img = self.images[board.cell(self.pawn_x, self.pawn_y)]
            koeff = (board.cell_size - 5) / img.get_height()
            board.field[self.pawn_x][self.pawn_y].sprite.image = pygame.transform.scale(
                self.images[board.cell(self.pawn_x, self.pawn_y)], (
                    img.get_width() * koeff, img.get_height() * koeff))

            board.field[self.pawn_x][self.pawn_y].sprite.rect = board.field[self.pawn_x][
                self.pawn_y].sprite.image.get_rect()

            board.field[self.pawn_x][self.pawn_y].sprite.rect.center = board.get_coords(
                self.pawn_x, self.pawn_y)
            self.chooze_fig_fl = 0
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def back(self) -> None:
        ''' Переход в основное окно '''
        menu_window = menu.Menu(self.screen, self.clock)

    def finish(self, fl: int) -> None:
        ''' Переход в финальное окно '''
        winner = None
        if fl == 3:
            if board.color == BLACK:
                winner = self.name_w
            else:
                winner = self.name_b
        elif fl == 2:
            winner = 'Ничья'
        elif fl == 1:
            if board.opponent(board.color) == BLACK:
                winner = self.name_b
            else:
                winner = self.name_w
        finish_window = finish.Finish(self.screen, self.clock, winner, self.name_w, self.name_b)
