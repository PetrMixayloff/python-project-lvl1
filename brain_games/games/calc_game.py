from random import randint, choice
import operator


DESCRIPTION = 'What is the result of the expression?'


def generate():
    num1, num2 = randint(0, 100), randint(0, 100)
    operations = {operator.add(num1, num2): '+',
                  operator.sub(num1, num2): '-',
                  operator.mul(num1, num2): '*'}
    answer = choice(list(operations.keys()))
    question = f'{num1} {operations[answer]} {num2}'
    return answer, question
