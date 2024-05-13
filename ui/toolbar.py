import pygame
from config import constants
import civlab_events

class Toolbar:
    def __init__(self):
        self.toolbar_dimensions = (constants.SCREEN_WIDTH, constants.TOOLBAR_HEIGHT)
        self.toolbar_surface = pygame.Surface(self.toolbar_dimensions)
        self.toolbar_surface.fill(constants.TOOLBAR_COLOR)

        self.button_image = pygame.image.load(constants.TOOL_BAR_ICON)
        self.button_image = pygame.transform.scale(self.button_image, (self.toolbar_dimensions[1], self.toolbar_dimensions[1]))
        self.button_surface = pygame.Surface(self.button_image.get_size())
        self.button_surface.blit(self.button_image, (0,0))
        self.button_dims = (self.toolbar_dimensions[0] - self.button_image.get_width(), 
                                              (self.toolbar_dimensions[1] - self.button_image.get_height()) // 2)
        self.button_rect = pygame.Rect(self.button_dims, self.button_image.get_size())
        
        self.event_registry = (pygame.MOUSEBUTTONDOWN,)

    def draw(self, screen):
        if self.button_image:
            self.toolbar_surface.blit(self.button_surface, self.button_dims)
        screen.blit(self.toolbar_surface, (0,0))
            
    def handle_event(self, event):
        if self.button_image and self.button_rect.collidepoint(event.pos):
            self.handle_click()

    def handle_click(self):
        pygame.event.post(pygame.event.Event(civlab_events.OPEN_MENU))
  
