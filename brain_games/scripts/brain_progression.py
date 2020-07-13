from brain_games.games.progression_game import generate
from ..flow import game_flow


def progression_game():
    answer, question, greeting = generate()
    game_flow(answer, question, greeting)


if __name__ == '__main__':
    progression_game()
