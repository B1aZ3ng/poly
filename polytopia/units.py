from collections import deque
'''
NOTE: movement: https://www.youtube.com/watch?v=gJOZZbipsTA
TODO: currently using tile.unit.owner != self.owner to check for if attackable
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

class Unit:
    def __init__(self,owner,health,attack,defense,movement,atk_range,env):
        self.type = None
        self.health = health
        self.max_health = health
        self.atk = attack
        self.defense = defense
        self.movement = movement
        self.range = atk_range
        self.moves = 0
        self.owner = owner
        self.env = env
        self.moved = True
        self.defense_bonus = 1
    
    def endTurn(self):  #resets the character after turn ends
        self.moved = False

    # def getMoves(self): 
    #     steps = self.movement
    #     queue = deque([(self.x,self.y,steps)])
    #     # bfs function
    #     moves = [] #list for all possible moves
    #     for _ in range (steps):
    #         for i in range (len(queue)):
    #             x,y,steps = queue.popleft()
    #             for xC,yC in directions: #change in x and y
    #                 xN,yN = x+xC, y+yC
    #                 if self.env.inBounds(xN,yN): # check if its in the fking grid
    #                     stepsLeft = self.canStepTo(x,y,xN,yN,steps) 
    #                     if not stepsLeft: #check it isnt None
                            
    #                         if int(stepsLeft) > 0: # will return None if cant move to, also round down cuz poly movement is weird
    #                             # Only if >0 becuase if 0, dont need to add to queue
    #                             queue.append((xN,yN,stepsLeft))

    #                         if int(stepsLeft) >= 0:
    #                             #>= 0 becuase if it is 0, it still counts
    #                             if (xN,yN) not in moves: #add to moves if not in
    #                                 moves.append((xN,yN))
    #     return moves  
    

      
    # def canMove(self,xTo,yTo):
    #     moves  = self.getMoves()
    #     return (xTo,yTo) in moves and not self.moved #if move is valid and unit hasnt moved
    
    
    # def getAttacks(self,x,y):
    #     attacks = [] #list for all possible attack 
    #     for xC in range (-self.range,self.range+1):
    #         for yC in range (-self.range,self.range+1):
    #             tile = self.env.board[x+xC][y+yC]
    #             if tile.isUnit():
    #                 attacks.append((x+xC,y+yC))
    #     return attacks

    # def canAttack(self,xTo,yTo): #peace treaties and stuff
    #     moves  = self.getAttacks(self.x,self.y)
    #     return (xTo,yTo) in moves

    
                        
    

    
    

'''
Land Units:
DONE: 
TODO: Warrior, Archer, Defender, Rider, Mind Bender, Swordsman, Catapult, Cloak, Dagger, Knight, Giant
'''

class LandUnit(Unit):
    
    # no init statement hopefully

    #checks if you can move each step and 
    def stepsCalc(self,startTile,endTile,steps):
        if steps == 0:
            return None #just edge case if i forget to do stuff
        
        if endTile.unit: #checks if there alr is a unit
            return None 
        
        
        road = startTile.isRoad() and endTile.isRoad()
            
        
        match endTile.terrain.type:
            case "Field":
                if road:
                    return steps - 0.5
                else:
                    return steps - 1
            case "Forest":
                if road:
                    return steps - 0.5
                else:
                    return 0
            
            case _: # returns error if i forget smth
                return SyntaxError("I forgot to add type{endTile.terrain.type} to movement for {self.type}")

class ProjUnit(Unit): #shoots projectiles
    pass
class MeleeUnit(Unit):
    pass


class Warrior(LandUnit,MeleeUnit):
    def __init__(self,coord,owner,env):
        return super().__init__(
            owner = owner,
            health = 10,
            attack = 2,
            defense = 2,
            movement = 1,
            atk_range = 1,
            env = env
        )
