def display_banner():
    '''Display a banner letting the user know what game they are playing'''

    msg = 'AWESOME Go Fish! Card Game PROGRAM'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n', stars, '\n')
    print('Welcome to the game! You will be playing against a MUTANT ROBOT!')


def display_menu_get_choice():
    '''Display choices for user, return users' selection'''

    print('''
        1. Start Game
        2. Rules + Tips (This is not a feature yet)
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice

def message(msg):
    '''Display a message to the user'''
    print(msg)

def display_rules():
    '''Display the rules of the game'''

    print('''
        OBJECT OF THE GAME:
        The goal is to win the most "books" of cards.
        A book is any four of a kind, such as four kings, four aces, and so on.

    ''')

def display_books(): pass #books are 4 of a kind (4 of same rank)
