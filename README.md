# Digital Munchkin

## Background story

Munchkin is a roleplay card game. It is filled with black humor and is very popular. 
The game itself consist of 2 different card types. Door Cards and Treasure Cards. 
Door Cards is what is running the game, each turn starts with drawing a Door Card. 
Treasure Cards is reward for monsterfight. 
Each player start as human level 1 and is the same gender than the person that plays. 
It is turn based, and players can get levels through figt and GUAL Cards (Go Up A Level). 
First to reach level 10 has won. 

## Introduction to the project

Digital Munchkin is a digitalization of the original card game. 
I have created the game so the cards is loaded from 2 different csv files and afterwards availabel as from a collection (a list). 
When starting the game the cards is transferred to two different stacks, players are created from a combi of a player class with pre-created values and inputs from the players. Players can be created as computers and as human players. 
The game itself is run by a graph which is used as a state machine. It keeps track all the time of where in the states of the player turn that the game is. 

## My motivation 

I am a huge fan of Munchkin. I especially like the humor of the game. That is the reason that it felt natural to create a digital version of the game. 
It is both exiting and has a huge potential to use a lot of different kind of Python code. 

## Main classes. 

The game is put together of a lot of different classes. The main classes is the following: 

### Cards 

The Cards class is the parent class of all my cards. There is a hierachy for all the different card types which each has their own classes that inherit from this class. 

### Player

The Player is used when creatin the players. It keeps track of all their cards, stats, items and so on.  

### Game

The Game class controls the game itself. It consist of a long line of methods that handle cards, is used to do actions in the game and handle monster fights and the player turn itself. 

### WelcomeAndStarting

The WelcomeAndStarting class is the actually class to starts the game. It welcomes the players and take user information like name, gender and type of player (human/computer). 
 
## Special code

There is some of my codes especially that is pretty advanced. 

[The state machine (my graph)](https://github.com/KristianOsback/DigitalMunchkin/blob/main/DigitalMunchkinGame/PlayerTurn_graph.py#L196-L213)