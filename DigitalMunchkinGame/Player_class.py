from typing import List
from Cards_Samlet import *
from dataclasses import dataclass
from enum import Enum



class Gender(Enum):
    """
    M = Male
    F = Female
    """

    MALE = "Male"
    FEMALE = "Female"


class PlayerType(Enum):
    """
    C = Computer
    H = Human
    """

    COMPUTER = "Computer"
    HUMAN = "Human"

@dataclass
class Table:
    armour: ArmourCards = None
    head: HeadgearCards = None
    foot: FootGearCards = None
    weapon_l: WeaponCards = None
    weapon_r: WeaponCards = None
    hireling: HirelingCards = None

    def remove(self, card: Cards):
        Player().table_cards.remove(card)

    def add_armour(self, card: Cards):
        Player().table_cards.armour = card

    def add_head(self, card: Cards):
        Player().table_cards.head = card

    def add_foot(self, card: Cards):
        Player().table_cards.foot = card

    def add_weapon_r(self, card: Cards):
        Player().table_cards.weapon_r = card

    def add_weapon_l(self, card: Cards):
        Player().table_cards.weapon_l = card

    def add_hireling(self, card: Cards):
        Player().table_cards.hireling = card


class Player:

    def __init__(self,
                 name=None,
                 type=None,
                 gender=None,
                 race="Human",
                 hand_cards=None,
                 table_cards=None,
                 player_class=None,
                 level=1,
                 level_total=1,
                 gold=0):
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

    def replace_card(self, old: Cards, new: Cards):
        self.table_cards.remove(old)
        if new is isinstance(new, ArmourCards):
            self.table_cards.add_armour(new)
        elif new is isinstance(new, HeadgearCards):
            self.table_cards.add_head(new)
        elif new is isinstance(new, FootGearCards):
            self.table_cards.add_foot(new)
        elif new is isinstance(new, HirelingCards):
            self.table_cards.add_hireling(new)

    def replace_weapon(self, old: Cards, new: Cards):
        self.table_cards.remove(old)
        for card in self.hand_cards:
            if isinstance(card, WeaponCards):  # looking through hand cards searching for a weapon
                if self.table_cards.weapon_l.level_bonus > self.table_cards.weapon_r.level_bonus:
                    worst_weapon = self.table_cards.weapon_r
                else:
                    worst_weapon = self.table_cards.weapon_l
                for card in self.hand_cards:
                    if isinstance(card, WeaponCards):
                        if card.level_bonus > worst_weapon.level_bonus:  # is it better than what you are wielding?
                            self.replace_card(worst_weapon, card)
                            return worst_weapon

    @property
    def throw_better_cards(self) -> List[Cards]:
        discards = [self.check_hand_cards(ArmourCards, self.table_cards.armour),
                    self.check_hand_cards(HeadgearCards, self.table_cards.head),
                    self.check_hand_cards(FootGearCards, self.table_cards.foot), self.check_weapon_cards()]
        return discards

    def check_hand_cards(self, card_type, item):
        for card in self.hand_cards:
            if not isinstance(card, TreasureCards):
                continue
            if card is card_type:  # looking through hand cards searching for a weapon
                if item is None:
                    item = card
                else:
                    if card.level_bonus > item.level_bonus:  # is it better than what you are wielding?
                        self.replace_card(item, card)
                        return item
            else:
                print(f"No {card_type} cards on hand")

    def check_weapon_cards(self):
        for card in self.hand_cards:
            if isinstance(card, WeaponCards):
                if self.table_cards.weapon_l is None and self.table_cards.weapon_r is None:
                    self.table_cards.weapon_r = card
                elif self.table_cards.weapon_l is None and self.table_cards.weapon_r is isinstance(self.table_cards.weapon_r, WeaponCards ):
                    self.table_cards.weapon_l = card
                    if self.table_cards.weapon_l.level_bonus > self.table_cards.weapon_r.level_bonus:
                        worst_weapon = self.table_cards.weapon_r
                    else:
                        worst_weapon = self.table_cards.weapon_l
                    for card in self.hand_cards:
                        if isinstance(card, WeaponCards):
                            if card.level_bonus > worst_weapon.level_bonus:  # is it better than what you are wielding?
                                self.replace_card(worst_weapon, card)
                            return worst_weapon

    def die(self):
        discards = [
            self.table_cards.armour,
            self.table_cards.head,
            self.table_cards.foot,
            self.table_cards.weapon_r,
            self.table_cards.weapon_l,
            self.table_cards.hireling,
            ]
        discards.extend(self.hand_cards)
        self.table_cards.armour = None
        self.table_cards.head = None
        self.table_cards.foot = None
        self.table_cards.weapon_r = None
        self.table_cards.weapon_l = None
        self.table_cards.hireling = None
        self.hand_cards = None
        self.race = "Human"
        self.player_class = None
        self.level = 1
        self.levelTotal = 1
        return discards
