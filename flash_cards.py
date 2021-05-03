import random

CARDS_FILE = 'cards.txt'
QA_DIVIDER = ':'

ADD_KEY = 'a'
PLAY_KEY = 'p'
VIEW_KEY = 'v'
REMOVE_KEY = 'r'
QUIT_KEY = 'q'

VALID_KEYS = [ADD_KEY, REMOVE_KEY, PLAY_KEY, VIEW_KEY, QUIT_KEY]


def __main__():
    choice = ''
    while choice != QUIT_KEY:
        choice = start()
        if choice == ADD_KEY:
            add_cards()
        elif choice == PLAY_KEY:
            play()
        elif choice == REMOVE_KEY:
            remove_cards()
        elif choice == VIEW_KEY:
            view_cards()

    print(f'\nSee you next time!\n')

def start():
    print(f'''
            Welcome to the Flash Card App!
            Enter '{ADD_KEY}' to Add new Cards
            Enter '{REMOVE_KEY}' to remove Cards
            Enter '{VIEW_KEY}' to View all Cards
            Enter '{PLAY_KEY}' to Play!
            or '{QUIT_KEY}' to Quit
            ''')
    user_in = ''
    while user_in not in VALID_KEYS:
        user_in = input('Enter your choice: ')
    return user_in


def play():
    user_in = ''
    f = open(CARDS_FILE, "r")
    cards = f.readlines()
    n = -1
    used = [-1]
    while user_in != QUIT_KEY:

        if len(used) == len(cards) + 1:
            print('\n')
            print("Congrats! You've done all questions")
            return

        while n in used:
            n = random.randint(0, len(cards)-1)

        card = cards[n].split(QA_DIVIDER)

        print('\n')
        print(f'QUESTION: {card[0]}\n')
        input("Press 'Enter' for answer\n")
        print(f'ANSWER: {card[1]}')

        used.append(n)


        user_in = input(f"Press 'Enter' for next question or {QUIT_KEY}' to quit: ")

    f.close()


def add_cards():

    count = 0
    user_in = ''
    while user_in != QUIT_KEY:

        user_in = input(f'Enter the question, or {QUIT_KEY} to quit: ')
        if user_in == QUIT_KEY:
            break

        question = user_in

        user_in = input(f'Enter the answer, or {QUIT_KEY} to quit: ')
        if user_in == QUIT_KEY:
            break

        answer = user_in

        write_to_file(question, answer)
        print(f'''
            Flash Card entered:
            Q: {question}
            A: {answer}
        ''')
        count += 1

    if count > 0:
        print(f'Thanks for entering {count} card(s)')


def remove_cards():

    choice = ''
    while choice != QUIT_KEY:
        view_cards()

        f = open(CARDS_FILE, "r")
        cards = f.readlines()

        print('\n')
        choice = input(f'''Enter the number of the Card you wish to remove, or {QUIT_KEY} to quit ''')
        if choice == QUIT_KEY:
            break
        try:
            choice = int(choice)
        except:
            print('Please Enter a valid Card number')
            continue

        if (choice) > len(cards) or choice < 0:
            print('Please Enter a valid Card number')
            continue

        cards.remove(cards[choice])

        w = open(CARDS_FILE, "w")
        w.write(''.join(cards))
        w.close()

        f.close()



def view_cards():
        f = open(CARDS_FILE, "r")
        print('\n')
        cards = f.readlines()
        print(f'{len(cards)} cards:')
        print('\n')

        cards = [card.split(QA_DIVIDER) for card in cards]
        for i, card in enumerate(cards):
            print(f'{i}) QUESTION: {card[0]}, ANSWER: {card[1]}')

        f.close()

def write_to_file(question, answer):
    f = open(CARDS_FILE, "a")
    f.write(question + QA_DIVIDER + answer + '\n')
    f.close()

__main__()