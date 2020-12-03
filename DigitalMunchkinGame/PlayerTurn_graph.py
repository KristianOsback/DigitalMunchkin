from Cards_Samlet import Cards
from Player_class import Player, Table
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
        return card

class Game:
    def __init__(self):

        self.players = [Player(), Player()]
        self.active_player = self.players[0]
        self.present_state = State.TURN_NOT_STARTED
        self.partOfTurn = 0
        self.door_stack = []
        self.treasure_stack = []
        self.door_discard = []
        self.treasure_discard = []
        self.active_player = self.players[0]
        self.door_card_in_play = DrawDoorCard.do_action(self)

    def pick_card(self, stack):
        card = choice(stack)
        self.active_player.hand_cards.append(card)  # add it to hans
        stack.remove(card)  # remove it from stack
        return card

    def throw_and_play_door_card(self):
        card = choice(Cards.doorCardsStack)
        Cards.doorCardsStack.remove(card)  # remove it from stack
        return card

    def discard(self, card):
        Cards.treasureCardsDiscardStack.append(card)  # add it to discard stack
        self.active_player.table_cards.remove(card)  # unwield item

    def throw_card(self, card):
        self.active_player.table_cards.append(card)  # wield new item
        self.active_player.hand_cards.remove(card)  # remove from handcards

    def replace(self, discard_card, throw_card):
        self.discard(discard_card.cardType)  # discard card
        self.throw_card(throw_card)  # place card

    def check_hand_cards(self, cardtype, item):
        # cardtype should be a string with 1 uppercase word, like: Armour
        for card in self.active_player.hand_cards:
            if card.cardType == cardtype:  # looking through hand cards searching for a weapon
                if card.levelBonus > item.itembonus:  # is it better than what you are wielding?
                    self.replace(item, card)
            else:
                print(f"No {cardtype} cards on hand")

    def check_weapon_cards(self):  # cardtype should be a string with 1 upercase word, like: Armour
        worst_weapon = None
        if self.active_player.table_cards.hands_l.levelBonus > self.active_player.table_cards.weapon_r.levelBonus:
            worst_weapon = self.active_player.table_cards.weapon_r.levelBonus
        else:
            worst_weapon = self.active_player.table_cards.weapon_l.levelBonus
        for card in self.active_player.hand_cards:
            if card.cardType == "Weapon":  # looking through hand cards searching for a weapon
                if card.levelBonus > worst_weapon.itembonus:  # is it better than what you are wielding?
                    self.replace(worst_weapon, card)
            else:
                print(f"No weapon cards on hand")

    def check_all_handcards(self):
        self.check_hand_cards("Armour", self.active_player.table_cards.armour)
        self.check_hand_cards("Headgear", self.active_player.table_cards.headgear)
        self.check_hand_cards("Footgear", self.active_player.table_cards.footgear)
        self.check_weapon_cards()

    def possible_actions(self):
        if self.present_state == State.TURN_NOT_STARTED:
            yield DrawDoorCard()

    def do_action(self, action):
        if self.present_state == State.TURN_NOT_STARTED:
            self.draw_door_card() #liste af mulige actions.

    def calculate_monsterfight(self):
        present_state = "B"
        for card in self.active_player.hand_cards:
            print(card.name)  # read card
            self.check_all_handcards()
        if self.door_card_in_play.monsterLevel < self.active_player.level:
            print("Victory!")
            self.active_player.level = self.active_player.level + 1
            self.active_player.level_total = self.active_player.level_total + 1
            self.active_player.hand_cards.append(self.pick_card(Cards.treasureCardsStack))
            present_state = "D"
            self.check_all_handcards()
            present_state = "H"
        else:
            present_state = "E"
            dice = randrange(1, 7)
            present_state = "F"
            if dice > self.door_card_in_play.run_away:
                present_state = "H"
            else:
                present_state = "G"
                print("You are dead!")
                self.active_player.level = 1
                self.active_player.level_total = 1
                self.active_player
        player_turn = "Next_player"

    def player_turn_calc(self):
        door_card_in_play = self.throw_and_play_door_card()
        part_of_turn = 1
        if door_card_in_play.cardType == "Monster":  # read card
            part_of_turn = 2
            self.calculate_monsterfight()

        elif door_card_in_play.cardType == "curse":
            present_state = "C"
            print(door_card_in_play.curseEffect)  # read card

        else:
            present_state = "C"
            self.active_player.hand_cards.append(door_card_in_play)
            self.check_all_handcards()
            for card in self.active_player.hand_cards:
                if any(card.cardtype == "Monster"):
                    self.door_card_in_play = self.throw_and_play_door_card()
                    self.calculate_monsterfight()
            else:
                print("You search the room")
                self.pick_card(Cards.doorCardsStack)
                self.check_all_handcards()
                present_state = "H"
 
class PlayerHandler:
   def choose_one(self, game, actions):



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
