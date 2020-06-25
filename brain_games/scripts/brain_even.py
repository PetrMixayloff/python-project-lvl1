from .brain_games import main
from ..cli import *


def even_game():
	main()
	print('Answer "yes" if number even otherwise answer "no".')
	name = welcome_user()
	if process_even_game():
		print(f'Congratulations, {name}!')
	else:
		print(f"Let's try again, {name}!")


if __name__ == '__main__':
	even_game()
