from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def generate():
    num = randint(0, 100)
    answer = 'yes' if num % 2 == 0 else 'no'
    question = f'{num}'
    return answer, question
