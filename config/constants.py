
import os

PROJ_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../"

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900
FPS = 60

COLORS = {
    "black": (0,0,0),
    "white": (255,255,255),
    "red": (255,0,0),
    "green": (0,255,0),
    "blue":(0,0,255),
    "grey": (100,100,100),
    'off-black': (50, 50, 50)
}

# Splash Screen
ASSET_PATH = PROJ_DIR + "assets/images/"
SPLASH_IMAGE = ASSET_PATH + "logo_v2.png"

SPLASH_TITLE_BOX_COLOR = COLORS['black']
SPLASH_TITLE_FONT_COLOR = COLORS['white']
SPLASH_TITLE_FONT_SIZE = 96

SPLASH_TITLE_BOX_WIDTH_RATIO = 0.25  # Title box width as a ratio of the screen width
SPLASH_TITLE_BOX_HEIGHT_RATIO = 0.125  # Title box height as a ratio of the screen height
SPLASH_TITLE_BOX_X_OFFSET = 0  # Horizontal offset for the title box
SPLASH_TITLE_BOX_Y_OFFSET = 0  # Vertical offset for the title box (from the center)

SPLASH_TITLE_TEXT_X_OFFSET = 0  # Horizontal offset for the title text
SPLASH_TITLE_TEXT_Y_OFFSET = 0  # Vertical offset for the title text (from the center of the title box)

SPLASH_START_BUTTON_WIDTH = 300
SPLASH_START_BUTTON_FONT_SIZE = 64
SPLASH_START_BUTTON_ORIGIN = (SCREEN_WIDTH/2 - (SPLASH_START_BUTTON_WIDTH/2), SCREEN_HEIGHT*.65)

# Menu Configs
MENU_IMAGE = ASSET_PATH + "civlab_logo_grayscale_25.png"
MENU_DIMENSIONS = (SCREEN_WIDTH/4, 0, SCREEN_WIDTH/2, SCREEN_HEIGHT)
MENU_BUTTON_WIDTH = 300
MENU_BUTTON_HEIGHT = 100
MENU_BUTTON_CENTER_X = center = SCREEN_WIDTH / 2 - (MENU_BUTTON_WIDTH/2)

MENU_BUTTON_ORIGIN = (MENU_BUTTON_CENTER_X, SCREEN_HEIGHT * .25)
MENU_BUTTON_SPACING_Y = 150

MENU_BUTTON_COLOR = COLORS['white']
MENU_BUTTON_HOVER_COLOR = COLORS['red']
MENU_BUTTON_TEXT_COLOR = COLORS['black']

# Toolbar
TOOLBAR_HEIGHT = 30
TOOL_BAR_ICON = ASSET_PATH + "civlab_logo.png"

# Game Board
BOARD_WIDTH = 50
BOARD_HEIGHT = 50

GAME_CAMERA_PAN_SPEED = (BOARD_HEIGHT/2) +10 # Adjust panning speed
GAME_CAMERA_MOUSE_PAN_THRESHOLD = 25  # Distance from edge to trigger mouse panning
MAX_CAMERA_X, MAX_CAMERA_Y = (1500, 2000)
MIN_CAMERA_X, MIN_CAMERA_Y = (-2500, -300)

GRASS_TILE_ASSET_PATH = ASSET_PATH + "grass.png"
FOREST_TILE_ASSET_PATH = ASSET_PATH + "forest.png"
MOUNTAIN_TILE_ASSET_PATH = ASSET_PATH + "mountain.png"
WATER_TILE_ASSET_PATH = ASSET_PATH + "water.png"
DESERT_TILE_ASSET_PATH = ASSET_PATH + "desert.png"