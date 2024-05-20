import pygame
import math
import random
from config import constants
import civlab_events

class Tile:  # Base Tile Class
    def __init__(self, image, iso_x_offset=0, iso_y_offset=0):
        self.image = pygame.image.load(image)
        self.iso_x_offset = iso_x_offset
        self.iso_y_offset = iso_y_offset
        
        # calculate top left coordinate when drawing the tile
        self.rect = self.image.get_rect()
        self.rect.x -= self.iso_x_offset
        self.rect.y -= self.iso_y_offset

    def draw(self, screen, x, y):
        screen.blit(self.image, (x + self.iso_x_offset, y + self.iso_y_offset))

class GrassTile(Tile):
    def __init__(self):
        super().__init__(constants.GRASS_TILE_ASSET_PATH, iso_x_offset=0, iso_y_offset=0)
    
class ForestTile(Tile):
    def __init__(self):
        super().__init__(constants.FOREST_TILE_ASSET_PATH, iso_x_offset=0, iso_y_offset=0)

class WaterTile(Tile):
    def __init__(self):
        super().__init__(constants.WATER_TILE_ASSET_PATH, iso_x_offset=0, iso_y_offset=5)

class MountainTile(Tile):
    def __init__(self):
        super().__init__(constants.MOUNTAIN_TILE_ASSET_PATH, iso_x_offset=0, iso_y_offset=-10)

class DesertTile(Tile):
    def __init__(self):
        super().__init__(constants.DESERT_TILE_ASSET_PATH, iso_x_offset=0, iso_y_offset=0)

# Available Tile Types
tile_types = [GrassTile, WaterTile, ForestTile, MountainTile]  # Add more as needed
# Available Tile Types and Their Weights
tile_weights = {
    GrassTile: 45,
    WaterTile: 10,  
    ForestTile: 45,
    MountainTile: 10,
    DesertTile: 10
}

class Game():
    def __init__(self):
        self.generate_random_game_board()
        self.game_surface = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.camera_x, self.camera_y = 0, 0
        self.tile_width, self.tile_height = GrassTile().rect.size
        self.iso_angle = 0

        self.event_registry = (
            pygame.MOUSEMOTION,
            pygame.MOUSEBUTTONDOWN,
            pygame.KEYDOWN
        )


    def generate_random_game_board(self):
        """Generates a 2D game board with random tiles based on weights."""
        self.board = []
        for _ in range(constants.BOARD_HEIGHT):
            row = []
            for _ in range(constants.BOARD_WIDTH):
                tile_type = random.choices(list(tile_weights.keys()), weights=tile_weights.values())[0]  
                row.append(tile_type()) 
            self.board.append(row)
        return
    

    def handle_events(self):
        # Keyboard Panning
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.camera_x -= constants.GAME_CAMERA_PAN_SPEED
        if keys[pygame.K_RIGHT]:
            self.camera_x += constants.GAME_CAMERA_PAN_SPEED
        if keys[pygame.K_UP]:
            self.camera_y -= constants.GAME_CAMERA_PAN_SPEED
        if keys[pygame.K_DOWN]:
            self.camera_y += constants.GAME_CAMERA_PAN_SPEED

        # Keyboard Menu
        if keys[pygame.K_ESCAPE]:
            my_event = pygame.event.Event(civlab_events.OPEN_MENU)
            pygame.event.post(my_event)

        # Mouse Panning
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x < constants.GAME_CAMERA_MOUSE_PAN_THRESHOLD:
            self.camera_x -= constants.GAME_CAMERA_PAN_SPEED
        if mouse_x > constants.SCREEN_WIDTH - constants.GAME_CAMERA_MOUSE_PAN_THRESHOLD:
            self.camera_x += constants.GAME_CAMERA_PAN_SPEED
        if mouse_y < constants.GAME_CAMERA_MOUSE_PAN_THRESHOLD:
            self.camera_y -= constants.GAME_CAMERA_PAN_SPEED
        if mouse_y > constants.SCREEN_HEIGHT - constants.GAME_CAMERA_MOUSE_PAN_THRESHOLD:
            self.camera_y += constants.GAME_CAMERA_PAN_SPEED

        if(self.camera_x < constants.MIN_CAMERA_X):
            self.camera_x = constants.MIN_CAMERA_X
        if(self.camera_x > constants.MAX_CAMERA_X):
            self.camera_x = constants.MAX_CAMERA_X
        if(self.camera_y < constants.MIN_CAMERA_Y):
            self.camera_y = constants.MIN_CAMERA_Y
        if(self.camera_y > constants.MAX_CAMERA_Y):
            self.camera_y = constants.MAX_CAMERA_Y

    def draw(self, screen):
        self.game_surface.fill((0, 0, 0))  # Clear the screen

        for y, row in enumerate(self.board):
            for x, tile in enumerate(row):
                # Isometric projection
                cart_x = (x - y) * (self.tile_width / 2)
                cart_y = (x + y) * (self.tile_height / 4)
                iso_x = cart_x * math.cos(self.iso_angle) - cart_y * math.sin(self.iso_angle) +250
                iso_y = cart_x * math.sin(self.iso_angle) + cart_y * math.cos(self.iso_angle)

                # Adjust tile position based on camera
                iso_x -= self.camera_x
                iso_y -= self.camera_y

                tile.draw(self.game_surface, iso_x, iso_y)
        screen.blit(self.game_surface, (0, constants.TOOLBAR_HEIGHT))


    def draw_agents(self, screen, locs):
        for loc in locs:
            screen.blit(constants.AGENT_ASSET_PATH, (loc.x, loc.y))