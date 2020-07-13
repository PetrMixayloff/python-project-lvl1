from brain_games.games.even_game import generate
from ..flow import game_flow


def even_game():
    answer, question, greeting = generate()
    game_flow(answer, question, greeting)


if __name__ == '__main__':
    even_game()
