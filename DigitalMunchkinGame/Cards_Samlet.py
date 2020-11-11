from enum import Enum #auto can auto number them.

class CardType(Enum):
    """The different cardtypes like monstercards, headgear, curses ect."""
    
    monsterCard = "Monster"
    curseCard = "Curse"
    steedCard = "Steed"
    hirelingCard = "Hireling"
    classCard = "Class"
    breedCard = "Breed"
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
    cardStack = list()
    discardStack = list()
    
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
     
    def __init__(self, monsterLevel, badStuff): 
        """Initializes the data."""
        
        self.monsterLevel = monsterLevel
        self.badStuff = badStuff
        print("(Initializing {})".format(self.monsterLevel))
        print("(Initializing {})".format(self.badStuff))
        
        
class CurseCards(Cards):    
     
    def __init__(self, curseEffect): 
        """Initializes the data."""
        
        self.curseEffect = curseEffect
        print("(Initializing {})".format(self.curseEffect))
        

class SteedCards(Cards):    
     
    def __init__(self, bonus, talking, flying, fireBreathing): 
        """Initializes the data."""
        
        self.bonus = bonus
        self.talking = talking
        self.flying = flying
        self.fireBreathing = fireBreathing
        print("(Initializing {})".format(self.bonus))
        print("(Initializing {})".format(self.talking))
        print("(Initializing {})".format(self.flying))
        print("(Initializing {})".format(self.fireBreathing))
        

class HirelingCards(Cards):    
     
    def __init__(self, hirelingBonus): 
        """Initializes the data."""
        
        self.hirelingBonus = hirelingBonus
        print("(Initializing {})".format(self.hirelingBonus))
   
   
class ClassCards(Cards):    
     
    def __init__(self, specialSkill): 
        """Initializes the data."""
        
        self.specialSkill = specialSkill
        print("(Initializing {})".format(self.specialSkill))
    
    
class BreedCards(Cards):    
     
    def __init__(self, specialSkill): 
        """Initializes the data."""
        
        self.specialSkill = specialSkill
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
     
    def __init__(self, cardType): 
        """Initializes the data."""
     

class MonsterboosterCards(Cards):    
     
    def __init__(self, boost): 
        """Initializes the data."""
        
        self.boost = boost
        print("(Initializing {})".format(self.boost))
        
        
class BoostCards(Cards):    
     
    def __init__(self, specialEffect): 
        """Initializes the data."""
        
        self.specialEffect = specialEffect
        print("(Initializing {})".format(self.specialEffect))
        
        
#Card1 = Cards(1, "Bi Polar Bear", CardType.monsterCard, "He cannot decide to battle or not") #create card


#SearchCard()

""" Questions
    - Dictreader does not work when using it on search function.
    - If a class inherit from another class which takes parameters, will you then have to add the parameters from
    parent class when creating and instans of the sub class? Better to destroy root class and then have door and treasure as root? 
    - Class parameter as method. Best way? e.g. BadStuff, CurseEffect. 
    - Footgear, headgear armour, level up cards and so on, has no special parameters. Should it just use the enum to identify itself?
"""
