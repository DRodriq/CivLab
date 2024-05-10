# Isometric gameboard with pan 

import pygame

pygame.init()

# Game Window Setup
window_width = 1200
window_height = 800
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Game Board")

# Square Asset Loading (Assuming Isometric Image)
square_image = pygame.image.load("/home/drodriq/Source/Python/CivLab/assets/images/tiles/forest.png") 
square_size = 110  # Adjust for desired square size

# Isometric Offset (Experiment for your specific asset)
isometric_offset_x = int(square_size * 0.5)  # Adjust based on your isometric angle
isometric_offset_y = int(square_size * 0.25)  # Adjust based on your isometric angle

# Game Board Parameters
board_width = 20  # Number of squares horizontally
board_height = 20   # Number of squares vertically

# Camera Setup
camera_x = 0
camera_y = 0
camera_speed = 5  # Adjust for desired camera speed


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Camera Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        camera_x -= camera_speed
    if keys[pygame.K_RIGHT]:
        camera_x += camera_speed
    if keys[pygame.K_UP]:
        camera_y -= camera_speed
    if keys[pygame.K_DOWN]:
        camera_y += camera_speed

    screen.fill((255, 255, 255))  # White background

    for row in range(board_height):
        for col in range(board_width):
            # Calculate adjusted position based on isometric angle and camera
            x = col * square_size - (row * isometric_offset_x) - camera_x
            y = row * isometric_offset_y - camera_y
            # Check if square is within the visible window
            if -square_size < x < window_width and -square_size < y < window_height:
                screen.blit(square_image, (x, y))

                # Draw the settler image at position (3, 3)
                if row == 3 and col == 3:
                    screen.blit(settler_image, (x, y))

    pygame.display.flip()  # Update the display

pygame.quit()







square_image = pygame.image.load("/home/drodriq/Source/Python/CivLab/assets/images/tiles/forest.png") 
