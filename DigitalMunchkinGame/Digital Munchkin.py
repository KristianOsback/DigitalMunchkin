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

class Prepare_decks:

    def __init__(self):
        """Initializes the data."""

        self.door_stack = []
        self.treasure_stack = []

    def prepare_game(self,):
        for card in Cards.door_cards_stack:
            self.door_stack.append(card)

        for card in Cards.treasure_cards_stack:
            self.treasure_stack.append(card)
        return self.door_stack, self.treasure_stack

class WelcomeAndStarting:

    def start_game(self):
        print("Welcome to Digital Munchkin!")
        print("First let me know a bit about the first player.")
        p1info = self.create_player()
        first_player_name = p1info[0]
        first_player_type = p1info[1]
        first_player_gender = p1info[2]

        print("Then let me know a bit about the second player.")
        p2info = self.create_player()
        second_player_name = p2info[0]
        second_player_type = p2info[1]
        second_player_gender = p2info[2]

        return first_player_name, first_player_type, first_player_gender, second_player_name, second_player_type, second_player_gender

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

    def actual_game(self):
        stacks = self.prepare_game(self)
        card_in_play = Game.pick_card(Game, stacks[1])
        player_info = self.start_game(WelcomeAndStarting)
        p1 = Player(player_info[0], player_info[1], player_info[2])
        p2 = Player(player_info[3], player_info[4], player_info[5])
        the_game = Game(p1, p2, stacks[0], stacks[1], card_in_play)
        the_game.player_turn_calc()

    def actual_game_TEST(self):
        decks = Prepare_decks()
        prepare = decks.prepare_game()
        game = Game()
        card_in_play = game.pick_card(prepare[0], game.door_discard)
        p1 = Player("Tester1", PlayerType.COMPUTER, Gender.MALE)
        p2 = Player("Tester2", PlayerType.COMPUTER, Gender.FEMALE)
        the_game = Game(p1, p2, prepare[0], prepare[1], card_in_play)
        the_game.player_turn_calc()



WelcomeAndStarting().start_game()
game = WelcomeAndStarting.actual_game_TEST(WelcomeAndStarting)


