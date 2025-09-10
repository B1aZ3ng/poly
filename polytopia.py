import random
import gymnasium as gym
from terrain import *
from gymnasium import spaces
from buildings import City
from players import Player
GRID_SIZE = 8

    
class PolytopiaEnv(gym.Env):
    def __init__(self):
        super(PolytopiaEnv, self).__init__()
        self.grid = [[Field() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.players = [Player("P1"),Player("P2")]
        self.current_player = 0
        
        self.action_space = spaces.Discrete(GRID_SIZE * GRID_SIZE * 2)
        self.observation_space = spaces.Box(low=0, high=3, shape=(GRID_SIZE, GRID_SIZE), dtype=int)

        self.init_map_test() #temp
    def init_map_test(self): #temp
        self.grid[1][1].building =  City(self.players[0])
        self.grid[GRID_SIZE-2][GRID_SIZE-2].building = City(self.players[1])
    
    def render(self):
        for y in range(GRID_SIZE):
            row = ""
            for x in range(GRID_SIZE):
                tile = self.grid[x][y]
                if tile.building:
                    row += "C1 " if tile.building.owner == self.players[0] else "C2 "
                elif tile.troop:
                    row += "W1 " if tile.troop.owner == self.players[0] else "W2 "
                else:
                    row += ".  "
            print(row)
        print("\n")