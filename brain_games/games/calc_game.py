from random import randint, choice


def generate():
    num1, num2 = randint(0, 100), randint(0, 100)
    signs = ['+', '-', '*']
    sign = choice(signs)
    if sign == '+':
        answer = num1 + num2
    elif sign == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    question = f'Question: {num1} {sign} {num2}'
    return answer, question
