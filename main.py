import pygame
import sys
import config.constants as constants
import ui.game_menu as game_menu
import ui.splash as splash
import events
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
        self.screen = pygame.display.set_mode(
            (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        )
        self.states = {
            "START": self.handle_startup,
            "QUIT": self.handle_quit,
            "PLAY": self.handle_play,
            "MENU": self.handle_menu
        }
        self.state = "START"
        

    def run(self):
        while True:
            self.check_events()
            self.states[self.state]()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click = True


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
                if event.type == events.START_IT_UP:
                    self.state = "MENU"
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                    startup_screen.start_button.handle_event(event)
                startup_screen.draw(self.screen)
            #    pygame.display.flip()

    def handle_menu(self):
        print("AT MENU!")
        menu = game_menu.GameMenu(self.screen, self.button_font)
        while self.state == "MENU":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "QUIT"

            self.screen.fill(constants.COLORS['off-black'])

            pygame.display.flip()


    def handle_play(self):
        SQUARE_SIZE = 50
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.screen.fill(constants.COLORS['black'])
        pygame.draw.rect(self.screen, constants.COLORS['white'], (mouse_x, mouse_y, SQUARE_SIZE, SQUARE_SIZE))
        pygame.display.flip()


if __name__ == "__main__":
    controller = ApplicationController()
    controller.run()