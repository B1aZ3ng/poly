from actions import Action
#basically an Action Modifier
class Skill():
    pass

class Dash(Action,Skill):
    def attack(self, xFrom, yFrom, xTo, yTo):
        super().attack(xFrom, yFrom, xTo, yTo)
        self.env.board[xFrom][yFrom].canAttack = True
