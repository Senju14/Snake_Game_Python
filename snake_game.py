import pygame
import random
from game_settings import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption('Python Snake Game')
        self.clock = pygame.time.Clock()
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()

    def show_message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.display.blit(mesg, [DISPLAY_WIDTH / 6, DISPLAY_HEIGHT / 3])

    def game_loop(self):
        game_over = False
        game_close = False

        while not game_over:
            while game_close:
                self.display.fill(BLUE)
                self.show_message("Game Over! Press C-Play Again or Q-Quit", RED)
                self.scoreboard.display(self.display)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.__init__()
                            self.game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    self.snake.change_direction(event.key)

            if self.snake.check_collision(DISPLAY_WIDTH, DISPLAY_HEIGHT):
                game_close = True

            self.snake.move()
            self.display.fill(BLUE)

            if self.snake.eat(self.food):
                self.food.spawn()
                self.scoreboard.increase()

            self.food.draw(self.display)
            self.snake.draw(self.display)
            self.scoreboard.display(self.display)

            pygame.display.update()
            self.clock.tick(SNAKE_SPEED)

        pygame.quit()
        quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.game_loop()