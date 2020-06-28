from .brain_games import main
from ..cli import welcome_user, process_prime_game


def prime_game():
    main()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = welcome_user()
    if process_prime_game():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    prime_game()
