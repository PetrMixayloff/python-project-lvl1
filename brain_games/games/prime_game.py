from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'


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


def generate():
    num = randint(2, 100)
    if is_prime(num):
        answer = 'yes'
    else:
        answer = 'no'
    question = f'{num}'
    return answer, question
