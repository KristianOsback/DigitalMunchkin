import PlayerTurn_graph
from Player_class import Gender
from enum import Enum, auto


class PlayerType(Enum):
    """
    C = Computer
    H = Human
    """

    COMPUTER = "ComputerKr"
    HUMAN = "Human"


class WelcomeAndStarting:

    def start_game(self):
        print("Welcome to Digital Munchkin!")
        print("First let me know a bit about the first player.")
        p1 = self.create_player(self)
        first_player_name = p1[0]
        first_player_type = p1[1]
        first_player_gender = p1[2]

        print("Then let me know a bit about the second player.")
        p2 = self.create_player(self)
        second_player_name = p2[0]
        second_player_type = p2[1]
        second_player_gender = p2[2]

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


welcome = WelcomeAndStarting
welcome.start_game(WelcomeAndStarting)


