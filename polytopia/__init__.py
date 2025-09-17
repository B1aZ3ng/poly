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
        self.unit = None
        self.owner = None
        self.road = None #Either "Road", "Bridge","City", or  "Algae" (if i bother to add special units)
    def isRoad(self): #the function is a bit weird REMEMBER TO USE IT INSTEAD OF getting .road
        return self.road or (self.building and self.building.type == "City" )

class PolytopiaEnv(gym.Env):
    
    def __init__(self,BOARD_SIZE = 8):
        self.BOARD_SIZE = BOARD_SIZE
        super(PolytopiaEnv, self).__init__() #initialises the board
        self.board = [[Tile(Field(self)) for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.players = [Player("P1"),Player("P2")]
        self.current_player = 0
        self.action_space = spaces.Discrete(self.BOARD_SIZE * self.BOARD_SIZE * 2)
        self.observation_space = spaces.Box(low=0, high=3, shape=(self.BOARD_SIZE, self.BOARD_SIZE), dtype=int)

        self.init_map_test() #temp
    
    
    def init_map_test(self): #temp
        self.board[1][1].building = City(self.players[0],self)
        self.board[self.BOARD_SIZE-2][self.BOARD_SIZE-2].building = City(self.players[1],self)

        self.board[1][1].unit = Warrior((1,1),self.players[0],self)
        self.board[self.BOARD_SIZE-2][self.BOARD_SIZE-2].unit = Warrior((1,1),self.players[1],self)
    
    def render(self):
        for y in range(self.BOARD_SIZE):
            row = ""
            for x in range(self.BOARD_SIZE):
                tile = self.board[x][y]
                if tile.building and tile.building.type == "City":
                    row += "C1" if tile.building.owner == self.players[0] else "C2"
                else:
                    row+=". "
                if tile.unit:
                    row += "W1" if tile.unit.owner == self.players[0] else "W2"
                else:
                    row += "  "
                row += "  "
                
            print(row)
        print("\n")

    def inBounds(self,x,y):# i will definately forget to put this where i need it
        return not (x < 0 or x >= self.BOARD_SIZE or y < 0 or y >= self.BOARD_SIZE)
    
    
