from typing import List

from Cards_Samlet import *
from dataclasses import dataclass
from enum import Enum, auto


class Gender(Enum):
    """
    M = Male
    F = Female
    """

    MALE = "Male"
    FEMALE = "Female"

@dataclass
class Table:
    armour: ArmourCards = None
    head: HeadgearCards = None
    foot: FootGearCards = None
    weapon_l: WeaponCards = None
    weapon_r: WeaponCards = None
    hireling: HirelingCards = None

    def remove(self, card):
        raise NotImplemented("WATT!")

    def add(self, card):
        raise NotImplemented("SHASDA!")


class Player:

    def __init__(self, name=None, type=None, gender=None, race="Human", hand_cards=None, table_cards=None, player_class=None, level=1, level_total=1, gold=0):
        """Initializes the data."""

        self.name = name
        self.type = type
        self.gender: Gender = gender
        self.race = race or "Human"
        self.hand_cards: List[Cards] = hand_cards or []
        self.table_cards: Table = table_cards or Table()
        self.player_class = player_class
        self.level: int = level
        self.levelTotal = level_total
        self.gold = gold

    def test_information(self):
        print(self.name)
        print(self.type)
        print(self.gender)
        print(self.race)
        print(self.hand_cards)
        print(self.table_cards)
        print(self.player_class)
        print(self.level)
        print(self.levelTotal)
        print(self.gold)

    def throw_card(self, card: Cards):
        self.table_cards.add(card)  # wield new item
        self.hand_cards.remove(card)  # remove from handcards

    def replace_card(self, old: Cards, new: Cards):
        self.table_cards.remove(old)
        self.throw_card(new)

    def throw_better_cards(self) -> List[Cards]:
        return []
        def check_hand_cards(self, cardtype, item):
            # cardtype should be a string with 1 uppercase word, like: Armour
            for card in self.active_player.hand_cards:
                if not isinstance(card, TreasureCards): continue
                if card.cardType == cardtype:  # looking through hand cards searching for a weapon
                    if item is None:
                        item = card
                    else:
                        if card.levelBonus > item.levelBonus:  # is it better than what you are wielding?
                            self.replace(item, card)
                else:
                    print(f"No {cardtype} cards on hand")

        def check_weapon_cards(self):  # cardtype should be a string with 1 upercase word, like: Armour
            worst_weapon = None
            for card in self.active_player.hand_cards:
                if isinstance(card, WeaponCards):  # looking through hand cards searching for a weapon
                    if self.active_player.table_cards.weapon_l is None:
                        self.active_player.table_cards.weapon_l = card
                    else:
                        if self.active_player.table_cards.weapon_l.levelBonus > self.active_player.table_cards.weapon_r.levelBonus:
                            worst_weapon = self.active_player.table_cards.weapon_r
                        else:
                            worst_weapon = self.active_player.table_cards.weapon_l

                        for card in self.active_player.hand_cards:
                            if card.levelBonus > worst_weapon.levelBonus:  # is it better than what you are wielding?
                                self.replace(worst_weapon, card)
                else:
                    print(f"No weapon cards on hand")

        def check_all_handcards(self):
            self.check_hand_cards("Armour", self.active_player.table_cards.armour)
            self.check_hand_cards("Headgear", self.active_player.table_cards.head)
            self.check_hand_cards("Footgear", self.active_player.table_cards.foot)
            self.check_weapon_cards()

    def die(self):
        raise NotImplemented()