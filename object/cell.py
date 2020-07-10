import pygame


class Cell:
    CELL_BORDER_SIZE = 2
    CELL_BORDER_COLOR = pygame.Color('BLACK')
    CELL_SELECTED_BORDER_COLOR = pygame.Color('RED')

    def __init__(self, surface: pygame.Surface, x: int, y: int, width: int, height: int, initial_val: int, bg_color):
        self.surface = surface
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._bg_color = bg_color

        self._value = int(initial_val)
        self.temp_value = None
        self.temp_value2 = None

        self._is_selected = False

        self._is_editable = False
        self._value_color = pygame.Color('BLACK')
        if self.value == 0:
            self._is_editable = True
            self._value_color = pygame.Color('WHITE')

        self.rect = pygame.Rect(self._x, self._y, self._width, self._height)

    @property
    def is_editable(self):
        return self._is_editable

    @property
    def is_selected(self):
        return self._is_selected

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if self.is_editable:
            self._value = val

    def select(self):
        self._is_selected = True

    def deselect(self):
        self._is_selected = False

    def draw(self):
        if self.is_selected:
            border_color = self.CELL_SELECTED_BORDER_COLOR
        else:
            border_color = self.CELL_BORDER_COLOR

        pygame.draw.rect(self.surface, self._bg_color, self.rect)
        self.rect = pygame.draw.rect(self.surface, border_color, self.rect, self.CELL_BORDER_SIZE)

        if self.value and self.value > 0:
            font = pygame.font.SysFont(pygame.font.get_default_font(), 90)
            rendered_font = font.render('{}'.format(self.value), True, self._value_color)
            self.surface.blit(rendered_font, rendered_font.get_rect(center=self.rect.center))

    def update(self):
        self.draw()
