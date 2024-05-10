import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
SQUARE_SIZE = 50
PAN_SPEED = 1

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a surface for the checkerboard
board = pygame.Surface((SQUARE_SIZE * 20, SQUARE_SIZE * 20))

# Draw the checkerboard
for i in range(20):
    for j in range(20):
        color = (255, 255, 255) if (i + j) % 2 == 0 else (0, 0, 0)
        pygame.draw.rect(board, color, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Set up variables for the camera position
camera_x, camera_y = 0, 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the camera
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        camera_x -= PAN_SPEED
    if keys[pygame.K_RIGHT]:
        camera_x += PAN_SPEED
    if keys[pygame.K_UP]:
        camera_y -= PAN_SPEED
    if keys[pygame.K_DOWN]:
        camera_y += PAN_SPEED

    # Wrap the camera position around the board
    camera_x %= board.get_width()
    camera_y %= board.get_height()

    # Blit the board onto the screen at the current camera position
    screen.blit(board, (-camera_x, -camera_y))
    screen.blit(board, (board.get_width() - camera_x, -camera_y))
    screen.blit(board, (-camera_x, board.get_height() - camera_y))
    screen.blit(board, (board.get_width() - camera_x, board.get_height() - camera_y))

    # Update the display
    pygame.display.flip()