import pygame
from config import constants
from ui import button
import civlab_events

def b1_action():
    pygame.event.post(pygame.event.Event(civlab_events.PLAY_GAME))


def b2_action():
    pygame.event.post(pygame.event.Event(civlab_events.OPEN_SETTINGS))


def b4_action():
    pygame.event.post(pygame.event.Event(pygame.QUIT))


class Menu:
    def __init__(self):
        self.menu_surface = pygame.Surface((int(constants.SCREEN_WIDTH), constants.SCREEN_HEIGHT))
        self.menu_surface.fill(constants.COLORS['grey'])

        # Load the background image
        background_image = pygame.image.load(constants.MENU_IMAGE)
        background_image = pygame.transform.scale(background_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        
        self.menu_surface.blit(background_image, (0, 0))

        self.event_registry = (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN)

        self.menu_buttons = self.button_factory()

    @staticmethod
    def button_factory():
        button_font = pygame.font.Font(None, constants.SPLASH_START_BUTTON_FONT_SIZE)
        y_coordinates = [constants.MENU_BUTTON_ORIGIN[1] + (x*constants.MENU_BUTTON_SPACING_Y) for x in range(5)]
        button_events = (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN)
        menu_buttons = [
            button.Button(constants.MENU_BUTTON_CENTER_X, y_coordinates[0], "Play", button_font, button_events, b1_action),
            button.Button(constants.MENU_BUTTON_CENTER_X, y_coordinates[1], "Settings", button_font, button_events, b2_action),
            button.Button(constants.MENU_BUTTON_CENTER_X, y_coordinates[2], "About", button_font, button_events),
            button.Button(constants.MENU_BUTTON_CENTER_X, y_coordinates[3], "Quit", button_font, button_events, b4_action)
        ]
        return menu_buttons


    def handle_event(self, event):
        for button in self.menu_buttons:
            if event.type in button.event_registry:
                button.handle_event(event)


    def draw(self, screen):
        for button in self.menu_buttons:
            button.draw(self.menu_surface)
        screen.blit(self.menu_surface, (0,0))



