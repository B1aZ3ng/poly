''' Tile types '''
class Tile:
    def __init__(self,type: str,resource = None):
        self.type = None
        self.resource = resource
        self.building = None
        self.troop = None
        self.city = None

class Field (Tile):
    def __init__(self):
        super().__init__(type = "Field")


''' Resources on Tile '''

class TileResource:
    def __init__ (self,type:str,requires:any,harvestCost:int,harvestResult:int):
        self.type = type
        self.requires = requires
        self.harvestCost = harvestCost
        self.harvestResult = harvestResult

