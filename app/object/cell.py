import pygame


class Cell:
    CELL_BORDER_SIZE = 1
    CELL_BORDER_COLOR = pygame.Color('BLACK')
    EDITABLE_TEXT_COLOR = pygame.Color('#C67171')
    LOCKED_TEXT_COLOR = pygame.Color('#C67171')

    def __init__(self, surface: pygame.Surface, x: int, y: int, width: int, height: int, initial_val: int, bg_color):
        self._surface = surface
        self._bg_color = bg_color

        self._value = initial_val
        self.temp_value = None
        self.temp_value2 = None

        self._is_selected = False
        self._is_editable = True if self.value == 0 else False

        self.rect = pygame.Rect(x, y, width, height)

    @property
    def cell_background_color(self):
        if self.is_selected:
            shaded = (int(self._bg_color.r * 0.75), int(self._bg_color.g * 0.75),
                      int(self._bg_color.b * 0.75), int(self._bg_color.a * 0.75))
            return pygame.Color(*shaded)
        if not self.is_editable:
            shaded = (int(self._bg_color.r * 0.90), int(self._bg_color.g * 0.90),
                      int(self._bg_color.b * 0.90), int(self._bg_color.a * 0.90))
            return pygame.Color(*shaded)
        return self._bg_color

    @property
    def cell_text_color(self):
        if self.is_editable:
            return self.EDITABLE_TEXT_COLOR
        return self.LOCKED_TEXT_COLOR

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
        if self.is_editable:
            self._is_selected = True

    def deselect(self):
        if self.is_editable:
            self._is_selected = False

    def update(self):
        pygame.draw.rect(self._surface, self.cell_background_color, self.rect)  # cell background color
        pygame.draw.rect(self._surface, self.CELL_BORDER_COLOR, self.rect, self.CELL_BORDER_SIZE)  # draw outline

        if self.value and self.value > 0:
            font = pygame.font.SysFont(pygame.font.get_default_font(), 60)

            # Text shadow
            if self.is_editable:
                rendered_shadow_font = font.render('{}'.format(self.value), True, pygame.Color('BLACK'))
                self._surface.blit(rendered_shadow_font,
                                   rendered_shadow_font.get_rect(center=(self.rect.centerx + 2, self.rect.centery + 2)))

            # Text
            rendered_font = font.render('{}'.format(self.value), True, self.cell_text_color)
            self._surface.blit(rendered_font, rendered_font.get_rect(center=self.rect.center))
