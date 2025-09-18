from polytopia.units import Unit
from polytopia import PolytopiaEnv
from collections import deque
DIRECTIONS = (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)



def canMove(self,xFrom,yFrom,xTo,yTo):
    moves  = self.getMoves(xFrom,yFrom)
    return (xTo,yTo) in moves and not self.moved #if move is valid and unit hasnt moved


def getAttacks(self,x,y,ZoC):
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

def canAttack(self,xFrom,yFrom,xTo,yTo): #peace treaties and stuff
    moves  = getAttacks(xFrom,yFrom)
    return (xTo,yTo) in moves


                    


def inZoneOfControl(self,x,y):# searches adjacent boxes to see theres a unit
    for xC,yC in DIRECTIONS:
        if self.env.inBounds(x+xC,y+yC) and self.env.board[x+xC][y+yC].unit: 
            if self.env.board[x+xC][y+yC].unit.owner != self.owner: # if owner is different
                return True
    return False  