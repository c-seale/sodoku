import pygame


class Cell:
    CELL_BORDER_SIZE = 1
    CELL_BORDER_COLOR = pygame.Color('BLACK')

    def __init__(self, surface: pygame.Surface, x: int, y: int, width: int, height: int, initial_val: int):
        self.surface = surface
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.value = initial_val
        self.temp_value = None

        if self.value == 0:
            self.editable = False
        else:
            self.editable = True

        self.rect = pygame.Rect(self._x, self._y, self._width, self._height)

    def draw(self):
        pygame.draw.rect(self.surface, self.CELL_BORDER_COLOR, self.rect, self.CELL_BORDER_SIZE)

    def update(self):
        self.draw()
