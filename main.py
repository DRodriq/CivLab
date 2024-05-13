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
import threading
import multiprocessing
import queue
import time

import config.constants as constants
import ui.menu as menu
import ui.splash as splash
import ui.game as game
import ui.toolbar as toolbar

import civlab_events

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

        self.the_game = game.Game()
        self.game_toolbar = toolbar.Toolbar()

        self.main_event_registry = (
            pygame.QUIT,
            civlab_events.START_IT_UP,
            civlab_events.PLAY_GAME,
            civlab_events.OPEN_MENU,
            civlab_events.CLOSE_MENU,
        )
        self.state = "START"
        

    def run(self):
        while True:
            self.states[self.state]()


    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.change_state("QUIT")
        elif event.type == civlab_events.START_IT_UP:
            self.change_state("MENU")
        elif event.type == civlab_events.PLAY_GAME:
            self.change_state("PLAY")
        elif event.type == civlab_events.OPEN_MENU:
            self.change_state("MENU")
        elif event.type == civlab_events.CLOSE_MENU:
            self.change_state("PLAY")


    def change_state(self, new_state):
        '''Wrapper class in case this gets more complex'''
        self.state = new_state


    def handle_quit(self):
        pygame.quit()
        sys.exit()


    def handle_startup(self):
        startup_screen = splash.SplashScreen()
        startup_screen.draw(self.screen)
        while self.state == "START":
            for event in pygame.event.get():
                if event.type in self.main_event_registry:
                    self.handle_event(event)
                elif event.type in startup_screen.event_registry:
                    startup_screen.handle_event(event)
                startup_screen.draw(self.screen)
            pygame.display.flip()


    def handle_menu(self):
        game_menu = menu.Menu()
        while self.state == "MENU":
            for event in pygame.event.get():
                if event.type in self.main_event_registry:
                    self.handle_event(event)
                elif event.type in game_menu.event_registry:
                    game_menu.handle_event(event)
            game_menu.draw(self.screen)
            pygame.display.flip()


    def handle_play(self):
        self.game_toolbar.draw(self.screen)
        while self.state == "PLAY":
            try:
                result = data_queue.get()  # Get data from the queue
                print(f"UI received data: {result}")
            except queue.Empty:
                pass
            for event in pygame.event.get():
                if event.type in self.main_event_registry:
                    self.handle_event(event)
                if event.type in self.game_toolbar.event_registry:
                    self.game_toolbar.handle_event(event)

            self.the_game.handle_events()  # for performance reasons, we do not want to call this in the for loop!
            self.the_game.draw(self.screen)
            pygame.display.flip()


def intense_task(shared_2d_array):
    i = 0
    while True:
        # Simulate a computationally intensive task
        time.sleep(1)  # Replace with your actual processing
        i+=1


if __name__ == "__main__":
    import numpy as np
    import random
    shared_2d_array = np.random.randint((100,100))
    data_queue = multiprocessing.Queue()

    process = multiprocessing.Process(target=intense_task, args=(shared_2d_array,))
    process.start()

    controller = ApplicationController()
    controller.run()

    