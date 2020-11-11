from Cards_Samlet import CardType


class Player:
    handCards = []
    tableCards = []
    gender = input('What is your Gender? (Male/Female) \n')
    breed = "Human"
    playerClass = None
    level = 1
    gold = 0
    armour = None
    head = None
    foot = None
    hands = None 
    
    def __init__(self, handCards, tableCards, gender, breed, playerClass,level,gold,armour,head,foot,hands): 
        """Initializes the data."""
        
        self.handCards = handCards
        self.tableCards = tableCards
        self.gender = gender
        self.breed = breed
        self.playerClass = playerClass
        self.level = level
        self.gold = gold
        self.armour = armour
        self.head = head
        self.foot = foot
        self.hands = hands
        print("(Initializing {})".format(self.handCards))
        print("(Initializing {})".format(self.tableCards))
        print("(Initializing {})".format(self.gender))
        print("(Initializing {})".format(self.breed))
        print("(Initializing {})".format(self.playerClass))
        print("(Initializing {})".format(self.level))
        print("(Initializing {})".format(self.gold))
        print("(Initializing {})".format(self.armour))
        print("(Initializing {})".format(self.head))
        print("(Initializing {})".format(self.foot))
        print("(Initializing {})".format(self.hands))
    



P1 = Player()
print(P1)


"""
- Where should start/default values be placed? 
"""