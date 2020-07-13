from brain_games.games.calc_game import generate
from ..flow import game_flow


def calc_game():
    answer, question, greeting = generate()
    game_flow(answer, question, greeting)


if __name__ == '__main__':
    calc_game()
