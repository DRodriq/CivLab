from config import constants
from abm import agent
import random

class Model():
    def __init__(self):
        self.agents = []

    def init_agents(self):
        for i in constants.NUM_STARTING_AGENTS:
            loc = (random.randint(0, constants.BOARD_WIDTH), random.randint(0, constants.BOARD_HEIGHT))
            self.agents.append(agent.Agent(loc))

    def process(self):
        for agent in self.agents:
            agent.move(random.randint(0, 1), random.randint(0, 1))

    def get_locations(self):
        return((agent.location[0], agent.location[1]) for agent in self.agents)