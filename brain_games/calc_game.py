import prompt
from random import randint, choice
from brain_games.cli import welcome_user


def generate():
    num1, num2 = randint(0, 100), randint(0, 100)
    return num1, num2


def process_game():
    res = 0
    signs = ['+', '-', '*']
    while res < 3:
        num1, num2 = generate()
        sign = choice(signs)
        if sign == '+':
            ans = num1 + num2
            print(f'Question: {num1} + {num2}')
        elif sign == '-':
            ans = num1 - num2
            print(f'Question: {num1} - {num2}')
        else:
            ans = num1 * num2
            print(f'Question: {num1} * {num2}')
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
    print('What is the result of the expression?')
    name = welcome_user()
    if process_game():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")