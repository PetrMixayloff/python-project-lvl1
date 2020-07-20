from random import randint


PROGRESSION_LENGTH = 9
DESCRIPTION = 'What number is missing in the progression?'


def generate():
    num = randint(0, 10)
    step = randint(1, 10)
    progression = []
    for i in range(0, PROGRESSION_LENGTH):
        progression.append(num + (step * i))
    answer_index = randint(0, PROGRESSION_LENGTH - 1)
    answer = progression[answer_index]
    progression[answer_index] = '..'
    question = ''
    for i in progression:
        question += f'{i} '
    return answer, question
