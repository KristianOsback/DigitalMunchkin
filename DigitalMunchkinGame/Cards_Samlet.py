from enum import Enum #auto can auto number them.
import csv
class CardType(Enum):
    """The different cardtypes like monstercards, headgear, curses ect."""
    
    monsterCard = "Monster"
    curseCard = "Curse"
    steedCard = "Steed"
    hirelingCard = "Hireling"
    classCard = "Class"
    RaceCard = "Race"
    headgearCard = "Headgear"
    footgearCard = "Footgear"
    armourCard = "Armour"
    weaponCard = "Weapon"
    levelCard = "Level up"
    monsterboostCard = "Monster boost"
    boostCard = "Boost"



class Cards:
    """The overall card object. Different kind of cards will inherit from this"""
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
        print("(Initializing {})".format(self.cardNumber))
        print("(Initializing {})".format(self.cardName))
        print("(Initializing {})".format(self.cardType))
        print("(Initializing {})".format(self.cardDescription))


        Cards.totalCardList.append(self)
        Cards.Amount += 1 #why does this not work? Will work, måske skal den ændres nu hvor det er class variables. 
        Cards.Left += 1 #Counting total cards in deck
        
        
    def discardCard(self, card, removedFrom): #removedFrom is the list that throws the card. Can be a players hand or the table or the Stack
        """Throw or discard a card"""
        
        discardStack.append(card) #card is thrown in the discard stack
        removedFrom.pop(card) #card is removed from stack or the players hand or the table
       
class TreasureCards(Cards):    
     
    def __init__(self, itemValue): 
        """Initializes the data."""
        
        self.itemValue = itemValue
        print("(Initializing {})".format(self.itemValue))

    
class GearCards(TreasureCards):    
     
    def __init__(self, bonus, special, limitation, big): 
        """Initializes the data."""
        
        self.bonus = bonus
        self.special = special
        self.limitation = limitation
        self.big = big
        print("(Initializing {})".format(self.itemValue))
        print("(Initializing {})".format(self.bonus))
        print("(Initializing {})".format(self.special))
        print("(Initializing {})".format(self.limitation))  
      
      
class MonsterCards(Cards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, monsterLevel, badStuff): 
        """Initializes the data."""
        
        super(MonsterCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
        self.monsterLevel = monsterLevel
        self.badStuff = badStuff
        print("(Initializing {})".format(self.monsterLevel))
        print("(Initializing {})".format(self.badStuff))
        
        
class CurseCards(Cards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, curseEffect): 
        """Initializes the data."""
        
        super(MonsterCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
        self.curseEffect = curseEffect
        print("(Initializing {})".format(self.curseEffect))
        

class HirelingCards(Cards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, hirelingBonus): 
        """Initializes the data."""
        
        super(MonsterCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
        self.hirelingBonus = hirelingBonus
        print("(Initializing {})".format(self.hirelingBonus))
   
   
class ClassCards(Cards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription): 
        """Initializes the data."""
        
        super(MonsterCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
  
    
    
class RaceCards(Cards):    
     
    def __init__(self): 
        """Initializes the data."""
        
        super(MonsterCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
        

class ModifierCards(Cards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, modifier): 
        """Initializes the data."""
        
        super(MonsterCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
        self.modifier = modifier
        print("(Initializing {})".format(self.specialSkill))
    
       
class HeadgearCards(GearCards):    
     
    def __init__(self): 
        """Initializes the data."""
        
        
class FootgearCards(GearCards):    
     
    def __init__(self): 
        """Initializes the data."""
       
        
class ArmourCards(GearCards):    
     
    def __init__(self): 
        """Initializes the data."""
        
        
class WeaponCards(GearCards):    
     
    def __init__(self, twoHanded): 
        """Initializes the data."""
        
        self.twoHanded = twoHanded
        print("(Initializing {})".format(self.twoHanded))
        
        
class LevelCards(GearCards):    
     
    def __init__(self): 
        """Initializes the data."""
     

class MonsterboosterCards(Cards):    
     
    def __init__(self, cardNumber, cardName, cardType, cardDescription, boost): 
        """Initializes the data."""
        
        super(MonsterCards, self).__init__(cardNumber, cardName, cardType, cardDescription)
        self.boost = boost
        print("(Initializing {})".format(self.boost))
        
   

#creating door card stack
#read csv, and split on "," the line
with open('MunchkinDoorCards.csv', "r") as csv_file:
    reader = csv.DictReader(csv_file)

    #loop through the csv list
    for row in reader:
        print(row)
        if len(row) > 1: #checking for empty rows 
            if row["card_type"] == "Monster":
                Cards.doorCardsStack.append(MonsterCards(row["card_number"], row["name"], row["card_type"], row["card_description"], row["modifier"], row["bad_stuff"]))
            #elif row[3] == "Curse":
                #doorCardsStack.append(CurseCards(row[0], row[2], row[3], row[9], row[5], row[5]))
            #elif row[3] == "Class":
                #doorCardsStack.append(ClassCards(row[0], row[2], row[3], row[9], row[5]))
            #elif row[3] == "Race":
                #doorCardsStack.append(RaceCards(row[0], row[2], row[3], row[9], row[5]))
            #elif row[3] == "Hireling":
                #doorCardsStack.append(HirelingCards(row[0], row[2], row[3], row[9], row[4]))
            #elif row[3] == "Modifier":
                #doorCardsStack.append(ModifierCards(row[0], row[2], row[3], row[9], row[4]))
                

#creating treasure card stack
#read csv, and split on "," the line
with open('MunchkinTreasureCards.csv', "r") as csv_file:
    reader = csv.reader(csv_file)

    #loop through the csv list
    for row in reader:
        if len(row) > 1: #checking for empty rows 
            if row[3] == "Weapon":
                Cards.treasureCardsStack.append(WeaponCards(row[0], row[2], row[3], row[16], row[5], row[13]))
            #elif row[3] == "Headgear":
                #treasureCardsStack.append(HeadgearCards(row[0], row[2], row[3], row[16], row[5], row[13]))
            #elif row[3] == "Footgear":
                #treasureCardsStack.append(FootgearCards(row[0], row[2], row[3], row[16], row[5], row[13]))
            #elif row[3] == "Armour":
                #treasureCardsStack.append(ArmourCards(row[0], row[2], row[3], row[16], row[5], row[13]))
            #elif row[3] == "GUAL":
                #treasureCardsStack.append(LevelCards(row[0], row[2], row[3], row[16], row[5], row[13]))
                
    
                
print(treasureCardsStack) 
print(doorCardsStack) 


""" Questions
    - Dictreader does not work when using it on search function.
    - If a class inherit from another class which takes parameters, will you then have to add the parameters from
    parent class when creating and instans of the sub class? Better to destroy root class and then have door and treasure as root? 
    - Class parameter as method. Best way? e.g. BadStuff, CurseEffect. 
    - Footgear, headgear armour, level up cards and so on, has no special parameters. Should it just use the enum to identify itself?
"""
