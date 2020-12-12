from typing import List
from PlayerTurn_graph import Game
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


@dataclass
class Table:
    armour: ArmourCards = None
    head: HeadgearCards = None
    foot: FootGearCards = None
    weapon_l: WeaponCards = None
    weapon_r: WeaponCards = None
    hireling: HirelingCards = None

    def remove(self, card: Cards, from_collection: list, discard_stack):


    def (self, card: Cards):
        self.


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
            if isinstance(card, WeaponCards):  # looking through hand cards searching for a weapon
                if self.table_cards.weapon_l is None and self.table_cards.weapon_r is None:
                    self.table_cards.weapon_r = card
                else:
                    if self.table_cards.weapon_l.level_bonus > self.table_cards.weapon_r.level_bonus:
                        worst_weapon = self.table_cards.weapon_r
                    else:
                        worst_weapon = self.table_cards.weapon_l
                    for card in self.hand_cards:
                        if isinstance(card, WeaponCards):
                            if card.level_bonus > worst_weapon.level_bonus:  # is it better than what you are wielding?
                                self.replace_card(worst_weapon, card)
                                return worst_weapon
            else:
                print(f"No weapon cards on hand")

    def die(self):
        raise NotImplemented()
