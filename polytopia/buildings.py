class City:
    def __init__(self,owner,env,isCapital=False,level=1):
        self.type = "City"
        self.isCapital = isCapital
        self.level = level
        self.population = 0
        self.owner = owner
        self.env = env
    
class Village(City):
    def __init__(self):
        pass

#class Building:
