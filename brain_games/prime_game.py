from random import randint
from brain_games.cli import welcome_user, is_prime
import prompt


def generate():
    num = randint(2, 100)
    if is_prime(num):
        ans = 'yes'
    else:
        ans = 'no'
    return num, ans


def process_game():
    res = 0
    while res < 3:
        num, ans = generate()
        print(f'Question: {num}')
        player_answer = prompt.regex(pattern="^(yes|no)$",
                                     prompt="Your answer: ")
        if player_answer.string == ans:
            res += 1
            print('Correct!')
        else:
            print(f"'{player_answer.string}' is wrong answer;(. "
                  f"Correct answer was '{ans}'.")
            return False
    return True


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = welcome_user()
    if process_game():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
