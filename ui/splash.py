import pygame
from config import constants
from ui import button
import events


def start_button_action():
    my_event = pygame.event.Event(events.START_IT_UP)
    pygame.event.post(my_event)


class SplashScreen():
    """
    Represents the splash screen for the CivLab game.

    The SplashScreen class is responsible for drawing the initial splash screen
    that is displayed when the game is launched. It includes a background image,
    a title box with the game title, and a "START" button that triggers the start
    of the game.

    Attributes:
        splash_surface (pygame.Surface): The surface on which the splash screen elements are drawn.
        start_button (Button): The "START" button that triggers the start of the game.

    Methods:
        __init__(): Initializes the SplashScreen object by loading the background image,
                    creating the title box and text, and setting up the start button.
        draw(screen): Draws the splash screen on the given screen surface.
    """

    def __init__(self) -> None:
        self.splash_surface = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

        # Load the background image
        background_image = pygame.image.load(constants.SPLASH_IMAGE)
        background_image = pygame.transform.scale(background_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

        # Set up the title font
        title_font = pygame.font.Font(None, constants.SPLASH_TITLE_FONT_SIZE)
        
        self.splash_surface.blit(background_image, (0, 0))

        # Draw the title box
        title_box_width = int(constants.SCREEN_WIDTH * constants.SPLASH_TITLE_BOX_WIDTH_RATIO)
        title_box_height = int(constants.SCREEN_HEIGHT * constants.SPLASH_TITLE_BOX_HEIGHT_RATIO)
        title_box_x = (constants.SCREEN_WIDTH - title_box_width) // 2 + constants.SPLASH_TITLE_BOX_X_OFFSET
        title_box_y = (constants.SCREEN_HEIGHT - title_box_height) // 4 + constants.SPLASH_TITLE_BOX_Y_OFFSET
        pygame.draw.rect(
            self.splash_surface, constants.SPLASH_TITLE_BOX_COLOR, (title_box_x, title_box_y, title_box_width, title_box_height)
        )

        # Draw the title text
        title_text = title_font.render("CivLab", True, constants.SPLASH_TITLE_FONT_COLOR)
        title_text_x = title_box_x + (title_box_width - title_text.get_width()) // 2 + constants.SPLASH_TITLE_TEXT_X_OFFSET
        title_text_y = title_box_y + (title_box_height - title_text.get_height()) // 2 + constants.SPLASH_TITLE_TEXT_Y_OFFSET
        self.splash_surface.blit(title_text, (title_text_x, title_text_y))

        # Add a start button
        button_font = pygame.font.Font(None, constants.SPLASH_START_BUTTON_FONT_SIZE)
        self.start_button = button.Button(
            constants.SPLASH_START_BUTTON_ORIGIN[0], 
            constants.SPLASH_START_BUTTON_ORIGIN[1], 
            "START", 
            button_font, 
            start_button_action
        )
        self.start_button.draw(self.splash_surface)


    def draw(self, screen):
        screen.blit(self.splash_surface, (0, 0))
        self.start_button.draw(self.splash_surface)
        pygame.display.flip()