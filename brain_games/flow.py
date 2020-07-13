import prompt

from .cli import WIN_COUNT, welcome_user


def game_flow(answer, question, greeting):
    print('Welcome to the Brain Games!')
    print(greeting)
    name = welcome_user()

    if process_game(answer, question):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def process_game(answer, question):
    res = 0
    while res < WIN_COUNT:
        print(question)
        if isinstance(answer, int):
            player_answer = prompt.integer(prompt="Your answer: ")
        else:
            player_answer = prompt.regex(pattern="^(yes|no)$",
                                         prompt="Your answer: ")
        if player_answer == answer:
            res += 1
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer;(. "
                  f"Correct answer was '{answer}'.")
            return False
    return True
