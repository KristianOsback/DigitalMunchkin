from Cards_Samlet import Cards
from PlayerTurn_graph import Game
from Player_class import Player, Table, Gender
from enum import Enum, auto


class PlayerType(Enum):
    """
    C = Computer
    H = Human
    """

    COMPUTER = "Computer"
    HUMAN = "Human"


class WelcomeAndStarting:

    def __init__(self):
        """Initializes the data."""

        self.door_stack = None
        self.treasure_stack = None

    def start_game(self):
        print("Welcome to Digital Munchkin!")
        print("First let me know a bit about the first player.")
        p1info = self.create_player(self)
        first_player_name = p1info[0]
        first_player_type = p1info[1]
        first_player_gender = p1info[2]

        print("Then let me know a bit about the second player.")
        p2info = self.create_player(self)
        second_player_name = p2info[0]
        second_player_type = p2info[1]
        second_player_gender = p2info[2]

        return (first_player_name, first_player_type, first_player_gender, second_player_name, second_player_type, second_player_gender)

    def create_player(self):

        player_name = input("Write your name.")
        p_type = input("Click C for computer, H for human.")
        if p_type == "C":
            player_type = PlayerType.COMPUTER
        else:
            player_type = PlayerType.HUMAN
        p_gender = input("Click M for computer, F for human.")
        if p_gender == "M":
            player_gender = Gender.MALE
        else:
            player_gender = Gender.FEMALE
        player_info = [player_name, player_type, player_gender]
        return player_info

    def prepare_game(self,):
        for card in Cards.door_cards_stack:
            door_stack = [card]

        for card in Cards.treasure_cards_stack:
            treasure_stack = [card]
        return door_stack, treasure_stack

    def actual_game(self):
        self.prepare_game()
        player_info = self.start_game(WelcomeAndStarting)
        p1 = Player(player_info[0], player_info[1], player_info[2])
        p2 = Player(player_info[3], player_info[4], player_info[5])
        the_game = Game(p1, p2)
        the_game.player_turn_calc()

    def actual_game_TEST(self):
        stacks = self.prepare_game(self)
        card_in_play = Game.pick_card(Game, stacks[1])
        p1 = Player("Tester1", PlayerType.COMPUTER, Gender.MALE)
        p2 = Player("Tester2", PlayerType.COMPUTER, Gender.FEMALE)
        the_game = Game(p1, p2, stacks[0], stacks[1], card_in_play)
        the_game.player_turn_calc()

WelcomeAndStarting.actual_game_TEST(WelcomeAndStarting)





