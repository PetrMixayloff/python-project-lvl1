from brain_games.cli import welcome_user
from random import randint
import prompt


def generate():
    num1, num2 = a, b = randint(0, 100), randint(0, 100)
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    gcd = a if a != 0 else b
    return num1, num2, gcd


def process_game():
    res = 0
    while res < 3:
        num1, num2, ans = generate()
        print(f'Question: {num1} {num2}')
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
    print('Find the greatest common divisor of given numbers.')
    name = welcome_user()
    if process_game():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
