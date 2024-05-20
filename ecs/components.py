import esper
import pygame
class Size:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Renderable:
    def __init__(self, image):
        self.image = image

class Clickable:
    def __init__(self, on_click=None):
        self.on_click = on_click  # Store a callback function
