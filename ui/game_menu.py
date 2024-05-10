import pygame
from config import constants
from ui import button
import events

def b1_action():
    my_event = pygame.event.Event(events.PLAY_GAME)
    pygame.event.post(my_event)


def b2_action():
    print("You chose Option 2 - different action!")


def b3_action():
    my_event = pygame.event.Event(events.CLOSE_MENU)
    pygame.event.post(my_event)


class GameMenu:
    def __init__(self, screen, font):
        self.menu_surface = pygame.Surface((int(constants.SCREEN_WIDTH * .66), constants.SCREEN_HEIGHT))
        self.menu_surface.fill(constants.COLORS['grey'])
        screen.blit(self.menu_surface, (0,0))
        # Draw the title box
        title_box_width = constants.SCREEN_WIDTH // 4
        title_box_height = constants.SCREEN_HEIGHT // 8
        title_box_x = (constants.SCREEN_WIDTH - title_box_width) // 2
        title_box_y = (constants.SCREEN_HEIGHT - title_box_height) // 2
        pygame.draw.rect(screen, constants.COLORS['blue'], (title_box_x, title_box_y, title_box_width, title_box_height))

        # Draw the title text
        title_text = font.render("CivLab", True, constants.COLORS['white'])
        title_text_x = (constants.SCREEN_WIDTH - title_text.get_width()) // 2
        title_text_y = (constants.SCREEN_HEIGHT - title_text.get_height()) // 2
        screen.blit(title_text, (title_text_x, title_text_y))

        # button size 150, 50
        y_coordinates = [constants.MENU_BUTTON_ORIGIN[1] + (x*constants.MENU_BUTTON_SPACING_Y) for x in range(5)]
        self.menu_buttons = [
            button.Button(constants.MENU_BUTTON_CENTER_X, y_coordinates[0], "Start", font, b1_action),
            button.Button(constants.MENU_BUTTON_CENTER_X, y_coordinates[1], "Option 2", font),
            button.Button(constants.MENU_BUTTON_CENTER_X, y_coordinates[2], "Option 3", font, b3_action),
            button.Button(constants.MENU_BUTTON_CENTER_X, y_coordinates[3], "Option 4", font),
        ]

        pygame.display.flip()

