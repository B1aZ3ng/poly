''' Tile types '''

class Terrain:
    def __init__(self,type_,env):
        self.type = type_
        self.canResource = None
        self.canBuild = None
        self.env = env

class Field (Terrain):
    def __init__(self,env):
        super().__init__("Field",env = env)


''' Resources on Tile '''

class TileResource:
    def __init__ (self,type:str,requires:any,harvestCost:int,harvestResult:int):
        self.type = type
        self.requires = requires
        self.harvestCost = harvestCost
        self.harvestResult = harvestResult

