''' Tile types '''

class Terrain:
    def __init__(self,type_):
        self.type = type_
        self.canResource = None
        self.canBuild = None

class Field (Terrain):
    def __init__(self):
        super().__init__("Field")


''' Resources on Tile '''

class TileResource:
    def __init__ (self,type:str,requires:any,harvestCost:int,harvestResult:int):
        self.type = type
        self.requires = requires
        self.harvestCost = harvestCost
        self.harvestResult = harvestResult

