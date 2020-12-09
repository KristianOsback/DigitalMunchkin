from Cards_Samlet import Cards
from Player_class import Player, Table
from random import randrange, choice, shuffle
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
    def __init__(self, p1=None, p2=None, door_stack=None, treasure_stack=None, door_card_in_play=None, door_discard=None, treasure_discard=None):

        self.players = [p1,  p2]
        self.door_stack = door_stack
        self.treasure_stack = treasure_stack
        self.door_card_in_play = door_card_in_play
        self.door_discard = door_discard or []
        self.treasure_discard = treasure_discard or []
        self.active_player = self.players[0]
        self.player_number_turn = 1
        self.present_state = State.TURN_NOT_STARTED
        self.part_of_turn = 0
        self.game_won = False

    def shuffle_stack(self, stack):
        if len(stack) > 0:
            print("Stack is not empty!")
        else:
            shuffle(stack)
            return stack

    def pick_card(self, stack, discard_stack):
        if not stack:
            self.shuffle_stack(discard_stack)
            stack.append(discard_stack)
            discard_stack = []
            card = stack.pop()
            return card
        else:
            discard_stack.append(stack.pop(0))
            if not stack:
                self.shuffle_stack(discard_stack)
                stack.append(discard_stack.pop())
            card = stack.pop()
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

    def change_player(self):
        if len(self.players) > self.player_number_turn:
            self.player_number_turn += 1
            self.active_player = self.players[self.player_number_turn - 1]
            print("Next player turn!")
            test = self.check_for_win()
            if test is not False:
                self.player_turn_calc()
        else:
            self.active_player = self.players[0]
            print("Next player turn!")
            test = self.check_for_win()
            if test is not False:
                self.player_turn_calc()

    def check_for_win(self):
        for player in self.players:
            if player.level >= 10:
                print(f"Congratulation! {player.name} won the game!")
                return True
                input("Play again?")
            else:
                return False

    def check_hand_cards(self, cardtype, item):
        # cardtype should be a string with 1 uppercase word, like: Armour
        for card in self.active_player.hand_cards:
            if card.cardType == cardtype:  # looking through hand cards searching for a weapon
                if item is None:
                    item = card
                else:
                    if card.levelBonus > item.levelBonus:  # is it better than what you are wielding?
                        self.replace(item, card)
            else:
                print(f"No {cardtype} cards on hand")

    def check_weapon_cards(self):  # cardtype should be a string with 1 upercase word, like: Armour
        worst_weapon = None
        for card in self.active_player.hand_cards:
            if (card.cardType == "Weapon"):  # looking through hand cards searching for a weapon
                if self.active_player.table_cards.weapon_l is None:
                    self.active_player.table_cards.weapon_l = card
                else:
                    if self.active_player.table_cards.weapon_l.levelBonus > self.active_player.table_cards.weapon_r.levelBonus:
                        worst_weapon = self.active_player.table_cards.weapon_r
                    else:
                        worst_weapon = self.active_player.table_cards.weapon_l
                    for card in self.active_player.hand_cards:
                        if card.levelBonus > worst_weapon.itembonus:  # is it better than what you are wielding?
                            self.replace(worst_weapon, card)
            else:
                print(f"No weapon cards on hand")

    def check_all_handcards(self):
        self.check_hand_cards("Armour", self.active_player.table_cards.armour)
        self.check_hand_cards("Headgear", self.active_player.table_cards.head)
        self.check_hand_cards("Footgear", self.active_player.table_cards.foot)
        self.check_weapon_cards()

    def do_action(self, action):
        if self.present_state == State.TURN_NOT_STARTED:
            self.pick_card(self.door_stack) #liste af mulige actions.

    def calculate_monsterfight(self):
        self.present_state = State.IN_FIGHT
        for card in self.active_player.hand_cards:
            print(card.name)  # read card
            self.check_all_handcards()
        if self.door_card_in_play.monsterLevel < self.active_player.level:
            print("Victory!")
            self.active_player.level = self.active_player.level + 1
            self.active_player.level_total = self.active_player.level_total + 1
            self.active_player.hand_cards.append(self.pick_card(self.treasure_stack))
            self.present_state = State.FIGHT_WICTORY
            self.check_all_handcards()
            self.present_state = State.TURN_ENDED
        else:
            self.present_state = State.FIGHT_DEFEAT
            dice = randrange(1, 7)
            self.present_state = State.FLEEING
            if dice > self.door_card_in_play.run_away:
                self.present_state = State.TURN_ENDED
            else:
                self.present_state = State.DEAD
                print("You are dead!")
                self.players[self.player_number_turn - 1] = Player()
                self.players.remove(self.active_player)
            self.change_player()

    def player_turn_calc(self):
        self.part_of_turn = 1
        if self.door_card_in_play.cardType == "Monster":  # read card
            self.part_of_turn = 2
            self.calculate_monsterfight()
        elif self.door_card_in_play.cardType == "curse":
            self.present_state = State.SECOND_PART_OF_TURN
            print(self.door_card_in_play.curseEffect)  # read card
        else:
            self.present_state = State.SECOND_PART_OF_TURN
            self.active_player.hand_cards.append(self.door_card_in_play)
            self.check_all_handcards()
            for card in self.active_player.hand_cards:
                if card.cardType == "Monster":
                    self.door_card_in_play = self.pick_card(self.door_stack)
                    self.calculate_monsterfight()
            else:
                print("You search the room")
                self.pick_card(self.door_stack, self.door_discard)
                self.check_all_handcards()
                self.present_state = State.TURN_ENDED
                self.change_player()


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
