import pygame
from config import constants

class Button:
    def __init__(self, x, y, text, font, action=None):
        self.rect = pygame.Rect(x, y, constants.MENU_BUTTON_WIDTH, constants.MENU_BUTTON_HEIGHT)  # Button area
        self.text = text
        self.color = constants.MENU_BUTTON_COLOR
        self.font = font
        self.action = action
        self.hover = True

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, constants.MENU_BUTTON_TEXT_COLOR)  # black text
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = constants.MENU_BUTTON_HOVER_COLOR
            else:
                self.color = constants.MENU_BUTTON_COLOR
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.on_click()

    def on_click(self):
        if self.action:
            self.action()
        else:
            print(f"Option {self.text.split()[-1]} was selected!")