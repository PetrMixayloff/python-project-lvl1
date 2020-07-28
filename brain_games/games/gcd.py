from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a if a != 0 else b


def generate_data():
    num1, num2 = randint(0, 100), randint(0, 100)
    answer = find_gcd(num1, num2)
    question = f'{num1} {num2}'
    return answer, question
