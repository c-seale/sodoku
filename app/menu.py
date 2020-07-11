from typing import Tuple

import pygame


class Menu:
    NO_CLICK = 0
    BTN_CHECK_SOLUTION = 1

    def __init__(self, surface: pygame.Surface):
        self._surface = surface
        self.rect = pygame.Rect((0, 0), (surface.get_width(), surface.get_height()))

        # Position & Size button to check board solution
        self._rect_btn_check_solution = pygame.Rect(self.rect.midtop, (100, 50))
        self._rect_btn_check_solution.center = self.rect.center

    def click(self, mouse_pos: Tuple[int, int]) -> int:
        # TODO: Animate buttons when clicked
        if self._rect_btn_check_solution.colliderect(pygame.Rect(mouse_pos, (1, 1))):
            return self.BTN_CHECK_SOLUTION
        return self.NO_CLICK

    def update(self):
        self._surface.fill(pygame.Color('GRAY'))
        self.update_btn_check_solution()

    def update_btn_check_solution(self):
        pygame.draw.rect(self._surface, pygame.Color('WHITE'), self._rect_btn_check_solution)  # btn bg color
        pygame.draw.rect(self._surface, pygame.Color('BLACK'), self._rect_btn_check_solution, 2)  # btn outline

        font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
        rendered_font = font.render('Check', True, pygame.Color('BLACK'))
        self._surface.blit(rendered_font, rendered_font.get_rect(center=self._rect_btn_check_solution.center))
