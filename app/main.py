import os

import pygame

from app.menu import Menu
from app.object.board import Board
from app.validator import check_solution

SCREEN_WIDTH = 792
SCREEN_HEIGHT = 892

BACKGROUND_COLOR = pygame.Color('BLACK')

FRAMERATE_LIMIT = 60


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # App opens centered on screen

    # Init pygame
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    # Init game window
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('cseale\'s Sudoku!')
    sever_tick = pygame.time.Clock()

    display.fill(BACKGROUND_COLOR)
    pygame.display.update()

    board_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - 100))
    board = Board(board_surface, load_level(1)[0].rstrip())

    menu_surface = pygame.Surface((SCREEN_WIDTH, 100))
    menu = Menu(menu_surface)

    # Init music
    # TODO: Setup background music

    running = True
    while running:
        # Get active input
        pressed_keys = pygame.key.get_pressed()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT \
                    or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4
                        and (pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT])):
                running = False
                break
            if event.type == pygame.KEYUP:
                cell_val_input = None
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    cell_val_input = 1
                if event.key in [pygame.K_2, pygame.K_KP2]:
                    cell_val_input = 2
                if event.key in [pygame.K_3, pygame.K_KP3]:
                    cell_val_input = 3
                if event.key in [pygame.K_4, pygame.K_KP4]:
                    cell_val_input = 4
                if event.key in [pygame.K_5, pygame.K_KP5]:
                    cell_val_input = 5
                if event.key in [pygame.K_6, pygame.K_KP6]:
                    cell_val_input = 6
                if event.key in [pygame.K_7, pygame.K_KP7]:
                    cell_val_input = 7
                if event.key in [pygame.K_8, pygame.K_KP8]:
                    cell_val_input = 8
                if event.key in [pygame.K_9, pygame.K_KP9]:
                    cell_val_input = 9
                if event.key in [pygame.K_BACKSPACE, pygame.K_DELETE, pygame.K_0, pygame.K_KP0]:
                    cell_val_input = 0
                if cell_val_input is not None:
                    board.update_selected_cell(cell_val_input)
            if event.type == pygame.MOUSEBUTTONUP:
                # TODO: Clicking seems weird -- colliderect is true no matter where on screen you click.
                #       However, it's currently working well enough. Should investigate this behavior in the future
                mouse_pos = pygame.mouse.get_pos()
                mouse_rect = pygame.Rect(mouse_pos, (1, 1))
                if board.rect.colliderect(mouse_rect):
                    board.click(mouse_pos)
                if menu.rect.colliderect(menu.rect):
                    menu_option = menu.click((mouse_pos[0], SCREEN_HEIGHT - mouse_pos[1]))
                    if menu_option == menu.BTN_CHECK_SOLUTION:
                        if check_solution(board.board_state):
                            print('Solved!')  # TODO: Some kind of victory screen that leads to next level?
                        else:
                            print('Try Harder')

        board.update()
        display.blit(board_surface, (0, 0))

        menu.update()
        display.blit(menu_surface, (0, SCREEN_HEIGHT - 100))

        pygame.display.update()
        sever_tick.tick(FRAMERATE_LIMIT)


def load_level(level: int):
    with open(r'data/level/1', 'r') as f:
        puzzle = f.readline()
        solution = f.readline()
    return puzzle, solution


if __name__ == '__main__':
    main()
