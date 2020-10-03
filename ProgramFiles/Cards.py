from enum import Enum #auto can auto number them.

totalCardList = []
cardStack = list()
discardStack = list()

class CardType(Enum):
    """The different cardtypes like monstercards, headgear, curses ect."""
    
    monsterCard = "Monster"
    curseCard = "Curse"
    steedCard = "Steed"
    hirelinkCard = "Hireling"
    classCard = "Class"
    

class Cards:
    """The overall card object. Different kind of cards will inherit from this"""
    
    
    Amount = 0
    Left = 0
    
    def __init__(self, cardNumber, cardName, cardType): 
        """Initializes the data."""
        self.cardNumber = cardNumber
        self.cardName = cardName
        self.cardType = cardType
        print("(Initializing {})".format(self.cardNumber))
        print("(Initializing {})".format(self.cardName))
        print("(Initializing {})".format(self.cardType))
        
        global Amount
        Amount += 1 #why does this not work? Will work, måske skal den ændres nu hvor det er class variables. 
        global Left 
        Left += 1 #Counting total cards in deck
        
    def discardCard(self, card, removedFrom): #removedFrom is the list that throws the card. Can be a players hand or the table or the Stack
        """Throw or discard a card"""
        discardStack.append(card) #card is thrown in the discard stack
        removedFrom.pop(card) #card is removed from stack or the players hand or the table
        
Card1 = Cards(1, "Bi Polar Bear", "Monster card") #create card
print(Card1)
print (Amount)
print(Left)
""" Questions
    - The global variables is not recogniced
    - 
    - totalCardList should be a tuple, is best way to create the variable and then assign the data to it afterwards.
    - Card types should be a enumerable (like from c#)
    class Cardtype:
    enums here = cardtype(value)
        def __itnit_
        
        , 
        
"""


    
    
