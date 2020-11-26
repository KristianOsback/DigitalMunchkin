import Cards_Samlet
from Player_class import Player
from random import randrange, choice

from enum import Enum, auto

class State(Enum):
    """
    A. Turn is not started
    B. In fight
    C. 2nd part of turn
    D. Fight ended with victory
    E. Fight ended with defeat
    F. Fleeing
    G. Dead
    H. Turn is ended
    """

    TURN_NOT_STARTED = auto()
    IN_FIGHT = auto()
    SECOND_PART_OF_TURN = auto()
    FIGHT_WICTORY = auto()
    FIGHT_DEFEAT = auto()
    FLEEING = auto()
    DEAD = auto()
    TURN_ENDED = auto()

class DrawDoorCard:

    def do_action(self, game):
        card = game.door_stack.pop()
        game.active_player.add_card(card)


class Game:
    def __init__(self):

        self.players = [Player(), Player()]
        self.active_player = self.players[0]
        self.present_state = State.TURN_NOT_STARTED
        self.door_stack =
        self.treasure_stack
        self.door_discard
        self.treasure_discard

    def possible_actions(self):
        if self.present_state == State.TURN_NOT_STARTED:
            yield DrawDoorCard()

    def do_action(self, action):
        if self.present_state == State.TURN_NOT_STARTED:
            draw_door_card #liste af mulige actions.
class PlayerHandler:
    def choose_one(self, game, actions):

        #playerhandler der er computer, en der er menneske, en random.
        #bryd ned i mulige actions




playerInput = 0

Computer = Player
P1 = Player  # Will later be created in the main game.
Players = [Computer, P1]
player_turn = Players[0]

present_state = "A"
partOfTurn = 0
# partOfTurn can be:
# 0 if turn is not started,
# 1 if you have drawn a door card,
# 2 if you have both drawn a door card and fought/searched room.

#Nodes and their edges
Nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
Edges = [("A", "B"), ("A", "C"), ("C", "C"), ("C", "B"),
         ("C", "H"), ("B", "B"), ("B", "D"), ("B", "E"),
         ("D", "D"), ("D", "H"), ("E", "E"), ("E", "F"),
         ("F", "F"), ("F", "G"), ("F", "H"), ("G", "H")]  # Connections

# graph
ConnectionList = {
    "A": ["B", "C"],
    "B": ["B", "D", "E"],
    "C": ["C", "B", "H"],
    "D": ["D", "H", ],
    "E": ["E", "F"],
    "F": ["F", "G", "H"],
    "G": ["H"],
    "H": []
}

def calculate_monsterfight():
    present_state = "B"
    for cards in player_turn.hand_cards:
        print(player_turn.hand_cards.name)  # read card
        player_turn.check_all_handcards()
    if door_card_in_play.monsterLevel < player_turn.level:
        print("Victory!")
        player_turn.level = player_turn.level + 1
        player_turn.level_total = player_turn.level_total + 1
        player_turn.hand_cards.append(player_turn.pick_card(Cards_Samlet.Cards.treasureCardsStack))
        present_state = "D"
        player_turn.check_all_handcards()
        present_state = "H"
    else:
        present_state = "E"
        dice = randrange(1, 7)
        present_state = "F"
        if dice > door_card_in_play.run_away:
            present_state = "H"
        else:
            present_state = "G"
            print("You are dead!")
            player_turn.level = 1
            player_turn.level_total = 1
            player_turn
    player_turn = "Next_player"


door_card_in_play = player_turn.throw_and_play_door_card()
partOfTurn = 1
if door_card_in_play.cardType == "Monster":  # read card
    partOfTurn = 2
    calculate_monsterfight()

elif door_card_in_play.cardType == "curse":
    present_state = "C"
    print(door_card_in_play.curseEffect)  # read card

else:
    present_state = "C"
    player_turn.hand_cards.append(door_card_in_play)
    player_turn.check_all_handcards()
    for card in player_turn.hand_cards:
        if any card.cardtype: == "Monster":
            door_card_in_play = player_turn.throw_and_play_door_card()
            calculate_monsterfight()
        else:
            print("You search the room")
            player_turn.pick_card(Cards_Samlet.Cards.doorCardsStack)
            player_turn.check_all_handcards()
            present_state = "H"

"""
doorCardStartTurn = random.choice(Cards_Samlet.Cards.doorCardsStack)
partOfTurn = 1
if doorCardStartTurn.cardType == "monster": #read card
    partOfTurn = 2
    presentState = "B"
    print(PlayerTurn.handCards.) #read card
    playerInput = input("Click 1 to throw card, click 2 to fight, click 3 to flee")
    while playerInput
        
else:
    presentState = "C"
"""

# print(ConnectionList)
# print(Players)
