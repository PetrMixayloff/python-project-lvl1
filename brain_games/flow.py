import prompt

TOTAL_COUNT = 3
GREETING = 'Welcome to the Brain Games!'


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    return name


def answer_is_correct(answer, player_answer):
    if player_answer != answer:
        return False
    return True


def game_process(game, name):
    count = 0
    while count < TOTAL_COUNT:
        answer, question = game.generate()
        print(f'Question: {question}')
        if isinstance(answer, int):
            player_answer = prompt.integer(prompt="Your answer: ")
        else:
            player_answer = prompt.regex(pattern="^(yes|no)$",
                                         prompt="Your answer: ").string
        if answer_is_correct(answer, player_answer):
            count += 1
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
    return


def main(game):
    print(GREETING)
    print(game.DESCRIPTION)
    name = welcome_user()
    game_process(game, name)
