from random import randint


def generate():
    num1, num2 = a, b = randint(0, 100), randint(0, 100)
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    answer = a if a != 0 else b
    question = f'Question: {num1} {num2}'
    return answer, question
