from Cards_Samlet import Cards
from dataclasses import dataclass

@dataclass
class Table:
    armour: Cards = None
    head: Cards = None
    foot: Cards= None 
    hands: Cards = None
    hireling: Cards = None


class Player:
    
    def __init__(self, gender, race, handCards = None, tableCards = None, weaponBonus = 0, armourBonus = 0, headgearBonus = 0, FootgearBonus = 0, playerClass = None, level = 1, levelTotal = 1, gold = 0): 
        """Initializes the data."""
        
        self.handCards = handCards or []
        self.tableCards = tableCards or Table()
        self.gender = gender
        self.race = race
        self.playerClass = playerClass
        self.level = level
        self.levelTotal = levelTotal
        self.gold = gold
        self.weaponBonus = weaponBonus
        self.armourBonus = armourBonus
        self.headgearBonus = headgearBonus
        self.FootgearBonus = FootgearBonus
        print("(Initializing {})".format(self.handCards))
        print("(Initializing {})".format(self.tableCards))
        print("(Initializing {})".format(self.gender))
        print("(Initializing {})".format(self.race))
        print("(Initializing {})".format(self.playerClass))
        print("(Initializing {})".format(self.level))
        print("(Initializing {})".format(self.levelTotal))
        print("(Initializing {})".format(self.gold))
        print("(Initializing {})".format(self.weaponBonus))
        print("(Initializing {})".format(self.armourBonus))
        print("(Initializing {})".format(self.headgearBonus))
        print("(Initializing {})".format(self.FootgearBonus))

    def CheckHandCards():
        for card in self.handCards:
            if card.cardType == "Weapon": #looking through hand cards searching for a weapon
                if card.levelBonus > self.weaponBonus: #is it better than what you are wielding? 
                    for weaponCard in self.tableCards: #looking on your table cards
                        if weaponCard.cardType == "Weapon": #looking if your are wielding a weapon
                            Cards_samlet.Cards.treasureCardsDiscardStack.append(weaponCard) #add it to discard stack
                            self.tableCards.remove(weaponCard) #unwield weapon
                            self.tableCards.append(card) #wield new weapon
                            self.handCards.remove(card) #remove from handcards   
            elif card.cardType == "Armour": 
                if card.levelBonus > self.armourBonus: 
                    for armourCard in self.tableCards: 
                        if armourCard.cardType == "Armour": 
                            Cards_samlet.Cards.treasureCardsDiscardStack.append(armourCard) 
                            self.tableCards.remove(armourCard) 
                            self.tableCards.append(card) 
                            self.handCards.remove(card) 
            elif card.cardType == "Headgear": 
                if card.levelBonus > self.headgearBonus: 
                    for headgearCard in self.tableCards: 
                        if headgearCard.cardType == "Headgear": 
                            Cards_samlet.Cards.treasureCardsDiscardStack.append(headgearCard) 
                            self.tableCards.remove(headgearCard)
                            self.tableCards.append(card) 
                            self.handCards.remove(card) 
            elif card.cardType == "Footgear": 
                if card.levelBonus > self.footgearBonus:
                    for footgearCard in self.tableCards: 
                        if footgearCard.cardType == "Footgear": 
                            Cards_samlet.Cards.treasureCardsDiscardStack.append(footgearCard)
                            self.tableCards.remove(footgearCard) 
                            self.tableCards.append(card) 
                            self.handCards.remove(card)
            else
                print("No gear cards")
                    
                    
                    

