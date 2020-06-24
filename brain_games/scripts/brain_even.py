from .brain_games import main
from ..cli import *


def game():
	main()
	name = welcome_user()
	if process_game():
		print(f'Congratulations, {name}!')
	else:
		print(f"Let's try again, {name}!")


if __name__ == '__main__':
	game()
