import pygame, sys, os


fps = 60
WHITE = 1
BLACK = 2


def terminate() -> None:
    '''Выход из программы'''
    pygame.quit()
    sys.exit()


def load_image(name: str, colorkey=None) -> pygame.Surface:
    '''Загрузка изображения (фон, фигуры и тп)'''
    fullname = os.path.join('../img', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Button(pygame.sprite.Sprite):
    '''Класс кнопки для использования в окнах'''
    def __init__(self, text: str, x: int, y: int, *groups: pygame.sprite.Group):
        ''' Инициализация '''
        super().__init__(*groups)
        self.text = text
        self.font = pygame.font.Font(None, 42)
        self.text_r = self.font.render(self.text, True, pygame.Color('black'))
        self.rect = pygame.rect.Rect(*[x, y, self.text_r.get_width() + 10, self.text_r.get_height() + 6])

    def render(self, screen: pygame.Surface) -> None:
        ''' Отображение на экране'''
        pygame.draw.rect(screen, pygame.Color('darkgrey'), self.rect)
        screen.blit(self.text_r, (self.rect.x + 5, self.rect.y + 3))

    def check_click(self, coords: list[int, int]) -> bool:
        ''' Проверка на нажатие '''
        return self.rect.x <= coords[0] <= self.rect.x + self.rect.w and \
            self.rect.y <= coords[1] <= self.rect.y + self.rect.h

    def swap_window(self) -> str:
        ''' Смена окна '''
        return self.text

    def get_click(self, mouse_pos: list[int, int]) -> [None, str]:
        ''' Обработать клик '''
        if self.check_click(mouse_pos):
            return self.swap_window()
        return None


class InputName(pygame.sprite.Sprite):
    ''' Поле ввода слов (имени игрока) '''
    def __init__(self, text: str, x: int, y: int, *groups: pygame.sprite.Group):
        ''' Инициализация '''
        super().__init__(*groups)
        self.colors = [(255, 255, 255), (0, 0, 255)]
        self.active = False
        self.text = text
        self.num = text[-1]
        self.color = 'Белые' if self.num == '1' else 'Черные'
        self.name_font = pygame.font.Font(None, 42)
        self.manual_font = pygame.font.Font(None, 32)
        self.rect = pygame.rect.Rect(*[x, y, 0, 0])

    def render(self, screen: pygame.Surface) -> None:
        ''' Отображение на экране '''
        text_r = self.name_font.render(self.text, True, pygame.Color('black'))
        self.rect.w = text_r.get_width() + 10
        self.rect.h = text_r.get_height() + 6
        pygame.draw.rect(screen, self.colors[self.active], self.rect, 2)
        screen.blit(text_r, (self.rect.x + 5, self.rect.y + 3))

        manual_r = self.manual_font.render(f'Игрок{self.num} ({self.color}):', True,
                                           pygame.Color('black'))
        screen.blit(manual_r, (self.rect.x - manual_r.get_width() - 15, self.rect.y + 8))

    def check_click(self, coords: list[int, int]) -> bool:
        ''' Проверка на то, что кнопка нажата '''
        return self.rect.x <= coords[0] <= self.rect.x + self.rect.w and \
            self.rect.y <= coords[1] <= self.rect.y + self.rect.h

    def get_click(self, mouse_pos: list[int, int]) -> bool:
        ''' Обработка клика '''
        return self.check_click(mouse_pos)


class RadioButton(Button):
    ''' Кнопка, когда из нескольких можно выбрать лишь одну '''
    def __init__(self, text: str, x: int, y: int, active: bool, *groups: pygame.sprite.Group):
        ''' Инициализация '''
        super().__init__(text, x, y, *groups)
        self.active = active
        self.font = pygame.font.Font(None, 30)

    def render(self, screen: pygame.Surface) -> None:
        ''' Отображение на экране '''
        super().render(screen)
        if self.active:
            pygame.draw.rect(screen, (0, 0, 255), self.rect, 3)

    def get_click(self, mouse_pos: list[int, int]) -> bool:
        ''' Обработка клика '''
        return self.check_click(mouse_pos)
