from brain_games.games.prime_game import generate
from ..flow import game_flow


def prime_game():
    answer, question, greeting = generate()
    game_flow(answer, question, greeting)


if __name__ == '__main__':
    prime_game()
