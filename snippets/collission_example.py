import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BOX_SIZE = 100

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the boxes
boxes = [
    pygame.Rect(50, 50, BOX_SIZE, BOX_SIZE),
    pygame.Rect(200, 50, BOX_SIZE, BOX_SIZE),
    pygame.Rect(350, 50, BOX_SIZE, BOX_SIZE)
]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the mouse is in any of the boxes
    for i, box in enumerate(boxes):
        if box.collidepoint(mouse_pos):
            print(f"the mouse is in box number {i+1}!")

    # Draw the boxes
    screen.fill((0, 0, 0))
    for box in boxes:
        pygame.draw.rect(screen, (255, 255, 255), box)

    # Update the display
    pygame.display.flip()