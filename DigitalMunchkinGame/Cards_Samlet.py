from enum import Enum, auto
import csv

class Card_type(Enum):
    """The different cardtypes like monstercards, headgear, curses ect."""
    
    monsterCard = auto()
    curseCard = auto()
    steedCard = auto()
    hirelingCard = auto()
    classCard = auto()
    RaceCard = auto()
    headgearCard = auto()
    footgearCard = auto()
    armourCard = auto()
    weaponCard = auto()
    levelCard = auto()
    monsterboost_card = auto()
    boostCard = auto()


class Cards:
    """The overall card object. Different kind of cards will inherit from this
    This class splits in DoorCards and TreasureCards. TreasureCards inherit to GearCards. 

    """
    totalCardList = []
    
    doorCardsStack = []
    doorCardsDiscardStack = []
    treasureCardsStack = []
    treasureCardsDiscardStack = []
    
    Amount = 0
    Left = 0
    
    def __init__(self, cardNumber, cardName, cardType, cardDescription): 
        """Initializes the data."""
        
        self.cardNumber = cardNumber
        self.cardName = cardName
        self.cardType = cardType
        self.cardDescription = cardDescription

        Cards.totalCardList.append(self)
        Cards.Amount += 1 #why does this not work? Will work, måske skal den ændres nu hvor det er class variables. 
        Cards.Left += 1 #Counting total cards in deck


class TreasureCards(Cards):

    def __init__(self, cardNumber, cardName, cardType, cardDescription, levelBonus, itemValue): 
        """Initializes the data."""
        
        super(TreasureCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
        self.levelBonus = levelBonus
        self.itemValue = itemValue


class DoorCards(Cards):
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription): 
        """Initializes the data."""
        
        super(DoorCards, self).__init__(cardNumber, cardName, cardType, cardDescription)

    
class GearCards(TreasureCards):    
     
    def __init__(self, card_number, cardName, cardType, cardDescription, levelBonus, itemValue, big):
        """Initializes the data."""
        
        super(GearCards, self).__init__(card_number, cardName, cardType, cardDescription, levelBonus, itemValue)
        self.big = big


class MonsterCards(DoorCards):    
     
    def __init__(self, card_number, card_name, card_type, card_description, monster_level, bad_stuff, run_away):
        """Initializes the data."""
        
        super(MonsterCards, self).__init__(card_number, card_name, card_type, card_description)
        self.monsterLevel = monster_level
        self.badStuff = bad_stuff
        self.run_away = run_away

        
class CurseCards(DoorCards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, curseEffect): 
        """Initializes the data."""
        
        super(CurseCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
        self.curseEffect = curseEffect


class HirelingCards(DoorCards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, hirelingBonus): 
        """Initializes the data."""
        
        super(HirelingCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
        self.hirelingBonus = hirelingBonus
   
   
class ClassCards(DoorCards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription): 
        """Initializes the data."""
        
        super(ClassCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
  
    
class RaceCards(DoorCards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription): 
        """Initializes the data."""
        
        super(RaceCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
        

class ModifierCards(DoorCards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, modifier): 
        """Initializes the data."""
        
        super(ModifierCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
        self.modifier = modifier
    
       
class HeadgearCards(GearCards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, levelBonus, itemValue, big): 
        """Initializes the data."""
        
        super(HeadgearCards, self).__init__(cardNumber, cardName, cardType, cardDescription, levelBonus, itemValue, big)
        
        
class FootgearCards(GearCards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, levelBonus, itemValue, big): 
        """Initializes the data."""
       
        super(FootgearCards, self).__init__(cardNumber, cardName, cardType, cardDescription, levelBonus, itemValue, big)
        
        
class ArmourCards(GearCards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, levelBonus, itemValue, big): 
        """Initializes the data."""
        
        super(ArmourCards, self).__init__(cardNumber, cardName, cardType, cardDescription, levelBonus, itemValue, big)
        
        
class WeaponCards(GearCards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, levelBonus, itemValue, big): 
        """Initializes the data."""
        
        super(WeaponCards, self).__init__(cardNumber, cardName, cardType, cardDescription, levelBonus, itemValue, big)
            
        
class LevelCards(TreasureCards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, levelBonus, itemValue): 
        """Initializes the data."""
        
        super(LevelCards, self).__init__(cardNumber, cardName, cardType, cardDescription, levelBonus, itemValue)
   

#creating door card stack
#read csv, and split on "," the line
with open('MunchkinDoorCards.csv', "r") as csv_file:
    reader = csv.DictReader(csv_file)

    #loop through the csv list
    for row in reader:
        if len(row) > 1: #checking for empty rows 
            if row["card_type"] == "Monster":
                Cards.doorCardsStack.append(MonsterCards(row["card_number"], row["name"], row["card_type"], row["card_description"], row["modifier"], row["bad_stuff"], row["run_away"]))
            elif row["card_type"] == "Curse":
                Cards.doorCardsStack.append(CurseCards(row["card_number"], row["name"], row["card_type"], row["card_description"], row["bad_stuff"]))
            elif row["card_type"] == "Class":
                Cards.doorCardsStack.append(ClassCards(row["card_number"], row["name"], row["card_type"], row["card_description"]))
            elif row["card_type"] == "Race":
                Cards.doorCardsStack.append(RaceCards(row["card_number"], row["name"], row["card_type"], row["card_description"]))
            elif row["card_type"] == "Hireling":
                Cards.doorCardsStack.append(HirelingCards(row["card_number"], row["name"], row["card_type"], row["card_description"], row["modifier"]))
            elif row["card_type"] == "Modifier":
                Cards.doorCardsStack.append(ModifierCards(row["card_number"], row["name"], row["card_type"], row["card_description"], row["modifier"]))
#creating treasure card stack
#read csv, and split on "," the line
with open('MunchkinTreasureCards.csv', "r") as csv_file:
    reader = csv.DictReader(csv_file)

    #loop through the csv list
    for row in reader:
        if len(row) > 1: #checking for empty rows 
            if row["card_type"] == "Weapon":
                Cards.treasureCardsStack.append(WeaponCards(row["card_number"], row["name"], row["card_type"], row["card_description"], row["battle_modifier"], row["price"], row["big"]))
            elif row["card_type"] == "Headgear":
                Cards.treasureCardsStack.append(HeadgearCards(row["card_number"], row["name"], row["card_type"], row["card_description"], row["battle_modifier"], row["price"], row["big"]))
            elif row["card_type"] == "Footgear":
                Cards.treasureCardsStack.append(FootgearCards(row["card_number"], row["name"], row["card_type"], row["card_description"], row["battle_modifier"], row["price"], row["big"]))
            elif row["card_type"] == "Armour":
                Cards.treasureCardsStack.append(ArmourCards(row["card_number"], row["name"], row["card_type"], row["card_description"], row["battle_modifier"], row["price"], row["big"]))
            elif row["card_type"] == "GUAL":
                Cards.treasureCardsStack.append(LevelCards(row["card_number"], row["name"], row["card_type"], row["card_description"], row["battle_modifier"], row["price"]))
                
    
                
#print(Cards.treasureCardsStack) 
#print(Cards.doorCardsStack) 


""" Questions
    - Dictreader does not work when using it on search function.
    - If a class inherit from another class which takes parameters, will you then have to add the parameters from
    parent class when creating and instans of the sub class? Better to destroy root class and then have door and treasure as root? 
    - Class parameter as method. Best way? e.g. BadStuff, CurseEffect. 
    - Footgear, headgear armour, level up cards and so on, has no special parameters. Should it just use the enum to identify itself?
"""
