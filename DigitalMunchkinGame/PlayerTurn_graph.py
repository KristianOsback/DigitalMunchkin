from typing import List

from Cards_Samlet import *
from Player_class import Player
from random import randrange, shuffle
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

class Game:
    def __init__(self, players, door_stack: List[Cards], treasure_stack: List[Cards]):

        self.players = players
        self.door_stack = door_stack
        self.treasure_stack = treasure_stack
        # self.door_card_in_play = door_card_in_play
        self.door_discard: List[DoorCards] = []
        self.treasure_discard: List[TreasureCards] = []
        self.active_player: Player = self.players[0]
        self.player_number_turn = 1
        self.present_state = State.TURN_NOT_STARTED
        self.part_of_turn = 0
        self.game_won = False


    def pick_door_card(self) -> Cards:
        if not self.door_stack:
            self.door_stack = shuffle_deck(self.door_discard)
            self.door_discard = []
        return self.door_stack.pop()

    def pick_treasure_card(self):
        if not self.treasure_stack:
            self.treasure_stack = shuffle_deck(self.treasure_discard)
            self.treasure_discard = []
        return self.treasure_stack.pop()

    def discard(self, card: TreasureCards):
        self.active_player.table_cards.remove(card)  # unwield item
        self.treasure_discard.append(card)  # add it to discard stack

    def replace(self, discard_card: TreasureCards, throw_card: TreasureCards):
        self.active_player.replace_card(discard_card, throw_card)  # place card
        self.treasure_discard.append(discard_card)

    def change_player(self):
        if len(self.players) > self.player_number_turn:
            self.player_number_turn += 1
            self.active_player = self.players[self.player_number_turn - 1]

        else:
            self.active_player = self.players[0]
            print("Next player turn!")
            test = self.check_for_win()
            if test is not False:
                self.player_turn_calc()

        winner = self.check_for_win()
        if winner:
            print(f"Congratulation! {winner.name} won the game!")
        else:
            print("Next player turn!")
            self.player_turn_calc()


    def check_for_win(self):
        for player in self.players:
            if player.level >= 10:
                return player

    def check_activeplayer_cards(self):
        discards = self.active_player.throw_better_cards()
        self.treasure_discard.extend(discards)

    def calculate_monsterfight(self, monstercard: MonsterCards):
        self.present_state = State.IN_FIGHT
        for card in self.active_player.hand_cards:
            print(card.cardName)  # read card
            self.check_activeplayer_cards()
        if monstercard.monsterLevel < self.active_player.level:
            print("Victory!")
            self.active_player.level = self.active_player.level + 1
            self.active_player.level_total = self.active_player.level_total + 1
            self.active_player.hand_cards.append(self.pick_treasure_card())
            self.present_state = State.FIGHT_WICTORY
            self.check_activeplayer_cards()
            self.present_state = State.TURN_ENDED
        else:
            self.present_state = State.FIGHT_DEFEAT
            dice = randrange(1, 7)
            self.present_state = State.FLEEING
            if dice > monstercard.run_away:
                self.present_state = State.TURN_ENDED
            else:
                self.present_state = State.DEAD
                print("You are dead!")
                discards = self.active_player.die()
                self.discard_cards(discards)
            self.change_player()

    def player_turn_calc(self):
        door_card_in_play: Cards = self.pick_door_card()
        self.part_of_turn = 1
        if isinstance(door_card_in_play, MonsterCards):  # read card
            self.part_of_turn = 2
            self.calculate_monsterfight(door_card_in_play)
        elif isinstance(door_card_in_play, CurseCards):
            self.present_state = State.SECOND_PART_OF_TURN
            print(door_card_in_play.curseEffect)  # read card
        else:
            self.present_state = State.SECOND_PART_OF_TURN
            self.active_player.hand_cards.append(door_card_in_play)
            self.check_activeplayer_cards()
            for card in self.active_player.hand_cards:
                if isinstance(card, MonsterCards):
                    self.calculate_monsterfight(card)
            else:
                print("You search the room")
                self.pick_door_card()
                self.check_activeplayer_cards()
                self.present_state = State.TURN_ENDED
                self.change_player()

    def discard_cards(self, discards):
        raise NotImplemented()


#playerhandler der er computer, en der er menneske, en random.
#bryd ned i mulige actions


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

def shuffle_deck(cards: List[Cards]) -> List[Cards]:
    return shuffle(cards) if cards else []