'''
TODO: using self.env.board[x+xC][y+yC].unit.owner != self.owner to check 
'''
from polytopia.units import *
from collections import deque

DIRECTIONS = (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)
class Action():
    def __init__(self,env):
        self.command = None
        self.env = env
    '''
    ATTACK
    '''
    def attack (self,xFrom,yFrom,xTo,yTo):
        if self.canAttack(xFrom,yFrom,xTo,yTo): 
            attacker = self.env.board[xFrom,yFrom]
            defender = self.env.unit[xTo,yTo]

            attackForce = attacker.attack * (attacker.health / attacker.maxHealth)
            defenseForce = defender.defense * (defender.health / defender.maxHealth) #* defenseBonus TODO
            totalDamage = attackForce + defenseForce 
            attackResult = round((attackForce / totalDamage) * attacker.attack * 4.5) 
            defenseResult = round((defenseForce / totalDamage) * defender.defense * 4.5)
            
            defender.health -= defenseResult
            if defender.health == 0:
                self.env.board[xTo,yTo].unit = None
                if self.canMove(xFrom,yFrom,xTo,yTo) and issubclass(attacker,MeleeUnit): 
                    self.move(xFrom,yFrom,xTo,yTo)
            else:
                if self.canAttack(xTo,yTo,xFrom,yFrom):
                    attacker.health -= attackResult

    def getAttacks(self,x,y):
        unit = self.env.board[x][y].unit
        attacks = [] #list for all possible attack 
        for xC in range (-unit.range,unit.range+1):
            for yC in range (-unit.range,unit.range+1):
                tile = unit.env.board[x+xC][y+yC]
                if tile.isUnit() and tile.unit.owner != unit.owner:
                    attacks.append((x+xC,y+yC))
        return attacks
                        

    def canAttack (self,xFrom,yFrom,xTo,yTo):
        return (xTo,yTo) in self.getAttacks(xFrom,yFrom)

    '''
    MOVEMENT
    '''
    def move(self,xFrom,yFrom,xTo,yTo):
        if self.canMove(xFrom,yFrom,xTo,yTo):
            #TODO
            pass

    def getMoves(self,x,y): 
        unit = self.env.board[x][y].unit
        steps = unit.movement
        queue = deque([(x,y,steps)])
        # bfs function
        moves = [] #list for all possible moves
        for _ in range (steps):
            for i in range (len(queue)):
                x,y,steps = queue.popleft()
                for xC,yC in DIRECTIONS: #change in x and y
                    xN,yN = x+xC, y+yC
                    if unit.env.inBounds(xN,yN): # check if its in the fking grid
                        startTile = self.env.board[x][y]
                        endTile = self.env.board[xN][yN]
                        stepsLeft = unit.stepsCalc(startTile,endTile,steps)
                        if self.inZoneOfControl(xN,yN,unit):
                            stepsLeft = 0

                        if not stepsLeft: #check it isnt None
                            if int(stepsLeft) > 0: # will return None if cant move to, also round down cuz poly movement is weird
                                # Only if >0 becuase if 0, dont need to add to queue
                                queue.append((xN,yN,stepsLeft))

                            if int(stepsLeft) >= 0:
                                #>= 0 becuase if it is 0, it still counts
                                if (xN,yN) not in moves: #add to moves if not in
                                    moves.append((xN,yN))
        return moves  
    
    def canMove (self,xFrom,yFrom,xTo,yTo):
        return (xTo,yTo) in self.getMoves(xFrom,yFrom)

    def inZoneOfControl(self,x,y,unit):# searches adjacent boxes to see theres a unit
        for xC,yC in DIRECTIONS:
            if self.env.inBounds(x+xC,y+yC) and self.env.board[x+xC][y+yC].isUnit(): 
                if self.env.board[x+xC][y+yC].unit.owner != unit.owner: # if owner is different
                    return True
        return False'