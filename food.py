import pygame
import random
from game_settings import *

class Food:
    def __init__(self):
        self.spawn()

    def spawn(self):
        self.x = round(random.randrange(0, DISPLAY_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
        self.y = round(random.randrange(0, DISPLAY_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    def draw(self, display):
        pygame.draw.rect(display, GREEN, [self.x, self.y, SNAKE_BLOCK, SNAKE_BLOCK])