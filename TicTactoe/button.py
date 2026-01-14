import pygame
from colors import *

class Button():
    def __init__(self, x, y, width, height, text, color, hover_color, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.font = font

    def draw_button_sets(self, surface):
        # BUTTON SHADOW
        shadow_rect = self.rect.copy()
        shadow_rect.y += 5
        pygame.draw.rect(surface, DARK_GRAY, shadow_rect, border_radius=20)

        # BUTTON AND BORDER
        pygame.draw.rect(surface, self.current_color, self.rect, border_radius=20)  # BUTTON
        pygame.draw.rect(surface, WHITE, self.rect, 1, border_radius=20)  # BORDER

        # TEXT
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def button_update(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color

    def is_clicked(self, mouse_position):
        return self.rect.collidepoint(mouse_position)