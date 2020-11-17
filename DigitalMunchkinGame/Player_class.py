from Cards_Samlet import Cards
from dataclass import dataclass

@dataclass
class Table:
    armour: Cards = None
    head: Cards = None
    foot: Cards= None 
    hands: cards = None
    hireling: Cards = None


class Player:
    
    def __init__(self, gender, race, handCards = None, tableCards = None, playerClass = None, level = 1, levelTotal = 1, gold = 0): 
        """Initializes the data."""
        
        self.handCards = handCards or []
        self.tableCards = tableCards or Table()
        self.gender = gender
        self.race = race
        self.playerClass = playerClass
        self.level = level
        self.levelTotal = levelTotal
        self.gold = gold
        print("(Initializing {})".format(self.handCards))
        print("(Initializing {})".format(self.tableCards))
        print("(Initializing {})".format(self.gender))
        print("(Initializing {})".format(self.race))
        print("(Initializing {})".format(self.playerClass))
        print("(Initializing {})".format(self.level))
        print("(Initializing {})".format(self.levelTotal))
        print("(Initializing {})".format(self.gold))

    

