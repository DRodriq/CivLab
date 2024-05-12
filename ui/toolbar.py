import pygame
from config import constants

class Toolbar:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, constants.SCREEN_WIDTH, constants.TOOLBAR_HEIGHT)
        self.button_image = None #constants.TOOL_BAR_ICON

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 215, 0), self.rect)
        if self.button_image:
            # Double the size of the button image
            scaled_button_image = pygame.transform.scale2x(self.button_image)  
            self.rect.blit(scaled_button_image, (self.rect.right - scaled_button_image.get_width(), 
                                              (self.rect.height - scaled_button_image.get_height()) // 2))

    def handle_click(self, pos):
        # Check if click is within Menu button area (if image provided)
        if self.button_image and self.button_image.get_rect(topleft=(self.rect.right - self.button_image.get_width(), 
                                                                        (self.rect.height - self.button_image.get_height()) // 2)).collidepoint(pos):
            return True
        return False
  
