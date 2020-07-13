from random import randint


def generate():
    num1 = randint(0, 10)
    step = randint(0, 10)
    progression = ['Question:', num1]
    for i in range(1, 10):
        progression.append(num1 + (step * i))
    ans_index = randint(0, 9)
    ans = progression[ans_index]
    progression[ans_index] = '..'
    que = ''
    for i in progression:
        que += f'{i} '
    greet = 'What number is missing in the progression?'
    return ans, que, greet
