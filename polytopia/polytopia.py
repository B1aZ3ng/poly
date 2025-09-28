import random
import gymnasium as gym

from gymnasium import spaces
from polytopia.terrain import *
from polytopia.buildings import City
from polytopia.players import Player
from polytopia.units import *


class Tile:
    def __init__(self,terrain: Terrain,resource = None):
        self.terrain = terrain
        self.resource = resource
        self.building = None
        self.troop = None
        self.owner = None
        self.road = None #Either "Road", "Bridge","City", or  "Algae" (if i bother to add special troops)
    def isRoad(self): #the function is a bit weird REMEMBER TO USE IT INSTEAD OF getting .road
        return self.road or (self.building and self.building.type == "City" )


class PolytopiaEnv(gym.Env):
    
    def __init__(self,GRID_SIZE = 8):
        self.GRID_SIZE = GRID_SIZE
        super(PolytopiaEnv, self).__init__() #initialises the grid
        self.grid = [[Tile(Field(self)) for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]
        self.players = [Player("P1"),Player("P2")]
        self.current_player = 0
        self.action_space = spaces.Discrete(self.GRID_SIZE * self.GRID_SIZE * 2)
        self.observation_space = spaces.Box(low=0, high=3, shape=(self.GRID_SIZE, self.GRID_SIZE), dtype=int)

        self.init_map_test() #temp
        
    def init_map_test(self): #temp
        self.grid[1][1].building = City(self.players[0],self)
        self.grid[self.GRID_SIZE-2][self.GRID_SIZE-2].building = City(self.players[1],self)

        self.grid[1][1].troop = Warrior(self.players[0],self)
        self.grid[self.GRID_SIZE-2][self.GRID_SIZE-2].troop = Warrior(self.players[1],self)
    
    def render(self):
        for y in range(self.GRID_SIZE):
            row = ""
            for x in range(self.GRID_SIZE):
                tile = self.grid[x][y]
                if tile.building and tile.building.type == "City":
                    row += "C1" if tile.building.owner == self.players[0] else "C2"
                else:
                    row+=". "
                if tile.troop:
                    row += "W1" if tile.troop.owner == self.players[0] else "W2"
                else:
                    row += "  "
                row += "  "
                
            print(row)
        print("\n")

    def inGrid(self,x,y):# i will definately forget to put this where i need it
        return not (x < 0 or x >= self.GRID_SIZE or y < 0 or y >= self.GRID_SIZE)

    