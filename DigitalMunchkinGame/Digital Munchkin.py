from Cards_Samlet import *
from PlayerTurn_graph import Game
from Player_class import Player, Gender, PlayerType


def prepare_game():
    return list([CreateCards().read_door_cards(), CreateCards().read_treasure_cards()])


class WelcomeAndStarting:

    def start_game(self):
        print("Welcome to Digital Munchkin!")
        print("First let me know a bit about the first player.")
        p1 = self.create_player()
        print("Then let me know a bit about the second player.")
        p2 = self.create_player()
        players = [p1, p2]
        return players

    def create_player(self):
        player = Player()
        player.name = input("Write your name.")
        p_type = input("Click C for computer, H for human.")
        if p_type == "C":
            player.type = PlayerType.COMPUTER
        else:
            player.type = PlayerType.HUMAN
        p_gender = input("Click M for Male, F for Female.")
        if p_gender == "M":
            player.gender = Gender.MALE
        else:
            player.gender = Gender.FEMALE
        return player

    def actual_game(self):
        stacks = prepare_game()
        players = self.start_game()
        the_game = Game([players[0], players[1]], stacks[0], stacks[1])
        the_game.active_player = players[0]
        the_game.pick_door_card()
        the_game.decide_player_type()


"""
    def actual_game(self):
        stacks = self.prepare_game(self)
        card_in_play = Game.pick_card(Game, stacks[1])
        player_info = self.start_game(WelcomeAndStarting)
        p1 = Player(player_info[0], player_info[1], player_info[2])
        p2 = Player(player_info[3], player_info[4], player_info[5])
        the_game = Game(p1, p2, stacks[0], stacks[1], card_in_play)
        the_game.player_turn_calc()
"""

The_Game = WelcomeAndStarting()
The_Game.actual_game()

# if __name__ == '__main__':
# game = WelcomeAndStarting()
# game.start_game()
# game.actual_game()


