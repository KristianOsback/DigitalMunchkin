from Cards_Samlet import CardType


class Player:
    handCards = []
    tableCards = [armour = None, head = None, foot = None, hands = None, hireling = None]
    gender = input('What is your Gender? (Male/Female) \n')
    race = "Human"
    playerClass = None
    level = 1
    levelTotal = 1
    gold = 0
    
    def __init__(self, handCards = [None], tableCards = [armour = None, head = None, foot = None, hands = None, hireling = None], gender = "Male", race = "human", playerClass = None, level = 1, levelTotal = 1, gold = 0, armour = None, head = None, foot = None, hands = None): 
        """Initializes the data."""
        
        self.handCards = handCards
        self.tableCards = tableCards
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

    

