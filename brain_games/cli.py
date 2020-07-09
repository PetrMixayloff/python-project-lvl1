from math import sqrt
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    return name


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True
