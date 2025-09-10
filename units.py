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

class Unit:
    def __init__(self,owner,health,attack,defense,movement,atk_range):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.movement = movement
        self.range = atk_range
        self.moves = 0
        self.owner = owner
    def endTurn(): pass
    def canMove(): pass
    def canAttack(): pass


'''
Land Units:
DONE: 
TODO: Warrior, Archer, Defender, Rider, Mind Bender, Swordsman, Catapult, Cloak, Dagger, Knight, Giant
'''
class Land_Unit:
    def __init__ (self,health,attack,defense,movement,atk_range):
        return super().__init__(
            health = 10,
            attack = 2,
            defense = 2,
            movement = 1,
            atk_range = 1
        )
    def canMove():
        pass
        
class Warrior(Land_Unit):
    def __init__(self):
        return super().__init__(
            health = 10,
            attack = 2,
            defense = 2,
            movement = 1,
            atk_range = 1
        )
