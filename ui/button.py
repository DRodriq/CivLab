import pygame
from config import constants

class Button:
    def __init__(self, x, y, text, font, _registry=None, action=None, color=None, _hover_color=None):
        self.rect = pygame.Rect(x, y, constants.MENU_BUTTON_WIDTH, constants.MENU_BUTTON_HEIGHT)  # Button area
        self.text = text
        self.font = font
        self.action = action
        if _registry is None:
            self.event_registry = (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN)
        else:
           self.event_registry = _registry
        if _hover_color is None:
            self.hover_color = constants.DEFAULT_HOVER_COLOR
        else:
            self.hover_color = _hover_color
        if color is None:
            self.default_color = constants.DEFAULT_BUTTON_COLOR
        else:
            self.default_color = color

        self.color = self.default_color


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, constants.MENU_BUTTON_TEXT_COLOR)  # black text
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)


    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = self.hover_color
            else:
                self.color = self.default_color
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.on_click()


    def on_click(self):
        if self.action:
            self.action()
        else:
            print(f"Option {self.text.split()[-1]} was selected!")