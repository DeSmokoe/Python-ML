import pygame
import os
import random
pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 500

STAT_FONT = pygame.font.SysFont("comicsans", 50)

SNAKE_IMG = pygame.image.load(os.path.join("imgs", "Snake.png"))
FOOD_IMG = pygame.image.load(os.path.join("imgs", "Food.png"))
BG_IMG = pygame.image.load(os.path.join("imgs", "bg.png"))


class Snake:
    LENGTH = 1
    SNAKE = SNAKE_IMG

    def __init__(self):

        self.x = 250
        self.y = 250

    def draw(self, win):
        win.blit(self.SNAKE, (self.x, self.y))


class Food:

    def __init__(self):

        self.x = 0
        self.y = 0

        self.FOOD = FOOD_IMG

        self.set_position()

    def draw(self, win):
        win.blit(self.FOOD, (self.x, self.y))

    def set_position(self):
        self.x = random.randrange(0, 500)
        self.y = random.randrange(0, 500)


def draw_field(win, snake, foods, score):
    win.blit(BG_IMG, (0, 0))

    text = STAT_FONT.render("Score: " + str(score), True, (0, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    snake.draw(win)
    for food in foods:
        food.draw(win)

    pygame.display.update()


def main():

    clock = pygame.time.Clock()
    x = 50
    y = 50

    snake = Snake
    foods = [Food]
    score = 0

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_field(win, snake, foods, score)


main()
