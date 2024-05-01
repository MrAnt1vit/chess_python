import rating, start, game
from utils import *


class Menu:
    ''' Окно выбора '''
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock):
        ''' Инициализация '''
        self.screen = screen
        self.size = self.width, self.height = screen.get_width(), screen.get_height()
        self.clock = clock
        pygame.display.set_caption("Меню")
        self.fon = pygame.transform.scale(load_image('menu_fon.png'), (self.width, self.height))
        self.all_sprites = pygame.sprite.Group()

        self.buttons = pygame.sprite.Group()
        Button('Назад', 20, 20, self.all_sprites, self.buttons)
        Button('Играть', self.width - 20 - 100, 20, self.all_sprites, self.buttons)
        Button('Рейтинг', 20, 100, self.all_sprites, self.buttons)

        self.names = pygame.sprite.Group()
        InputName('Player1', 500, 225, self.all_sprites, self.names)
        InputName('Player2', 500, 300, self.all_sprites, self.names)

        self.radio_btns = pygame.sprite.Group()
        RadioButton('Классика', 300, 400, True, self.all_sprites, self.radio_btns)
        RadioButton('Шахматы-960', 475, 400, False, self.all_sprites, self.radio_btns)
        self.main()

    def main(self) -> None:
        ''' Обработка событий и отображение на экране '''
        next_window = None
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for obj in self.buttons:
                        new = obj.get_click(event.pos)
                        if new:
                            next_window = new
                            running = False
                    for obj in self.names:
                        if obj.get_click(event.pos):
                            obj.active = not obj.active
                        else:
                            obj.active = False
                    for obj in self.radio_btns:
                        if obj.get_click(event.pos):
                            for i in self.radio_btns:
                                i.active = False
                            obj.active = True
                elif event.type == pygame.KEYDOWN:
                    for obj in self.names:
                        if obj.active:
                            if event.key == pygame.K_BACKSPACE:
                                obj.text = obj.text[:-1]
                            elif event.key in (pygame.K_RETURN, pygame.K_ESCAPE, pygame.K_TAB):
                                obj.active = False
                            else:
                                if len(obj.text) < 15:
                                    obj.text += event.unicode
            self.screen.blit(self.fon, (0, 0))
            for obj in self.all_sprites:
                obj.render(self.screen)
            pygame.display.flip()
            self.clock.tick(fps)
        if next_window == 'Назад':
            self.back()
        elif next_window == 'Играть':
            game = None
            for obj in self.radio_btns:
                if obj.active:
                    game = obj.text
            self.start_game(game)
        elif next_window == 'Рейтинг':
            self.rating()
        else:
            terminate()

    def start_game(self, var: [None, str]) -> None:
        ''' Старт игры и переход в основное окно '''
        names = []
        for obj in self.names:
            names.append(obj.text)
        if var == 'Классика':
            game_window = game.Game(self.screen, self.clock, *names)
        elif var == 'Шахматы-960':
            game_window = game.Game(self.screen, self.clock, *names, flag=True)

    def rating(self) -> None:
        ''' Переход в рейтинговое окно '''
        rating_window = rating.Rating(self.screen, self.clock)

    def back(self) -> None:
        ''' Переход в стартовое окно '''
        start_window = start.Start(self.screen, self.clock)
