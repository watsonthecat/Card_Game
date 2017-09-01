sadTrombone = "Go Fish!"

def deal_hand(): pass

def user_turn(): pass

 #Thinking about using a loop while TRUE, breaking @ Go Fish!
    #Get user's requested card
    #See if robot has the card
        #if so: give user card (add card to user hand) + remove card from robot's hand
            #check for pairs, display user's books
        #else: GO FISH! + user draws a card


def robot_turn(): pass
    #Out of robot's hand, pick a card to request from user
        #if so: add card to hand + remove from user's hand
            #check for pairs, display robots's books 
        #else: ui.message(sadTrombone) GO FISH + robot draws card
def make_pairs():
    #check's the hand for any pairs, groups them together
    #if = 4 then make a book, if book, reward point to player

def play_game(): #This is where the game starts and all the stuff happens

    #Shuffle Deck/

    #deal hands to computer and player
    deal_hand()

    #Loop through turns until totalBooks = 13

    #Winner = player with most books, so determine the winner by figuring that Out
    #Say who wins

    #Restart program/display_menu_get_choice()
