from random import randint
import prompt
from brain_games.cli import welcome_user


def generate():
    num1 = randint(0, 10)
    step = randint(0, 10)
    progression = ['Question:', num1]
    for i in range(1, 10):
        progression.append(num1 + (step * i))
    ans_index = randint(0, 9)
    ans = progression[ans_index]
    progression[ans_index] = '..'
    return progression, ans


def process_game():
    res = 0
    while res < 3:
        question, ans = generate()
        for i in question:
            print(i, end=' ')
        player_answer = prompt.integer(prompt="Your answer: ")
        if player_answer == ans:
            res += 1
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer;(. "
                  f"Correct answer was '{ans}'.")
            return False
    return True


def main():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
    name = welcome_user()
    if process_game():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
