from random import randint


def generate():
    num1 = randint(0, 10)
    step = randint(0, 10)
    progression = ['Question:', num1]
    for i in range(1, 10):
        progression.append(num1 + (step * i))
    answer_index = randint(0, 9)
    answer = progression[answer_index]
    progression[answer_index] = '..'
    question = ''
    for i in progression:
        question += f'{i} '
    return answer, question
