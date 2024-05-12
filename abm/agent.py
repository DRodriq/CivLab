
class Agent():
    def __init__(self) -> None:
        self.location = (0, 0)
        self.age = 0
        self.items = []

    def move(self, direction):
        self.location = (self.location[0] + direction[0], self.location[1] + direction[1])