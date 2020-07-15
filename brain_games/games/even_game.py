from random import randint


def generate():
    num = randint(0, 100)
    answer = 'yes' if num % 2 == 0 else 'no'
    question = f'Question: {num}'
    return answer, question
