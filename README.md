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

[Card loading](https://github.com/KristianOsback/DigitalMunchkin/blob/main/DigitalMunchkinGame/Cards_Samlet.py#L171-L208)

As mentioned before, all my cards is kept in csv files from where they are loaded to a list. Each card is loaded and saved as an object depending of the type of cards and split in door cards and treasure cards. 

[The state machine (my graph)](https://github.com/KristianOsback/DigitalMunchkin/blob/main/DigitalMunchkinGame/PlayerTurn_graph.py#L196-L213)

The graph is the foundation of my it keeps track of all the state through a player turn. It consist of nodes which each is a state you can be in a long the player turn, and edges that is actions that lead you from one of the states to the next. 
How to come from one state to the other is very different. It can be random depending on which card you receive, by your choice of action or by roling a dice. 

[The game class](https://github.com/KristianOsback/DigitalMunchkin/blob/main/DigitalMunchkinGame/PlayerTurn_graph.py#L34-L179)

This class is very big that it keeps all the functions to actually run the game. Almost all actions and events through the game is based on one or more methods of this class.

## Perspectivation

I think I have builded the game very well but possible updates and fixes could be: 

- More different kind of cards: It has been necessary to focus on the most basic cards, but in the real game there is a long list of special cards. 
- Better handling of "Bad Stuff" from monster cards: Monster cards has very individual Bad Stuff. Bad Stuff is what happens when you lose a fight and fails to flee. In my game i have been only handling all of them as death which is a bit harsh that it means loosing all your stuff and levels. 
- Handling of curses: All curses are individual and again that complicate things very much. Right now you are told which consequence that the curse has but it is not automatically executed. 
- Adding expantions like steeds: Steeds is one of the most cool expansions. The original idea was to include them, but including them means new cards, both treasures and door cards, which new special abilities, add ons to each cards and new bonusses in fight. 

## Conclusion

I think the game itself is great. It works well with many special features. I achieved a lot of the tasks that I had planned and think it is very well. I have has to change my plan some times in the process but I have learned a lot about python coding and think the results end well according to my expectations. 