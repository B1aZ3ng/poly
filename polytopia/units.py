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

directions = (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)
class Unit:
    def __init__(self,coord,owner,health,attack,defense,movement,atk_range,env):
        self.type = None
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.movement = movement
        self.range = atk_range
        self.moves = 0
        self.owner = owner
        self.env = env
        self.moved = True
        self.x,self.y = coord
    
    
    def endTurn(self):  #resets the character after turn ends
        self.moved = False

    def getMoves(self): 
        steps = self.movement
        queue = deque([(self.x,self.y,steps)])
        # bfs function
        moves = [] #list for all possible moves
        for _ in range (steps):
            for i in range (len(queue)):
                x,y,steps = queue.popleft()
                for xC,yC in directions: #change in x and y
                    xN,yN = x+xC, y+yC
                    if self.env.inBounds(xN,yN): # check if its in the fking grid
                        stepsLeft = self.canStepTo(x,y,xN,yN,steps) 
                        if not stepsLeft: #check it isnt None
                            
                            if int(stepsLeft) > 0: # will return None if cant move to, also round down cuz poly movement is weird
                                # Only if >0 becuase if 0, dont need to add to queue
                                queue.append((xN,yN,stepsLeft))

                            if int(stepsLeft) >= 0:
                                #>= 0 becuase if it is 0, it still counts
                                if (xN,yN) not in moves: #add to moves if not in
                                    moves.append((xN,yN))
        return moves  
    

      
    def canMove(self,xTo,yTo):
        moves  = self.getMoves()
        return (xTo,yTo) in moves and not self.moved #if move is valid and unit hasnt moved
    
    
    def getAttacks(self,x,y):
        attacks = [] #list for all possible attack 
        for xC in range (-self.range,self.range+1):
            for yC in range (-self.range,self.range+1):
                tile = self.env.board[x+xC][y+yC]
                if tile.unit and tile.unit.owner != self.owner:
                    if tile.unit.type == "Cloaker":#checks for cloakers
                        if tile.unit.seen == True: #if the cloakers seen than can attack
                            attacks.append((x+xC,y+yC))
                    else: #not cloaker
                        attacks.append((x+xC,y+yC))
        return attacks

    def canAttack(self,xTo,yTo): #peace treaties and stuff
        moves  = self.getAttacks(self.x,self.y)
        return (xTo,yTo) in moves

    def attack(self,xTo,yTo):
        if self.canAttack(xTo,yTo):
            enemy = self.env.board[xTo][yTo].unit
            
        else:
            return SyntaxError("attacking smth that cant be attacked")
                        
    

    def inZoneOfControl(self,x,y):# searches adjacent boxes to see theres a unit
        for xC,yC in directions:
            if self.env.inBounds(x+xC,y+yC) and self.env.board[x+xC][y+yC].unit: 
                if self.env.board[x+xC][y+yC].unit.owner != self.owner: # if owner is different
                  return True
        return False  
    

'''
Land Units:
DONE: 
TODO: Warrior, Archer, Defender, Rider, Mind Bender, Swordsman, Catapult, Cloak, Dagger, Knight, Giant
'''

class Land_Unit(Unit):
    
    # no init statement hopefully

    #checks if you can move each step and 
    def canStepTo(self,xFrom,yFrom,xTo,yTo,steps):
        if steps == 0:
            return None #just edge case if i forget to do stuff
        startTile = self.env.board[xFrom][yFrom]
        endTile = self.env.board[xTo][yTo]
        
        if endTile.unit: #checks if there alr is a unit
            return None 

        endInZoneCtrl = self.inZoneOfControl(xTo,yTo) 
        
        isRoad = startTile.isRoad() and endTile.isRoad() # check if roads connect
        
        match endTile.terrain.type:
            case "Field":
                if endInZoneCtrl:
                    return 0
                if isRoad:
                    return steps - 0.5
                else:
                    return steps - 1
            case _: # returns error if i forget smth
                return SyntaxError("I forgot to add type{endTile.terrain.type} to movement for {self.type}")


class Warrior(Land_Unit):
    def __init__(self,coord,owner,env):
        return super().__init__(
            owner = owner,
            health = 10,
            attack = 2,
            defense = 2,
            movement = 1,
            atk_range = 1,
            env = env,
            coord = coord
        )
