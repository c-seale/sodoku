import pygame

from object.cell import Cell


class Board:
    INNER_BORDER_SIZE = 3
    INNER_BORDER_COLOR = pygame.Color('BLACK')
    BACKGROUND_COLOR = pygame.Color('LIGHTSALMON4')

    def __init__(self, surface: pygame.Surface, x, y, width, height, puzzle):
        self.surface = surface
        self.rect = pygame.Rect((x, y), (width, height))

        self.surface.fill(self.BACKGROUND_COLOR)

        self._puzzle = puzzle
        self.cells = list()

        cell_width = surface.get_width() / 9
        cell_height = surface.get_height() / 9

        cell_y = 0
        cell_val_idx = 0
        for row in range(0, 9):
            cell_x = 0
            for col in range(0, 9):
                cell_color = pygame.Color('azure3')  # some blue
                if (row in [0, 1, 2] or row in [6, 7, 8]) and (col in [0, 1, 2] or col in [6, 7, 8]) \
                        or (row in [3, 4, 5] and col in [3, 4, 5]):
                    cell_color = pygame.Color('lightsteelblue2')  # some gray
                self.cells.append(Cell(self.surface, cell_x, cell_y, cell_width, cell_height,
                                       self._puzzle[cell_val_idx], cell_color))
                cell_x += cell_width
                cell_val_idx += 1
            cell_y += cell_height

    @property
    def active_cell(self):
        for cell in self.cells:
            if cell.is_selected:
                return cell
        return None

    @property
    def board_state(self) -> str:
        return ''.join([str(cell.value) for cell in self.cells])

    def update(self):
        self.surface.fill(self.BACKGROUND_COLOR)
        for cell in self.cells:
            cell.update()
        if self.active_cell:
            self.active_cell.update()  # Ensures cell is drawn on top
        pygame.display.update(self.rect)

    def set_active_cell(self, mouse_pos):
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

    def update_active_cell(self, new_value):
        if self.active_cell:
            self.active_cell.value = new_value
