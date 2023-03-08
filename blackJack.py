# Imported random for the card generator and os to clear the shell screen,
# and import sleep from time to slow the program down at certain points
import random
from os import system, name
from time import sleep
# Initializing my variables
value = 0
global card
card = 0
play = "Y"
score = 0
scoreD = 0
# function to clear the screen
def clear():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
     _ = system('clear')
    # Creating the function to draw the dealer's card

# function to display the loser txt image
def loser():
    print("Your a LOSER!!")
    print("****************************************************************************************************************")
    print("     ||||           ||||||||||||   /|||||||||\    ||||||||||||   ||||||||||||\   |||||  ")
    print("     ||||           ||||    ||||  ////      \||   ||||           ||||      |||   |||||  ")
    print("     ||||           ||||    ||||  \\\\\\\            ||||           ||||      |||   |||||  ")
    print("     ||||           ||||    ||||   \\\\\\\______     ||||||||||||   ||||      |||   |||||  ")
    print("     ||||           ||||    ||||    \||||||||\    ||||||||||||   ||||||||||||/   \|||/  ")
    print("     ||||           ||||    ||||           \\\|\   ||||           ||||  \\\\\\         *   ")
    print("     ||||       ||  ||||    ||||  ||\      ////   ||||           ||||   \\\\\\       ***  ")
    print("     |||||||||||||  ||||||||||||  \||||||||||/    ||||||||||||   ||||    \\\\|||     *   ")
    print("****************************************************************************************************************")
# function to determine the winner
def results():
    if add <= 21 and addD > 21:
        print("********************")
        print("Your score is:", add, "|  Dealer's score:", scoreD)
        win()       
        if add > addD:
            print("********************")
            print("Your score is:", add, "|  Dealer's score:", addD)
            win()               
    elif add > 21 and addD <=21:
        print("********************")
        print("Your score is:", score, "|  Dealer's score:", addD)
        loser()
    else:
        print("********************")
        print("Your score is:", add, "|  Dealer's score:", addD)
        loser()
# function to display the win txt image
def win():
    print("Your a WINNER!!")
    print("****************************************************************************************************************")
    print("      \\\\\\\\\\            ///\\\\\\            ///////  |||||||||||||||||||    |||||||||\    |||||||||| ||||||| ")
    print("       \\\\\\\\\\          ////\\\\\\\\          ///////   |||/  ||||||   \|||    ||||||\\\\\\\\\     ||||||   ||||||| ")
    print("        \\\\\\\\\\        /////\\\\\\\\\\        ///////          ||||||           |||||| \\\\\\\\\    ||||||   ||||||| ")
    print("         \\\\\\\\\\      //////\\\\\\\\\\\\      ///////           ||||||           ||||||  \\\\\\\\\   ||||||   \\\\\|/// ")
    print("          \\\\\\\\\\    //////  \\\\\\\\\\\\    ///////            ||||||           ||||||   \\\\\\\\\  ||||||          ")
    print("           \\\\\\\\\\  //////    \\\\\\\\\\\  ///////             ||||||           ||||||    \\\\\\\\\ ||||||     ***   ")
    print("            \\\\\\\\\\//////      \\\\\\\\\\\///////        |||\  ||||||   /|||    ||||||     \\\\\\\\\||||||    *****  ")
    print("             \\\\\\\\/////        \\\\\\\\\\\/////         |||||||||||||||||||  ||||||||||    \\\\\\\\||||||     ***   ")
    print("****************************************************************************************************************") 
# function to draw the players cards
def playercard():
    global card
    global value
    card = random.randint(1,13)
    if card == 11:
        card = "JACK"
        value = 10
    elif card == 12:
        card = "QUEEN"
        value = 10
    elif card == 13:
        card = "KING"
        value = 10
    elif card == 1:
        card = "ACE"
        if add <= 10:
            value = 11
        else:
            value = 1
    else:
        value = card
# function to deal additional cards
def hit():
    global add
    # Adding a draw another card to get a higher score
    choose = input("Would you like to hit? Yes or No: ")
    clear()
    print("*******************")
    while choose == "y" or choose == "Yes" or choose == "Y" or choose == "yes":
        if choose == "y" or choose == "yes" or choose == "Y" or choose == "Yes":
            playercard()
            print("Your next card:",card)
            add = add + value
            print("Your score is now:", add)
        
            # This takes care of whether the player exceeds a score of 21 and loses
        
            print("*************************")
            if add > 21:
                score = "BUST!!"
                print("BUST!!!")
                print("*************************")
                hold = input("Take a sec. to think about your actions.. :( ...Press enter to continue...")
                clear()
                break
            choose = input("Would you like to hit again? Yes or No: ")
            clear()
            print("*******************")
        else:
            print("Your staying at: ",add)
            print("*************************")
            print("Press enter to continue...")
# function to deal the dealer's cards
def dealer():
    global addD
    addD = 0
    value = 0
    deal = random.randint(1,13)
    if deal == 11:
        deal = "JACK"
        value = 10
    elif deal == 12:
        deal = "QUEEN"
        value = 10
    elif deal == 13:
        deal = "KING"
        value = 10
    elif deal == 1:
        deal = "ACE"
        if addD <= 10:
            value = 11
        else:
            value = 1
    else:
        value = deal
    print("Dealer's first card:",deal)
    addD = addD + value
    deal = random.randint(1,13)
    if deal == 11:
        deal = "JACK"
        value = 10
    elif deal == 12:
        deal = "QUEEN"
        value = 10
    elif deal == 13:
        deal = "KING"
        value = 10
    elif deal == 1:
        deal = "ACE"
        if addD <= 10:
            value = 11
        else:
            value = 1
    else:
        value = deal
    print("Dealer's Second card:",deal)
    addD = addD + value
    print("*********************")
    print("Dealer's Score:",addD)
    sleep(2)
# Created a function to draw additional cards for the dealer
# function to deal additional dealer cards
def deal():
    global addD
    global add
    global scoreD
    while add >= addD:
        deal = random.randint(1,10)
        if deal == 11:
            deal = "JACK"
            value = 10
        elif deal == 12:
            deal = "QUEEN"
            value = 10
        elif deal == 13:
            deal = "KING"
            value = 10
        elif deal == 1:
            deal = "ACE"
            if addD <= 10:
                value = 11
            else:
                value = 1
        else:
            value = deal
        print("Dealer's Next card:",deal)
        addD = addD + value
        print("******************")
        print("Dealers Score:",addD)
        sleep(2)
        if addD > 21:
            scoreD = "Bust!!"
            print("Dealer BUST!!!")
            sleep(2)
            return
# Drawing 2 cards for the player
# Starting the program
print("I wanna play a game!")
enter = input("Press Enter to Continue...")
while play == "Yes" or play == "yes" or play == "Y" or play == "y":
    clear()
    print("Lets play some Black Jack!")
    print("*******************")
    global add
    add = 0
    playercard()
    print("first card:",card)
    add = add + value
    playercard()
    print("Second card:",card)
    add = add + value
    print("Your score:",add)
    print("*******************")
    # Adding a draw another card to get a higher score
    hit()
    # Calling the dealer function
    dealer()
    if add >= addD and add <= 21:
        #Calling the addition card draw for the dealer
        deal()
    clear()
    # Decides the outcome of the game
    results()
    
    # Resets the loop and restarts the game
    
    play = input("Shall we play again?? Yes or No: ")