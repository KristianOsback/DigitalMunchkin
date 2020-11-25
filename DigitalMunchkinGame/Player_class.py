from Cards_Samlet import Cards
from dataclasses import dataclass


@dataclass
class Table:
    armour: Cards = None
    head: Cards = None
    foot: Cards = None
    hands: Cards = None
    hireling: Cards = None


class Player:

    def __init__(self, gender, race, hand_cards=None, table_cards=None, r_weapon=None, l_weapon=None,
                 armour=None, headgear=None, footgear=None, player_class=None, level=1, level_total=1, gold=0):
        """Initializes the data."""

        self.handCards = hand_cards or []
        self.tableCards = table_cards or Table()
        self.gender = gender
        self.race = race
        self.weapon_r = r_weapon
        self.weapon_l = l_weapon
        self.armour = armour
        self.headgear = headgear
        self.footgear = footgear
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
        self.discard(discard_card.cardType)  # discard card
        self.throwcard(throw_card)  # place card

    def check_hand_cards(self, cardtype, item):  # cardtype should be a string with 1 upercase word, like: Armour
        for card in self.handCards:
            if card.cardType == cardtype:  # looking through hand cards searching for a weapon
                if card.levelBonus > item.itembonus:  # is it better than what you are wielding?
                    self.replace(item, card)
            else:
                print(f"No {cardtype} cards on hand")

    def check_weapon_cards(self):  # cardtype should be a string with 1 upercase word, like: Armour
        worst_weapon = None
        if self.weapon_l.levelBonus > self.weapon_r.levelBonus:
            worst_weapon = self.weapon_r.levelBonus
        else:
            worst_weapon = self.weapon_l.levelBonus
        for card in self.handCards:
            if card.cardType == "Weapon":  # looking through hand cards searching for a weapon
                if card.levelBonus > worst_weapon.itembonus:  # is it better than what you are wielding?
                    self.replace(worst_weapon, card)
            else:
                print(f"No weapon cards on hand")

    def check_all_handcards(self):
        self.check_hand_cards("Armour", self.armour)
        self.check_hand_cards("Headgear", self.headgear)
        self.check_hand_cards("Footgear", self.footgear)
        self.check_hand_cards("Armour", self.armour)
        self.check_weapon_cards()
