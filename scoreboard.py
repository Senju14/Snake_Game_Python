import pygame
from game_settings import *

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("comicsansms", 35)

    def increase(self):
        self.score += 1

    def display(self, display):
        score_text = self.font.render(f"Score: {self.score}", True, YELLOW)
        display.blit(score_text, [0, 0])