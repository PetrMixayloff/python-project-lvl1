from random import randint


def generate():
    num1, num2 = a, b = randint(0, 100), randint(0, 100)
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    ans = a if a != 0 else b
    que = f'Question: {num1} {num2}'
    greet = 'Find the greatest common divisor of given numbers.'
    return ans, que, greet
