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
    
    def __init__(self, gender, race, hand_cards = None, table_cards = None, r_weapon = None,  l_weapon = None,
                 armour=None, headgear = None, foodgear = None, player_class = None, level = 1, level_total = 1, gold = 0):
        """Initializes the data."""
        
        self.handCards = hand_cards or []
        self.tableCards = table_cards or Table()
        self.gender = gender
        self.race = race
        self.weaponBonus = weapon_bonus
        self.armourBonus = armour_bonus
        self.headgearBonus = headgear_bonus
        self.footgear_bonus = footgear_bonus
        self.playerClass = player_class
        self.level = level
        self.levelTotal = level_total
        self.gold = gold


    def discard(self, card):
        Cards.treasureCardsDiscardStack.append(card)  # add it to discard stack
        self.tableCards.remove(card)  # unwield item

    def throw_card(self, card):
        self.tableCards.append(card)  # wield new item
        self.handCards.remove(card)  # remove from handcards

    def replace(self, discard_card, throw_card):
        self.discard(discard_card.cardType) #discard card
        self.throwcard(throw_card) #place card

    def check_hand_cards(self, cardtype, itembonus):
        for card in self.handCards:
            if card.cardType == cardtype: #looking through hand cards searching for a weapon
                if card.levelBonus > itembonus: #is it better than what you are wielding?
                    self.replace(, card)



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
                    
                    
                    

