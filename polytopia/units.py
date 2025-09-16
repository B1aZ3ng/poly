from collections import deque
'''

Units
Information	
Units, List of Units, Unit Skills, Super Unit, Disband
Land	
Warrior, Archer, Defender, Rider, Mind Bender, Swordsman, Catapult, Cloak, Dagger, Knight, Giant
Naval	
Raft, Rammer, Scout, Bomber, Juggernaut, Dinghy, Pirate
Aquarion	
Tridention, Shark, Jelly, Puffer, Crab
∑∫ỹriȱŋ	
Polytaur, Dragon Egg, Baby Dragon, Fire Dragon
Polaris	
Ice Archer, Battle Sled, Mooni, Ice Fortress, Gaami
Cymanti	
Hexapod, Kiton, Phychi, Shaman, Exida, Raychi, Doomux, Centipede
Other	
Battleship, Boat, Bunny, Bunta, Guard Tower, Navalon, Scout (Removed), Ship
'''
global directions

directions = (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)
class Unit:
    def __init__(self,owner,health,attack,defense,movement,atk_range,env):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.movement = movement
        self.range = atk_range
        self.moves = 0
        self.owner = owner
        self.env = env
    def endTurn(): pass
    def canMove(self,xFrom,yFrom,xTo,yTo): pass
        # need to include trees,mountains and roads
    
    def canAttack(self,xFrom,yFrom,xTo,yTo):
        return abs(xFrom-xTo) <= self.attack and abs(yFrom-yTo) <= self.attack
    def canMoveInTerrain(): pass

'''
Land Units:
DONE: 
TODO: Warrior, Archer, Defender, Rider, Mind Bender, Swordsman, Catapult, Cloak, Dagger, Knight, Giant
'''

class Land_Unit(Unit):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def canMove(self,xFrom,yFrom,xTo,yTo):
        steps = self.movement
        queue = deque([(xFrom,yFrom)])
        # bfs function
        for _ in range (steps):
            for i in range (len(queue)):
                x,y = queue.popleft()
                for dir in directions:
                    x_,y_ = dir#change in x and y
                    x_ += x
                    y_ += y
                    match self.env.grid[x_][y_].terrain.type:
                        case "Field":
                            return True
                        case "_":
                            return False #TODO
                        
                    if x_ == xTo and y_ == yTo

        
    def canMoveInTerrain(terrainType):
            
                
        
        
        
class Warrior(Land_Unit):
    def __init__(self):
        return super().__init__(
            health = 10,
            attack = 2,
            defense = 2,
            movement = 1,
            atk_range = 1
        )
