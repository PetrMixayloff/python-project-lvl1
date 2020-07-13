from random import randint, choice


def generate():
    num1, num2 = randint(0, 100), randint(0, 100)
    signs = ['+', '-', '*']
    sign = choice(signs)
    if sign == '+':
        ans = num1 + num2
    elif sign == '-':
        ans = num1 - num2
    else:
        ans = num1 * num2
    que = f'Question: {num1} {sign} {num2}'
    greet = 'What is the result of the expression?'
    return ans, que, greet
