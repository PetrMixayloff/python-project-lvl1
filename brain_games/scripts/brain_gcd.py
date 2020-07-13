from brain_games.games.gcd_game import generate
from ..flow import game_flow


def gcd_game():
    answer, question, greeting = generate()
    game_flow(answer, question, greeting)


if __name__ == '__main__':
    gcd_game()
