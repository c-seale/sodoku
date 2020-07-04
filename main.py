import os

import pygame

from object.board import Board

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

BACKGROUND_COLOR = pygame.Color('WHITE')

FRAMERATE_LIMIT = 60


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # App opens centered on screen

    # Init pygame
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    # Init game window
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('cseale\'s Sudoku!')
    sever_tick = pygame.time.Clock()

    surface.fill(BACKGROUND_COLOR)
    pygame.display.update()

    board = Board(surface, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Init music
    # TODO: Setup background music

    running = True
    while running:
        # Get active input
        pressed_keys = pygame.key.get_pressed()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and (
                    pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT])):
                running = False
                break

        board.update()

        sever_tick.tick(FRAMERATE_LIMIT)


def load_level(level: int) -> str:
    with open(r'data\levels\1', 'r') as f:
        puzzle = f.readline()
        solution = f.readline()
    return puzzle, solution


if __name__ == '__main__':
    main()
