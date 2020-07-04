import pygame


class Board:
    INNER_BORDER_SIZE = 3
    INNER_BORDER_COLOR = pygame.Color('BLACK')

    DRAW_OUTER_BORDER = True
    OUTER_BORDER_SIZE = 5
    OUTER_BORDER_COLOR = pygame.Color('BLACK')

    BACKGROUND_COLOR = pygame.Color('LIGHTSALMON4')

    def __init__(self, surface: pygame.Surface, x, y, width, height):
        self.surface = surface
        self.rect = pygame.Rect((x, y), (width, height))

        self.surface.fill(self.BACKGROUND_COLOR)

    def update(self):
        self.draw_major_grid()
        pygame.display.update(self.rect)

    def draw_major_grid(self):
        x_off = self.rect.width // 3
        y_off = self.rect.height // 3

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
