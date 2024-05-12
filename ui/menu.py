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

        title_font = pygame.font.Font(None, constants.SPLASH_TITLE_FONT_SIZE)
        button_font = pygame.font.Font(None, constants.SPLASH_START_BUTTON_FONT_SIZE)

        """        
        # Draw the title box
        title_box_width = constants.SCREEN_WIDTH // 4
        title_box_height = constants.SCREEN_HEIGHT // 8
        title_box_x = (constants.SCREEN_WIDTH - title_box_width) // 2
        title_box_y = (constants.SCREEN_HEIGHT - title_box_height) // 2
        pygame.draw.rect(self.menu_surface, constants.COLORS['blue'], (title_box_x, title_box_y, title_box_width, title_box_height))

        # Draw the title text
        title_text = title_font.render("CivLab", True, constants.COLORS['white'])
        title_text_x = (constants.SCREEN_WIDTH - title_text.get_width()) // 2
        title_text_y = (constants.SCREEN_HEIGHT - title_text.get_height()) // 2
        self.menu_surface.blit(title_text, (title_text_x, title_text_y))
        """
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



