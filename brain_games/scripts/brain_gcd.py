from .brain_games import main
from ..cli import welcome_user, process_gcd_game


def gcd_game():
    main()
    print('Find the greatest common divisor of given numbers.')
    name = welcome_user()
    if process_gcd_game():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    gcd_game()
