"""
The ApplicationController class is the main entry point for the application. 
It handles the overall application state and flow, including the startup screen, game menu, and gameplay.

The class initializes Pygame, sets up the game screen, and defines the different application states and their corresponding handler methods.
The `run()` method is the main game loop that checks for events and executes the appropriate state handler.

The `handle_startup()` method displays the startup splash screen and waits for the user to click the start button to transition to the game menu.
The `handle_menu()` method displays the game menu, and the `handle_play()` method handles the actual gameplay, 
drawing a square at the mouse position.
"""

import pygame
import sys
import config.constants as constants
import ui.menu as menu
import ui.splash as splash
import ui.gameboard as gameboard
import ui.toolbar as toolbar

import civlab_events
import logging
import logging.config

"""
logging.config.fileConfig('logging.ini')

logger = logging.getLogger('simulationLogger') 
data_logger = logging.getLogger('dataLogger')
"""

class ApplicationController:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        )
        self.states = {
            "START": self.handle_startup,
            "QUIT": self.handle_quit,
            "PLAY": self.handle_play,
            "MENU": self.handle_menu
        }
        self.game_board = gameboard.GameBoard() 
        self.game_toolbar = toolbar.Toolbar()
        self.state = "START"

    def run(self):
        while True:
            self.states[self.state]()
            #pygame.time.wait(constants.FPS)

    def handle_quit(self):
        pygame.quit()
        sys.exit()

    def handle_startup(self):
        startup_screen = splash.SplashScreen()
        startup_screen.draw(self.screen)
        while self.state == "START":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "QUIT"
                if event.type == civlab_events.START_IT_UP:
                    self.state = "MENU"
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                    startup_screen.start_button.handle_event(event)
                startup_screen.draw(self.screen)

                pygame.display.flip()

    def handle_menu(self):
        game_menu = menu.Menu()
        while self.state == "MENU":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "QUIT"
                if event.type == civlab_events.PLAY_GAME:
                    self.state = "PLAY"
                else:
                    for button in game_menu.menu_buttons:
                        button.handle_event(event)
            game_menu.draw(self.screen)

            pygame.display.flip()

    def handle_play(self):
        self.game_board.draw(self.screen)
        self.game_toolbar.draw(self.screen)
        while self.state == "PLAY":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "QUIT"
                if event.type == civlab_events.OPEN_MENU:
                    self.state = "MENU"
            self.game_board.check_game_events()
            self.game_board.draw(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    controller = ApplicationController()
    controller.run()