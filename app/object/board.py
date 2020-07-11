from typing import Optional, Tuple

import pygame

from app.object.cell import Cell


class Board:
    INNER_BORDER_SIZE = 3
    INNER_BORDER_COLOR = pygame.Color('BLACK')
    CELL_COLOR_ONE = pygame.Color('AZURE3')
    CELL_COLOR_TWO = pygame.Color('LIGHTSTEELBLUE2')

    def __init__(self, surface: pygame.Surface, puzzle: str):
        self._surface = surface
        self.rect = pygame.Rect((0, 0), (surface.get_width(), surface.get_height()))
        self.cells = None

        self.setup_board(puzzle)

    @property
    def selected_cell(self) -> Optional[Cell]:
        for cell in self.cells:
            if cell.is_selected:
                return cell
        return None

    @property
    def board_state(self) -> str:
        return ''.join([str(cell.value) for cell in self.cells])

    def click(self, mouse_pos: Tuple[int, int]):
        cell_to_select = None
        for cell in self.cells:
            if cell.rect.colliderect(pygame.Rect(mouse_pos, (1, 1))):
                cell_to_select = cell
                break
        for cell in self.cells:
            if cell.is_selected:
                cell.deselect()
                break
        if cell_to_select:
            cell_to_select.select()

    def setup_board(self, puzzle: str):
        cell_width = self._surface.get_width() // 9
        cell_height = self._surface.get_height() // 9
        self.cells = list()

        cell_y = 0
        cell_val_idx = 0
        for row in range(0, 9):
            cell_x = 0
            for col in range(0, 9):
                cell_color = self.CELL_COLOR_ONE
                if (row in [0, 1, 2] or row in [6, 7, 8]) and (col in [0, 1, 2] or col in [6, 7, 8]) \
                        or (row in [3, 4, 5] and col in [3, 4, 5]):
                    cell_color = self.CELL_COLOR_TWO
                self.cells.append(Cell(self._surface, cell_x, cell_y, cell_width,
                                       cell_height, int(puzzle[cell_val_idx]), cell_color))
                cell_x += cell_width
                cell_val_idx += 1
            cell_y += cell_height

    def update(self):
        for cell in self.cells:
            cell.update()
        if self.selected_cell:
            self.selected_cell.update()  # Ensures cell is drawn on top

    def update_selected_cell(self, new_value: int):
        if self.selected_cell:
            self.selected_cell.value = new_value
