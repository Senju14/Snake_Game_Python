import pygame
from game_settings import *

class Snake:
    def __init__(self):
        self.body = []
        self.length = 1
        self.x = DISPLAY_WIDTH / 2
        self.y = DISPLAY_HEIGHT / 2
        self.direction = "RIGHT"
        self.change_to = self.direction

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != "DOWN":
            self.change_to = "UP"
        if key == pygame.K_DOWN and self.direction != "UP":
            self.change_to = "DOWN"
        if key == pygame.K_LEFT and self.direction != "RIGHT":
            self.change_to = "LEFT"
        if key == pygame.K_RIGHT and self.direction != "LEFT":
            self.change_to = "RIGHT"

    def move(self):
        if self.change_to == "UP":
            self.y -= SNAKE_BLOCK
        if self.change_to == "DOWN":
            self.y += SNAKE_BLOCK
        if self.change_to == "LEFT":
            self.x -= SNAKE_BLOCK
        if self.change_to == "RIGHT":
            self.x += SNAKE_BLOCK
        
        self.direction = self.change_to
        self.body.insert(0, [self.x, self.y])
        if len(self.body) > self.length:
            del self.body[-1]

    def draw(self, display):
        for segment in self.body:
            pygame.draw.rect(display, BLACK, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])

    def check_collision(self, width, height):
        return (self.x >= width or self.x < 0 or 
                self.y >= height or self.y < 0 or 
                [self.x, self.y] in self.body[1:])

    def eat(self, food):
        if self.x == food.x and self.y == food.y:
            self.length += 1
            return True
        return False