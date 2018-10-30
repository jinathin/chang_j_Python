# import the random package so that we can generate random numbers
from random import randint

# choices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False

# def win or lose function
def winorlose(status):
    print("Called win or lose function")
    print("********************************")
    print("You", status, " ! Would you like to play again?")
    choice = input("Y / N: ")

    #reset the lives
    if choice == "Y" or choice =="y":
        # change global variables
        global player_life
        global computer_life
        global player
        global computer

        player_life = 3
        computer_life = 3
        player = False
        computer = choices[randint(0, 2)]

    elif choice == "N" or choice =="n":
        print("You choose to quit!")
        print("**********************")
        exit()

# make the computer choose a weapon choices array at random
computer_choice = choices[randint(0,2)]

# set the lives for player and computer
player_life = 3
computer_life = 3




# set up our loop
while player is False:
    # set players to True by making a selection
    print()
    print("Your lives: ", player_life)
    print("Computer lives:", computer_life)
    print("Choose your weapon!")
    player = input("Rock, Paper or Scissors ?\n")
    # print the choice to the terminal window
    print("Player chooses", player, "\n")

    #quit Game
    if player == "quit":
            exit()
    #choices of player and computer
    print("Player chooses:", player)
    print("Computer chooses: ", computer_choice)

    #set the restart command
    if player == "restart":
            player_life = 3
            computer_life = 3
            player = False
            computer_choice = choices[randint(0,2)]

    # check for a tie = choices are the same
    if player == computer_choice:
        print("Tie! You live to shoot another day")
    # check to see if the computer choice beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            player_life = player_life - 1
            # computer won. Crap!!
            print("You lose! Paper covers Rock")
        else:
            computer_life = computer_life - 1
            # we win! such winning
            print("You won!", player, "smashes", computer_choice)

    elif player == "Paper":
        if computer_choice == "Scissors":
            player_life = player_life - 1
            print("You lose", computer_choice, "cut", player)
        else:
            computer_life = computer_life - 1
            print("You won!", player, "covers", computer_choice)

    elif player == "Scissors":
        if computer_choice == "Rock":
            player_life = player_life - 1
            print("You lose", computer_choice, "smashes", player)
        else:
            computer_life = computer_life - 1
            print("You won!", player, "cut", computer_choice)
    else:
        print("Check your spelling... that's not a valid choice\n")
   	# reset the game loop and start over again
    player = False
    computer_choice = choices [randint(0, 2)]

    # set to restart or to quit when game over (player loses)    
    if player_life == 0:
        winorlose("lose")


    # set to restart or to quit when game over (computer loses)  
    if computer_life == 0:
        winorlose("lose")
