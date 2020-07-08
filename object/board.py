import pygame

from object.cell import Cell


class Board:
    INNER_BORDER_SIZE = 3
    INNER_BORDER_COLOR = pygame.Color('BLACK')

    DRAW_OUTER_BORDER = True
    OUTER_BORDER_SIZE = INNER_BORDER_SIZE
    OUTER_BORDER_COLOR = pygame.Color('BLACK')

    CELL_GRID_PADDING = 5

    BACKGROUND_COLOR = pygame.Color('LIGHTSALMON4')

    def __init__(self, surface: pygame.Surface, x, y, width, height, puzzle):
        self.surface = surface
        self.rect = pygame.Rect((x, y), (width, height))

        self.surface.fill(self.BACKGROUND_COLOR)

        self._puzzle = puzzle
        self.cells = list()

        cell_width = (self.surface.get_width() - self.OUTER_BORDER_SIZE * 2
                      - self.INNER_BORDER_SIZE * 2 - self.CELL_GRID_PADDING * 10) / 9
        cell_height = (self.surface.get_height() - self.OUTER_BORDER_SIZE * 2
                       - self.INNER_BORDER_SIZE * 2 - self.CELL_GRID_PADDING * 10) / 9

        cell_y = 0
        cell_val_idx = 0
        for row in range(0, 9):
            cell_x = 0
            if row == 0:
                cell_y = self.OUTER_BORDER_SIZE
            elif row % 9 == 0:
                cell_y += self.INNER_BORDER_SIZE * 2
            cell_y += self.CELL_GRID_PADDING
            for col in range(0, 9):
                if col == 0:
                    cell_x += self.OUTER_BORDER_SIZE
                elif col % 3 == 0:
                    cell_x += self.INNER_BORDER_SIZE
                cell_x += self.CELL_GRID_PADDING

                self.cells.append(
                    Cell(self.surface, cell_x, cell_y, cell_width, cell_height, self._puzzle[cell_val_idx]))

                cell_x += cell_width
                cell_val_idx += 1
            cell_y += cell_height

    @property
    def board_state(self) -> str:
        return ''.join([str(cell.value) for cell in self.cells])

    def update(self):
        self.draw_major_grid()
        self.draw_grid_cells()
        pygame.display.update(self.rect)

    def draw_grid_cells(self):
        for cell in self.cells:
            cell.update()

    def draw_major_grid(self):
        x_off = (self.rect.width - self.OUTER_BORDER_SIZE * 2 - self.INNER_BORDER_SIZE * 2) / 3
        y_off = (self.rect.height - self.OUTER_BORDER_SIZE * 2 - self.INNER_BORDER_SIZE * 2) / 3

        # Vertical lines
        pygame.draw.rect(self.surface, self.INNER_BORDER_COLOR,
                         pygame.Rect((self.rect.left + x_off, self.rect.top),
                                     (self.INNER_BORDER_SIZE, self.rect.height)))  # left
        pygame.draw.rect(self.surface, self.INNER_BORDER_COLOR,
                         pygame.Rect((self.rect.left + x_off * 2, self.rect.top),
                                     (self.INNER_BORDER_SIZE, self.rect.height)))  # right

        # Horizontal lines
        pygame.draw.rect(self.surface, self.INNER_BORDER_COLOR,
                         pygame.Rect((self.rect.left, self.rect.top + y_off),
                                     (self.rect.width, self.INNER_BORDER_SIZE)))  # top
        pygame.draw.rect(self.surface, self.INNER_BORDER_COLOR,
                         pygame.Rect((self.rect.left, self.rect.top + y_off * 2),
                                     (self.rect.width, self.INNER_BORDER_SIZE)))  # bottom

        # Draw outer border
        if self.DRAW_OUTER_BORDER:
            pygame.draw.rect(self.surface, self.OUTER_BORDER_COLOR,
                             pygame.Rect((self.rect.left, self.rect.top),
                                         (self.rect.width, self.OUTER_BORDER_SIZE)))  # top
            pygame.draw.rect(self.surface, self.OUTER_BORDER_COLOR,
                             pygame.Rect((self.rect.left, self.rect.bottom - self.OUTER_BORDER_SIZE),
                                         (self.rect.width, self.OUTER_BORDER_SIZE)))  # bottom
            pygame.draw.rect(self.surface, self.OUTER_BORDER_COLOR,
                             pygame.Rect((self.rect.left, self.rect.top),
                                         (self.OUTER_BORDER_SIZE, self.rect.height)))  # left
            pygame.draw.rect(self.surface, self.OUTER_BORDER_COLOR,
                             pygame.Rect((self.rect.right - self.OUTER_BORDER_SIZE, self.rect.top),
                                         (self.OUTER_BORDER_SIZE, self.rect.height)))  # right
