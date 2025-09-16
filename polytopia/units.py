from collections import deque
'''
NOTE: movement: https://www.youtube.com/watch?v=gJOZZbipsTA
TODO: currently using tile.troop.owner != self.owner to check for if attackable
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
        self.type = None
        self.health = health
        self.attack = attack
        self.defense = defense
        self.movement = movement
        self.range = atk_range
        self.moves = 0
        self.owner = owner
        self.env = env
    def endTurn(): pass #resets the character after turn ends


    def getMoves(self,xFrom,yFrom): 
        steps = self.movement
        queue = deque([(xFrom,yFrom,steps)])
        # bfs function
        moves = [] #list for all possible moves
        for _ in range (steps):
            for i in range (len(queue)):
                x,y,steps = queue.popleft()
                for xC,yC in directions: #change in x and y
                    if self.env.inGrid(x+xC,y+yC): # check if its in the fking grid
                        stepsLeft = self.canMoveTo(x,y,x+xC,y+yC,steps) 
                        if int(stepsLeft) > 0: # will return None if cant move to, also round down cuz poly movement is weird
                            # Only if >0 becuase if 0, dont need to add to queue
                            queue.append((x+xC,y+yC,stepsLeft))

                        if int(stepsLeft) >= 0:
                            #>= 0 becuase if it is 0, it still counts
                            if (x,y) not in moves: #add to moves if not in
                                moves.append(x,y)
        return moves    
    def canAttack(owner): #peace treaties and stuff
        pass

    def getAttack(self,x,y):
        attacks = [] #list for all possible attack 
        for xC in range (-self.range,self.range+1):
            for yC in range (-self.range,self.range+1):
                tile = self.env.grid[x+xC][y+yC]
                if tile.troop and tile.troop.owner != self.owner:
                    if tile.troop.type == "Cloaker":#checks for cloakers
                        if tile.troop.seen == True: #if the cloakers seen than can attack
                            attacks.append((x+xC,y+yC))
                    else: #not cloaker
                        attacks.append((x+xC,y+yC))

                        
    

    def inZoneOfControl(self,x,y):# searches adjacent boxes to see theres a troop
        for xC,yC in directions:
            if self.env.inGrid(x+xC,y+yC) and self.env.grid[x+xC][y+yC].troop: 
                if self.env.grid[x+xC][y+yC].troop.owner != self.owner: # if owner is different
                  return True
        return False  
    
   
    



'''
Land Units:
DONE: 
TODO: Warrior, Archer, Defender, Rider, Mind Bender, Swordsman, Catapult, Cloak, Dagger, Knight, Giant
'''

class Land_Unit(Unit):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    #checks if you can move each step and 
    def canStepTo(self,xFrom,yFrom,xTo,yTo,steps):
        if steps == 0:
            return None #just edge case if i forget to do stuff
        startTile = self.env.grid[xFrom][yFrom]
        endTile = self.env.grid[xTo][yTo]
        
        if endTile.troop: #checks if there alr is a troop
            return None 

        endInZoneCtrl = self.inZoneOfControl(xTo,yTo) 
        
        isRoad = startTile.road and endTile.road # check if roads connect
        
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
    def __init__(self):
        return super().__init__(
            health = 10,
            attack = 2,
            defense = 2,
            movement = 1,
            atk_range = 1
        )
