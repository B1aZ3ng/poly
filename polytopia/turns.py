class Turn():
    def __init__(self,player,env):
        self.env = env
        player.stars += player.starsPerRound
        # TODO: once structures added, need to search through all structures and check capturables.
    def endTurn(self):
        for i in range (self.env):
            
