from random import randint


def generate():
    num = randint(0, 100)
    ans = 'yes' if num % 2 == 0 else 'no'
    que = f'Question: {num}'
    greet = 'Answer "yes" if number even otherwise answer "no".'
    return ans, que, greet
