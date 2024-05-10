import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.SysFont("Comic Sans MS", 30)

# Render the text
text = font.render("Hello World", True, BLACK)

# Get the rectangle of the text
text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw a black rectangle for the box
    box_rect = pygame.Rect(0, 0, 300, 50)
    box_rect.center = text_rect.center
    pygame.draw.rect(screen, BLACK, box_rect, 2)

    # Blit the text onto the screen
    screen.blit(text, text_rect)

    # Flip the display
    pygame.display.flip()