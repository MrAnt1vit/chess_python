from chess.board import Board
import pygame
from utils import load_image


clock = pygame.time.Clock()
image = load_image('start_fon.png')
size = width, height = image.get_width() // 2, image.get_height() // 2
screen = pygame.display.set_mode(size)
board = Board(8, 8, 100, 100, 50, 3)