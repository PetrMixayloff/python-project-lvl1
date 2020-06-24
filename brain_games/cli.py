from random import randint
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    return name


def generate():
    num = randint(0, 100)
    ans = 'yes' if num % 2 == 0 else 'no'
    return num, ans


def process_game():
    res = 0
    while res < 3:
        num, ans = generate()
        print(f'Question: {num}')
        player_answer = prompt.regex(pattern="^(yes|no)$", prompt="Your answer: ")
        if player_answer.string == ans:
            res += 1
            print('Correct!')
        else:
            print(f"'{player_answer.string}' is wrong answer;(. Correct answer was '{ans}'.")
            return False
    return True
