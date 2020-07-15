import prompt
import importlib

TOTAL_COUNT = 3
GREETING = 'Welcome to the Brain Games!'
DESCRIPTION = {
    'calc_game': 'What is the result of the expression?',
    'even_game': 'Answer "yes" if number even otherwise answer "no".',
    'gcd_game': 'Find the greatest common divisor of given numbers.',
    'prime_game': 'Answer "yes" if given number is prime. '
                  'Otherwise answer "no".',
    'progression_game': 'What number is missing in the progression?'
}


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    return name


def game_flow(game_name):
    game = importlib.import_module(f'brain_games.games.{game_name}')
    print(GREETING)
    print(DESCRIPTION[game_name])
    name = welcome_user()

    count = 0
    while count < TOTAL_COUNT:
        answer, question = game.generate()
        print(question)
        if isinstance(answer, int):
            player_answer = prompt.integer(prompt="Your answer: ")
        else:
            player_answer = prompt.regex(pattern="^(yes|no)$",
                                         prompt="Your answer: ").string
        if player_answer == answer:
            count += 1
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
    return
