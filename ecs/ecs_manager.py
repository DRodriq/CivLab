import pygame
import esper
import time
from config import constants
import math
import processors
import components

class ECSManager:
    def __init__(self) -> None:
    # Create Entities

        player1 = esper.create_entity(
            components.Position(100, 100),
            components.Size(50,50),
            components.Clickable(self.on_player_click),
            components.Renderable(pygame.image.load("/home/drodriq/Art/Settler1.png")),
        )
        esper.add_processor(processors.InputProcessor(), priority=0)


    def on_player_click(self, ent):
        print(f"Player clicked! Entity ID: {ent}")


esper.process(1/60)  # Assuming 60 FPS

