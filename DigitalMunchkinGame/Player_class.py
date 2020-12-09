from Cards_Samlet import Cards
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
    armour: Cards = None
    head: Cards = None
    foot: Cards = None
    weapon_l: Cards = None
    weapon_r: Cards = None
    hireling: Cards = None


class Player:

    def __init__(self, name=None, type=None, gender=None, race="Human", hand_cards=None, table_cards=None, player_class=None, level=1, level_total=1, gold=0):
        """Initializes the data."""

        self.name = name
        self.type = type
        self.gender = gender
        self.race = race or "Human"
        self.hand_cards = hand_cards
        self.table_cards = table_cards or Table()
        self.playerClass = player_class
        self.level = level
        self.levelTotal = level_total
        self.gold = gold

    def test_information(self):
        print(self.name)
        print(self.type)
        print(self.gender)
        print(self.race)
        print(self.hand_cards)
        print(self.table_cards)
        print(self.playerClass)
        print(self.level)
        print(self.levelTotal)
        print(self.gold)

