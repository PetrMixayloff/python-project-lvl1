import prompt

TOTAL_COUNT = 3
GREETING = 'Welcome to the Brain Games!'


def get_user_name():
    name = prompt.string('May I have your name? ')
    return name


def game_interaction(game, name):
    count = 0
    while count < TOTAL_COUNT:
        answer, question = game.generate_data()
        print(f'Question: {question}')
        # prompt.regex не возвращает строку, поэтому там стоит .string
        # вся эта конструкция нужна для того чтобы исключить принятие игрой других вариантов ответов кроме возможных.
        # часть игр принимает ответы ввиде чисел, а часть ввиде да/нет
        if isinstance(answer, int):
            player_answer = prompt.integer(prompt="Your answer: ")
        else:
            player_answer = prompt.regex(pattern="^(yes|no)$",
                                         prompt="Your answer: ").string
        if answer == player_answer:
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
    name = get_user_name()
    print(f'Hello {name}!')
    game_interaction(game, name)
