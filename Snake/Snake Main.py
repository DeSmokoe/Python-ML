import pygame
import os
import neat
pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 500

STAT_FONT = pygame.font.SysFont("comicsans", 50)

SNAKE_IMG = pygame.image.load(os.path.join("imgs", "Snake.png"))
FOOD_IMG = pygame.image.load(os.path.join("imgs", "Food.png"))
BG_IMG = pygame.image.load(os.path.join("imgs", "bg.png"))

class Field:
    pass


class Snake:
    LENGTH = 1

    def __init__(self):

        self.x = 250
        self.y = 250

        self.SNAKE = SNAKE_IMG

    def draw(self, win):
        win.blit(self.SNAKE, (self.x, self.y))


class Food:
    pass


def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    snake = Snake

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

    draw_field(win, snake)


def draw_field(win, snake):
    win.blit(BG_IMG, (0, 0))

    text = STAT_FONT.render("Test: ", True, (255, 255, 255))
    win.blit(text, (10, 10))

    snake.draw(win)
    pygame.display.update()


main()
