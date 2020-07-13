from random import randint
from brain_games.cli import is_prime


def generate():
    num = randint(2, 100)
    if is_prime(num):
        ans = 'yes'
    else:
        ans = 'no'
    que = f'Question: {num}'
    greet = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return ans, que, greet
