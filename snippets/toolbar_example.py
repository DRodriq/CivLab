import pygame

class Toolbar:
    def __init__(self, screen_width, toolbar_height, button_image=None):
        self.screen_width = screen_width
        self.toolbar_height = toolbar_height
        self.rect = pygame.Rect(0, 0, screen_width, toolbar_height)
        self.button_image = button_image  # Optional image for Menu button

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 215, 0), self.rect)  # Gold color 
        if self.button_image:
            # Double the size of the button image
            scaled_button_image = pygame.transform.scale2x(self.button_image)  
            screen.blit(scaled_button_image, (self.rect.right - scaled_button_image.get_width(), 
                                              (self.rect.height - scaled_button_image.get_height()) // 2))


    def handle_click(self, pos):
        # Check if click is within Menu button area (if image provided)
        if self.button_image and self.button_image.get_rect(topleft=(self.rect.right - self.button_image.get_width(), 
                                                                        (self.rect.height - self.button_image.get_height()) // 2)).collidepoint(pos):
            # Handle Menu button click (Open Menu logic)
            return True  # Indicate Menu button clicked
        return False  # No button clicked
  
pygame.init()

screen_width = 800
screen_height = 600

toolbar_height = 30 * 1.5  # 50% wider
toolbar = Toolbar(screen_width, toolbar_height)

screen = pygame.display.set_mode((screen_width, screen_height))

# Load button image (optional)
menu_button_image = pygame.image.load("/home/drodriq/Source/Python/CivLab_2/assets/civlab_logo.png").convert_alpha()  # Replace with your image path
toolbar.button_image = menu_button_image

# Draw toolbar
toolbar.draw(screen)

# Handle events
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check for click on toolbar
            if toolbar.rect.collidepoint(event.pos):
                if toolbar.handle_click(event.pos):
                    # Menu button clicked, open your menu logic here
                    pass

        # Update display
        pygame.display.flip()