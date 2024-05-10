
import os

PROJ_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../"

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900

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
ASSET_PATH = PROJ_DIR + "assets/"
SPLASH_IMAGE = ASSET_PATH + "civlab_logo.png"

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
MENU_DIMENSIONS = (SCREEN_WIDTH/4, 0, SCREEN_WIDTH/2, SCREEN_HEIGHT)
MENU_BUTTON_WIDTH = 300
MENU_BUTTON_HEIGHT = 100
MENU_BUTTON_CENTER_X = center = SCREEN_WIDTH / 2 - (MENU_BUTTON_WIDTH/2)

MENU_BUTTON_ORIGIN = (MENU_BUTTON_CENTER_X, 250)
MENU_BUTTON_SPACING_Y = 150

MENU_BUTTON_COLOR = COLORS['white']
MENU_BUTTON_HOVER_COLOR = COLORS['red']
MENU_BUTTON_TEXT_COLOR = COLORS['black']
