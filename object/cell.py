import pygame


class Cell:
    CELL_BORDER_SIZE = 1
    CELL_BORDER_COLOR = pygame.Color('BLACK')
    CELL_SELECTED_BORDER_COLOR = pygame.Color('RED')

    def __init__(self, surface: pygame.Surface, x: int, y: int, width: int, height: int, initial_val: int, bg_color):
        self._surface = surface
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

        self.rect = pygame.Rect(x, y, width, height)

    @property
    def bg_color(self):
        if self.is_selected:
            shaded = (int(self._bg_color.r * 0.75), int(self._bg_color.g * 0.75),
                      int(self._bg_color.b * 0.75), int(self._bg_color.a * 0.75))
            return pygame.Color(*shaded)
        return self._bg_color

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
        pygame.draw.rect(self._surface, self.bg_color, self.rect)  # cell background color
        pygame.draw.rect(self._surface, self.CELL_BORDER_COLOR, self.rect, self.CELL_BORDER_SIZE)  # draw outline

        if self.value and self.value > 0:
            font = pygame.font.SysFont(pygame.font.get_default_font(), 60)
            rendered_font = font.render('{}'.format(self.value), True, self._value_color)
            self._surface.blit(rendered_font, rendered_font.get_rect(center=self.rect.center))

    def update(self):
        self.draw()
