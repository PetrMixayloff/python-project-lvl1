from random import randint, choice
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    return name


def generate_even():
    num = randint(0, 100)
    ans = 'yes' if num % 2 == 0 else 'no'
    return num, ans


def generate_calc():
    num1, num2 = randint(0, 100), randint(0, 100)
    return num1, num2


def process_even_game():
    res = 0
    while res < 3:
        num, ans = generate_even()
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


def process_calc_game():
    res = 0
    signs = ['+', '-', '*']
    while res < 3:
        num1, num2 = generate_calc()
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


def generate_gcd():
    num1, num2 = a, b = randint(0, 100), randint(0, 100)
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    gcd = a if a != 0 else b
    return num1, num2, gcd


def process_gcd_game():
    res = 0
    while res < 3:
        num1, num2, ans = generate_gcd()
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
