from enum import Enum, auto
import csv


class CardType(Enum):
    """The different card types like monster cards, headgear, curses ect."""
    
    monsterCard = auto()
    curseCard = auto()
    steedCard = auto()
    hirelingCard = auto()
    classCard = auto()
    RaceCard = auto()
    headgearCard = auto()
    footGearCard = auto()
    armourCard = auto()
    weaponCard = auto()
    levelCard = auto()
    monster_boost_card = auto()
    boostCard = auto()


class Cards:
    """The overall card object. Different kind of cards will inherit from this
    This class splits in DoorCards and TreasureCards. TreasureCards inherit to GearCards. 

    """
    
    def __init__(self, card_number, card_name, card_description):
        """Initializes the data."""
        
        self.cardNumber = card_number
        self.cardName = card_name
        self.cardDescription = card_description


class TreasureCards(Cards):

    def __init__(self, card_number, card_name, card_description, level_bonus, item_value):
        """Initializes the data."""
        
        super(TreasureCards, self).__init__(card_number, card_name, card_description)
        self.level_bonus = level_bonus
        self.itemValue = item_value


class DoorCards(Cards):
     
    def __init__(self, card_number, card_name, card_description):
        """Initializes the data."""
        
        super(DoorCards, self).__init__(card_number, card_name, card_description)

    
class GearCards(TreasureCards):    
     
    def __init__(self, card_number, card_name, card_description, level_bonus, item_value, big):
        """Initializes the data."""
        
        super(GearCards, self).__init__(card_number, card_name, card_description, level_bonus, item_value)
        self.big = big


class MonsterCards(DoorCards):    
     
    def __init__(self, card_number, card_name, card_description, monster_level, bad_stuff, run_away):
        """Initializes the data."""
        
        super(MonsterCards, self).__init__(card_number, card_name, card_description)
        self.monsterLevel: int = monster_level
        self.badStuff = bad_stuff
        self.run_away = run_away

        
class CurseCards(DoorCards):    
     
    def __init__(self, card_number, card_name, card_description, curse_effect):
        """Initializes the data."""
        
        super(CurseCards, self).__init__(card_number, card_name, card_description)
        self.curseEffect = curse_effect


class HirelingCards(DoorCards):    
     
    def __init__(self, card_number, card_name, card_description, hireling_bonus):
        """Initializes the data."""
        
        super(HirelingCards, self).__init__(card_number, card_name, card_description)
        self.hirelingBonus = hireling_bonus
   
   
class ClassCards(DoorCards):    
     
    def __init__(self, card_number, card_name, card_description):
        """Initializes the data."""
        
        super(ClassCards, self).__init__(card_number, card_name, card_description)
  
    
class RaceCards(DoorCards):    
     
    def __init__(self, card_number, card_name, card_description):
        """Initializes the data."""
        
        super(RaceCards, self).__init__(card_number, card_name, card_description)
        

class ModifierCards(DoorCards):    
     
    def __init__(self, card_number, card_name, card_description, modifier):
        """Initializes the data."""
        
        super(ModifierCards, self).__init__(card_number, card_name, card_description)
        self.modifier = modifier
    
       
class HeadgearCards(GearCards):    
     
    def __init__(self, card_number, card_name, card_description, level_bonus, item_value, big):
        """Initializes the data."""
        
        super(HeadgearCards, self).__init__(card_number, card_name, card_description, level_bonus, item_value, big)
        
        
class FootGearCards(GearCards):
     
    def __init__(self, card_number, card_name, card_description, level_bonus, item_value, big):
        """Initializes the data."""
       
        super(FootGearCards, self).__init__(card_number, card_name, card_description, level_bonus, item_value, big)
        
        
class ArmourCards(GearCards):    
     
    def __init__(self, card_number, card_name, card_description, level_bonus, item_value, big):
        """Initializes the data."""
        
        super(ArmourCards, self).__init__(card_number, card_name, card_description, level_bonus, item_value, big)
        
        
class WeaponCards(GearCards):    
     
    def __init__(self, card_number, card_name, card_description, level_bonus, item_value, big):
        """Initializes the data."""
        
        super(WeaponCards, self).__init__(card_number, card_name, card_description, level_bonus, item_value, big)
            
        
class LevelCards(TreasureCards):    
     
    def __init__(self, card_number, card_name, card_description, level_bonus, item_value):
        """Initializes the data."""
        
        super(LevelCards, self).__init__(card_number, card_name, card_description, level_bonus, item_value)


class CreateCards:
    # creating door card stack
    # read csv, and split on "," the line
    def read_door_cards(self, file='MunchkinDoorCards.csv'):

        cards = []
        with open(file, "r") as csv_file:
            reader = csv.DictReader(csv_file)

            # loop through the csv list
            for row in reader:
                # checking for empty rows
                if len(row) > 1:
                    if row["card_type"] == "Monster":
                        card = MonsterCards(
                            row["card_number"],
                            row["name"],
                            row["card_description"],
                            int(row["modifier"]),
                            row["bad_stuff"],
                            int(row["run_away"]))
                        cards.append(card)
                    elif row["card_type"] == "Curse":
                        card = CurseCards(
                            row["card_number"],
                            row["name"],
                            row["card_description"],
                            row["bad_stuff"])
                        cards.append(card)
                    elif row["card_type"] == "Class":
                        card = ClassCards(
                            row["card_number"],
                            row["name"],
                            row["card_description"])
                        cards.append(card)
                    elif row["card_type"] == "Race":
                        card = RaceCards(
                            row["card_number"],
                            row["name"],
                            row["card_description"])
                        cards.append(card)
                    elif row["card_type"] == "Hireling":
                        card = HirelingCards(
                            row["card_number"],
                            row["name"], row["card_description"],
                            row["modifier"])
                        cards.append(card)
                    elif row["card_type"] == "Modifier":
                        card = ModifierCards(
                            row["card_number"],
                            row["name"],
                            row["card_description"],
                            row["modifier"])
                        cards.append(card)
        return cards

    # creating treasure card stack
    # read csv, and split on "," the line

    def read_treasure_cards(self, file='MunchkinTreasureCards.csv'):
        cards = []
        with open(file, "r") as csv_file:
            reader = csv.DictReader(csv_file)

            # loop through the csv list
            for row in reader:
                if len(row) > 1:  # checking for empty rows
                    if row["card_type"] == "Weapon":
                        card = WeaponCards(
                            row["card_number"],
                            row["name"],
                            row["card_description"],
                            row["battle_modifier"],
                            row["price"],
                            row["big"])
                        cards.append(card)
                    elif row["card_type"] == "Headgear":
                        card = HeadgearCards(
                            row["card_number"],
                            row["name"],
                            row["card_description"],
                            row["battle_modifier"],
                            row["price"],
                            row["big"])
                        cards.append(card)
                    elif row["card_type"] == "Footgear":
                        card = FootGearCards(
                            row["card_number"],
                            row["name"],
                            row["card_description"],
                            row["battle_modifier"],
                            row["price"],
                            row["big"])
                        cards.append(card)
                    elif row["card_type"] == "Armour":
                        card = ArmourCards(
                            row["card_number"],
                            row["name"],
                            row["card_description"],
                            row["battle_modifier"],
                            row["price"],
                            row["big"])
                        cards.append(card)
                    elif row["card_type"] == "GUAL":
                        card = LevelCards(
                            row["card_number"],
                            row["name"],
                            row["card_description"],
                            row["battle_modifier"],
                            row["price"])
                        cards.append(card)
        return cards

                
# print(Cards.treasureCardsStack)
# print(Cards.doorCardsStack)


""" Questions
    - Dictreader does not work when using it on search function.
    - If a class inherit from another class which takes parameters, will you then have to add the parameters from
    parent class when creating and instans of the sub class? Better to destroy root class and then have door and 
    treasure as root? 
    - Class parameter as method. Best way? e.g. BadStuff, CurseEffect. 
    - Footgear, headgear armour, level up cards and so on, has no special parameters. Should it just use the enum to 
    identify itself?
"""
