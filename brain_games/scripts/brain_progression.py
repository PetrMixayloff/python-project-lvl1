from .brain_games import main
from ..cli import welcome_user, process_progression_game


def progression_game():
    main()
    print('What number is missing in the progression?')
    name = welcome_user()
    if process_progression_game():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    progression_game()
