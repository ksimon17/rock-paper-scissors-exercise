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

# import appropriate libraries
import random # for simulating a random computer selection
import os # for customizing the user's name


# DETERMINE WINNER CODE - AUTOMATED TESTING 
def determine_winner(choice_1, choice_2):
    """
    Determines the winning choice between two valid choices from selectable options: "rock", "paper", or "scissors".

    Returns the winning choice (e.g. "paper"), or None if there is a tie.

    Example: determine_winner("rock", "paper")
    """
    # code to determine the winner
    winner = ""

    #if (choice_1 == choice_2): #Tie

    if (((choice_1 == "Paper" or choice_1 == "PAPER" or choice_1 == "paper") and 
          (choice_2 == "Paper" or choice_2 == "PAPER" or choice_2 == "paper")) 
        or 
         ((choice_1 == "Rock" or choice_1 == "ROCK" or choice_1 == "rock") and
         (choice_2 == "Rock" or choice_2 == "ROCK" or choice_2 == "rock"))
         or
         ((choice_1 == "Scissors" or choice_1 == "SCISSORS" or choice_1 == "scissors") and
         (choice_2 == "Scissors" or choice_2 == "SCISSORS" or choice_2 == "scissors")) ): # all tie combination with different valid inputs
        winner = None
    elif (choice_1 == "rock" or choice_1 == "ROCK" or choice_1 == "Rock"):
        if (choice_2 == "paper" or choice_2 == "PAPER" or choice_2 == "Paper"): # Rock vs. Paper
            winner = choice_2 # "paper"
        else: # Rock vs. Scissors
            winner = choice_1 # "rock" 
    elif (choice_1 == "paper" or choice_1 == "PAPER" or choice_1 == "Paper"):
        if (choice_2 == "rock" or choice_2 == "ROCK" or choice_2 == "Rock"): # Paper vs. Rock 
            winner = choice_1 # "paper"
        else: # Paper vs. Scissors
            winner = choice_2 # "scissors"
    else: # (choice_1 == "Scissors" or choice_1 == "SCISSORS" or choice_1 == "Scissors")
        if (choice_2 == "rock" or choice_2 == "ROCK" or choice_2 == "Rock"): # Scissors vs. Rock
            winner = choice_2 # "rock"
        else: # Scissors vs. Paper
            winner = choice_1 # "scissors"
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

  #  valid_inputs = ['rock','paper','scissors','ROCK','PAPER','SCISSORS','Rock','Paper','Scissors']

    
    # Validating User Input - Check if the User Inputted Valued Input
    if (user_selection != "rock" and user_selection != "paper" and user_selection != "scissors" and
        user_selection != "ROCK" and user_selection != "PAPER" and user_selection != "SCISSORS" and 
        user_selection != "Rock" and user_selection != "Paper" and user_selection != "Scissors" ):
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
    
    #User Input is Valid 

    # Simulating Computer Selection
    computer_selection = random.choice(list_of_choices) 
    
    # Determining the Winner
    # CALL THE DETERMINE_WINNER FUNCTION WITHIN MAIN ?
    winner = determine_winner(user_selection, computer_selection)
    print ("-------------------------")
    print ("You chose: " + user_selection)
    print ("The computer chose: " + computer_selection)
    print ("-------------------------")
    if (winner == None):
        print("You tied. Nice job!")
    elif (winner == user_selection):
        print("Congratulations! You won the game!")
    elif (winner == computer_selection):
        print("Oh, the computer won. It's ok. Better luck next time.")
    print ("-------------------------")
    print ("Thanks for playing. Please play again!")
    print ("-------------------------")
    print("")


