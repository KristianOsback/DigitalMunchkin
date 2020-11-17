import Cards_Samlet
from Player_class import Player
import random

"""
A. Turn is not started
B. In fight
C. Bnd part of turn
D. Fight ended with victory
E. Fight ended with defeat
F. Fleeing
G. Dead
H. Turn is ended
"""


Computer = Player()
P1 = Player #Will later be created in the main game. 
Players = [Computer, P1]

PlayerTurn = Players[0]
presentState = "A"
partOfTurn = 0 #Can be 0 if turn is not started, 1 if you have drawn a door card, and 2 if you have both drawn a door card and fought/searched room.


Nodes = ["A", "B", "C", "D", "E", "F", "G", "H"] #Stages
Edges = [("A", "B"), ("A", "C"), ("C", "C"), ("C", "B"),
         ("C", "H"), ("B", "B"), ("B", "D"), ("B", "E"),
         ("D", "D"), ("D", "H"), ("E", "E"), ("E", "F"),
         ("F", "F"), ("F", "G"), ("F", "H"), ("G", "H")] #Connections

ConnectionList = { #graph
    "A":["B", "C"],
    "B":["B", "D", "E"],
    "C":["C", "B", "H"],
    "D":["D", "H", ],
    "E":["E", "F"],
    "F":["F", "G", "H"],
    "G":["H"],
    "H":[]  
}

doorCardStartTurn = random.choice(Cards_Samlet.doorCardsStack)
partOfTurn = 1
if doorCardStartTurn(cardType) == monster: #read card
    partOfTurn = 2
    presentState = "B"
    print(PlayerTurn[handCards]) #read card
        
else:
    presentState = "C"





print(ConnectionList)
print(Players)
