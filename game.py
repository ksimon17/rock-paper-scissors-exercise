# this is the "game.py" file...

# Objectives
# --------------------
# ASK FOR USER INPUT
# VALIDATIONS
# COMPUTER CHOICE
# DETERMINE THE WINNER
# DISPLAY FINAL RESULTS 
# NAME CUSTOMIZATION
# AUTOMATED TESTING
# --------------------

# should all variable names be underscored?

# import appropriate libraries
import random
import os


# DETERMINE WINNER CODE - AUTOMATED TESTING 
def determine_winner(choice_1, choice_2):
    """
    Determines the winning choice between two valid choices from selectable options: "rock", "paper", or "scissors".

    Returns the winning choice (e.g. "paper"), or None if there is a tie.

    Example: determine_winner("rock", "paper")
    """
    # code to determine the winner
    winner = ""
    if (choice_1 == choice_2): #Tie
        winner = None
    elif (choice_1 == "rock"):
        if (choice_2 == "paper"): # Rock vs. Paper
            winner = "paper"
        else: # Rock vs. Scissors
            winner = "rock" 
    elif (choice_1 == "paper"):
        if (choice_2 == "rock"): # Paper vs. Rock 
            winner = "paper"
        else: # Paper vs. Scissors
            winner = "scissors"
    else: # Scissors vs. Rock
        if (choice_2 == "rock"):
            winner = "rock"
        else: # Scissors vs. Paper
            winner = "scissors"
    return winner

# MAIN 
if __name__ == "__main__":

    # Set the username to the default "Player One" or to the user's provided one
    player_name = os.getenv("PLAYER_NAME", default="Player One")

    # Welcome the user to the game 
    print("")
    print ("-------------------------")
    print("Welcome '" + player_name + "' to the Rock, Paper, Scissors Game!")
    print ("-------------------------")

    # Create a List of Valid Choices to Use in Future Computer Simulations
    list_of_choices = ["rock", "paper","scissors"]

    # User Input 
    user_selection = input("To play the game, Please choose one of 'rock', 'paper', or 'scissors': ")

    # Validating User Input / Simulating Computer Selection / Determining a Winner
    if (user_selection != "rock" and user_selection != "paper" and user_selection != "scissors"):
        #Invalid Input -- Inform the User and Gracefully Exit the Program
        print("")
        print ("-------------------------")
        print("Unfortunately, this user input is invalid.")
        print("For reference, the valid input is either 'rock', 'paper', or 'scissors'.") 
        print("However, you inputted '" + user_selection + "', which is not valid.")
        print("To replay the game, please reinsert python game.py in your command line") 
        print("and input an appropriate selection when prompted.")
        print("Thank you!")
        print ("-------------------------")
        print("")
        exit() # gracefully exit the program
    else :
        # Simulating Computer Selection
        computer_selection = random.choice(list_of_choices)
        
        # Determining the Winner
        user_result = ""
        if (user_selection == computer_selection): # TIE
            user_result = "tie"
        else:
            if (computer_selection == "rock"): # COMPUTER PICKS PAPER
                if (user_selection == "scissors"): # scissors (user) vs rock (comp)
                    user_result = "loss"
                else: #user_selection == "paper" -- paper (user) vs rock (comp)
                    user_result = "win"
            elif (computer_selection == "scissors"): # COMPUTER PICKS SCISSORS
                if (user_selection == "rock"): # rock (user) vs. scissors (comp)
                    user_result = "win"
                else: #user_selection == "paper" -- paper (user) vs. scissors (comp)
                    user_result = "loss"
            else: # computer_selection == "paper" -- COMPUTER PICKS PAPER
                if (user_selection == "rock"): # rock (user) vs. paper (comp)
                    user_result = "loss"
                else: #user_selection == "scissors" -- scissors (user) vs paper (comp)
                    user_result = "win"

    #Display Final Results 
    print ("-------------------------")
    print ("You chose: " + user_selection)
    print ("The computer chose: " + computer_selection)
    print ("-------------------------")
    if (user_result == "win"):
        print("Congratulations! You won the game!")
    elif (user_result == "loss"):
        print("Oh, the computer won. It's ok. Better luck next time.")
    else: 
        print("You tied. Nice job!")
    print ("-------------------------")
    print ("Thanks for playing. Please play again!")
    print ("-------------------------")
    print("")

