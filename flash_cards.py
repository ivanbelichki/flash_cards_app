import random

# CONSTANTS
CARDS_FILE = 'cards.txt'
QA_DIVIDER = ':'

ADD_KEY = 'a'
PLAY_KEY = 'p'
VIEW_KEY = 'v'
REMOVE_KEY = 'r'
QUIT_KEY = 'q'

VALID_KEYS = [ADD_KEY, REMOVE_KEY, PLAY_KEY, VIEW_KEY, QUIT_KEY]

# driver
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

# start menu
def start():
    # print app menu
    print(f'''
            Welcome to the Flash Card App!
            Enter '{ADD_KEY}' to Add new Cards
            Enter '{REMOVE_KEY}' to remove Cards
            Enter '{VIEW_KEY}' to View all Cards
            Enter '{PLAY_KEY}' to Play!
            or '{QUIT_KEY}' to Quit
            ''')

    # get valid user choice
    user_in = ''
    while user_in not in VALID_KEYS:
        user_in = input('Enter your choice: ')

    return user_in

# Flash Card Game Loop
def play():

    f = open(CARDS_FILE, "r")
    cards = f.readlines()

    # keep track of used cards
    n = -1
    used = [-1]

    # game loop
    user_in = ''
    while user_in != QUIT_KEY:

        # check if all cards used
        all_cards_used = len(used) == len(cards) + 1
        if all_cards_used:
            print('\n')
            print("Congrats! You've done all questions")
            return

        # find random card index
        while n in used:
            n = random.randint(0, len(cards)-1)
        card = cards[n].split(QA_DIVIDER)

        # print flash card
        print('\n')
        print(f'QUESTION: {card[0]}\n')
        input("Press 'Enter' for answer\n")
        print(f'ANSWER: {card[1]}')

        # keep track of used card index
        used.append(n)

        # get user choice
        user_in = input(f"Press 'Enter' for next question or {QUIT_KEY}' to quit: ")

    f.close()

# add flash cards to deck
def add_cards():

    count = 0

    # adding card loop
    user_in = ''
    while user_in != QUIT_KEY:

        # enter question
        user_in = input(f'Enter the question, or {QUIT_KEY} to quit: ')
        if user_in == QUIT_KEY:
            break

        question = user_in

        # enter answer
        user_in = input(f'Enter the answer, or {QUIT_KEY} to quit: ')
        if user_in == QUIT_KEY:
            break

        answer = user_in

        # write to flash card to file
        write_to_file(question, answer)

        # print flash card
        print(f'''
            Flash Card entered:
            Q: {question}
            A: {answer}
        ''')

        count += 1

    if count > 0:
        print(f'Thanks for entering {count} card(s)')

# remove flash cards from deck
def remove_cards():

    choice = ''
    while choice != QUIT_KEY:

        # print flash card deck
        view_cards()

        # get user input to delete card
        print('\n')
        choice = input(f'''Enter the number of the Card you wish to remove, or {QUIT_KEY} to quit ''')

        if choice == QUIT_KEY:
            break
        try:
            choice = int(choice)
        except:
            print('Please Enter a valid Card number')
            continue

        f = open(CARDS_FILE, "r")
        cards = f.readlines()

        if choice > len(cards) or choice < 0:
            print('Please Enter a valid Card number')
            continue

        # delete card from data strucutre
        cards.remove(cards[choice])

        # overwrite card file with new cards
        w = open(CARDS_FILE, "w")
        w.write(''.join(cards))
        w.close()

        f.close()


# print flash cards
def view_cards():
        f = open(CARDS_FILE, "r")
        cards = f.readlines()

        print('\n')
        print(f'{len(cards)} cards:')
        print('\n')

        # get [question, answer] list of flash cards
        cards = [card.split(QA_DIVIDER) for card in cards]

        # list cards by number
        for i, card in enumerate(cards):
            print(f'{i}) QUESTION: {card[0]}, ANSWER: {card[1]}')

        f.close()

# write flash card to file
def write_to_file(question, answer):
    f = open(CARDS_FILE, "a")
    f.write(question + QA_DIVIDER + answer + '\n')
    f.close()

__main__()