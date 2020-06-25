from .brain_games import main
from ..cli import *


def calc_game():
	main()
	print('What is the result of the expression?')
	name = welcome_user()
	if process_calc_game():
		print(f'Congratulations, {name}!')
	else:
		print(f"Let's try again, {name}!")


if __name__ == '__main__':
	calc_game()
