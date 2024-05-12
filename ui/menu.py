import pygame
from config import constants
from ui import button
import civlab_events

def b1_action():
    my_event = pygame.event.Event(civlab_events.PLAY_GAME)
    pygame.event.post(my_event)


def b2_action():
    my_event = pygame.event.Event(civlab_events.OPEN_SETTINGS)
    pygame.event.post(my_event)


def b3_action():
    my_event = pygame.event.Event(civlab_events.CLOSE_MENU)
    pygame.event.post(my_event)


class Menu:
    def __init__(self):
        self.menu_surface = pygame.Surface((int(constants.SCREEN_WIDTH), constants.SCREEN_HEIGHT))
        self.menu_surface.fill(constants.COLORS['grey'])

        button_font = pygame.font.Font(None, constants.SPLASH_START_BUTTON_FONT_SIZE)

        # Load the background image
        background_image = pygame.image.load(constants.MENU_IMAGE)
        background_image = pygame.transform.scale(background_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        
        self.menu_surface.blit(background_image, (0, 0))

        # button size 150, 50
        y_coordinates = [constants.MENU_BUTTON_ORIGIN[1] + (x*constants.MENU_BUTTON_SPACING_Y) for x in range(5)]
        self.menu_buttons = [
            button.Button(constants.MENU_BUTTON_CENTER_X, y_coordinates[0], "Start", button_font, b1_action),
            button.Button(constants.MENU_BUTTON_CENTER_X, y_coordinates[1], "Settings", button_font, b2_action),
            button.Button(constants.MENU_BUTTON_CENTER_X, y_coordinates[2], "Option 3", button_font, b3_action),
            button.Button(constants.MENU_BUTTON_CENTER_X, y_coordinates[3], "Option 4", button_font),
        ]

    def draw(self, screen):
        for button in self.menu_buttons:
            button.draw(self.menu_surface)
        screen.blit(self.menu_surface, (0,0))



