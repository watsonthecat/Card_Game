#Main PROGRAM
import ui, card_deck, player, random
from card_deck import Card
from player import Fisherman

sadTrombone = "Go Fish!"



user_hand = []
robot_hand = []
totalBooks = 0


def handle_choice(choice):

    if choice == '1':
        play_game()

    elif choice == '2':
        show_rules() #TODO Make this method + do this stuff

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')

def deal_hand(deck, handSize):

    hand = []

    if len(deck) >= handSize:

        for i in range(0, handSize):
            hand.append(deck[i])
            deck.remove(deck[i])
    return hand

def draw_card(deck, player):
    ui.message('Drawing Card...')
    #Deck size print for testing
    print('Deck Size: ', len(deck))
    if len(deck) >= 1:
        card = deck.pop()
        #Add card to player's hand
        #This might just be replacing the last card?
        player.hand.append(card)
        #Printing deck size to make sure pop removes from deck
        print ('Deck Size: ', len(deck))
        #Testing prints -- can be removed because this works
        print('The card you drew is:', card)
        print(player.name,'hand is: ', player.hand)

def user_turn(player1, player2, deck): #Tested seems to be working
    #TODO: Test this if robot has 2 of the same card, I don't think it would give the user both

    anotherTurn = True
    has = []

    while anotherTurn == True:
        has = []
        msg = '...Your turn...'
        stars = '*' * len(msg)
     #Thinking about using a loop while TRUE, breaking @ Go Fish!
        #Get user's requested card
        ask = input('What card would you like to ask for?')
        #card.rank = ask
        print('Do you have a...', ask,'?')
        #See if robot has the card
        print('Robot is checking his hand...')
        #if so: give user card (add card to user hand) + remove card from robot's hand
        #check for pairs, display user's books
        for card in player2.hand:
            if card.rank == ask:
                has.append(card)
                print('Robot has that card!')
                player2.hand.remove(card)
            for card in has: #This probably isn't working properly
                player1.hand.append(card)
                #print('How many times is this happening?')
        print(player1.name, 'asked', player2.name, 'for', ask,"'s")
        print(player2.name, ' had ', str(len(has)))


        #print('Your hand is now:', player1.hand)
        #print('Robot hand is now: ', player2.hand)

        if len(has) == 0:
            print(player1.name, 'has to GO FISH!')
            draw_card(deck,player1)
            anotherTurn = False


def robot_turn(player1, player2, deck):


    anotherTurn = True
    has = []

    while anotherTurn == True:
        has = []
        msg = "...MUTANT ROBOT'S turn..."
        stars = '*' * len(msg)

        #Out of robot's hand, pick a card to request from user
        choose = random.randint(0, len(player1.hand)-1)
        ask = player1.hand[choose]
        askNum = ask.rank

        #card.rank = ask
        print('Do you have a...', askNum,'?')
        #See if robot has the card
        print('Checking your hand for a match...')
        #if so: give user card (add card to user hand) + remove card from robot's hand
        #check for pairs, display user's books
        for card in player2.hand:
            if card.rank == askNum:
                has.append(card)
                print('You have that card!')
                player2.hand.remove(card)
            for card in has:
                player1.hand.append(card)
        print(player1.name, 'asked', player2.name, 'for', askNum,"'s")
        print(player2.name, ' had ', str(len(has)))


        #print('Your hand is now:', player1.hand)
        #print('Robot hand is now: ', player2.hand)

        if len(has) == 0:
            print(player1.name, 'has to GO FISH!')
            draw_card(deck,player1)
            anotherTurn = False
    #Out of robot's hand, pick a card to request from user
        #if so: add card to hand + remove from user's hand
            #check for pairs, display robots's books
        #else: ui.message(sadTrombone) GO FISH + robot draws card

def make_pairs(player, totalBooks): #This isn't tested 100% - no bugs, but don't know if it's doing what I really want it to
#This also doesn't remove the pairs from the player's hand yet
#It's saying that a group of 3 is a pair? I'm confused...
    ui.message('Checking for pairs...')
    #check's the hand for any pairs, groups them together
    #if = 4 then make a book, if book, reward point to player
    #add 1 to totalBooks
    amount = {}
    for card in player.hand:
        if card.rank not in amount.keys():
            amount[card.rank] = 1
        if card.rank in amount.keys():
            amount[card.rank] += 1
    #if = 4 then make a book, if book, reward point to player
    for count in amount.keys():
        if amount[count] == 4:
            print(player.name+" got a set of "+count+"s.")
            player.sets.append(count)
            #add 1 to totalBooks
            totalBooks = totalBooks + 1
            player.hand[:] = [card for card in player.hand if card.rank == count]



def play_game(): #This is where the game starts and all the stuff happens


    user = Fisherman()
    robot = Fisherman()
    robot.name = "Mutant Robot"

    #Get user's name and set robots name in Player class
    user.name = input("Please enter your name: ")
    #print ('Your name is: ',user.name)

    #Shuffle Deck/Get Deck of cards
    deck = card_deck.shuffled_deck()
    ui.message('Shuffling deck...')

    # #Display deck for testing
    # print ('Deck Size: ', len(deck))

    #deal hands to computer and player
    user.hand = deal_hand(deck,7)
    robot.hand = deal_hand(deck,7)

    #Display hands for testing
    print('User Hand = ', user.hand)
    print('Robot Hand = ', robot.hand)


    #Testing draw_card
    #draw_card(deck,user)

    # #Display deck for testing
    # print ('Deck Size: ', len(deck))

    #Loop through turns until totalBooks = 13
    while totalBooks < 13:
        #alternate between turns/gameplay
        user_turn(user, robot, deck)
        make_pairs(user, totalBooks)
        robot_turn(robot, user, deck)
        make_pairs(robot, totalBooks)


    #Winner = player with most books, so determine the winner by figuring that Out
    #Say who wins

    #Restart program/display_menu_get_choice()
def main():
    quit = 'q'
    choice = None

    while choice != quit:
        #Display Banner to let user know what game they are playing
        ui.display_banner()
        #Display Menu for user
        choice = ui.display_menu_get_choice()
        #Handle user's choice
        handle_choice(choice)

if __name__ == '__main__':
    main()
