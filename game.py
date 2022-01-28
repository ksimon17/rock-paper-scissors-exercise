# this is the "game.py" file...



# Objectives

# ASK FOR USER INPUT


# VALIDATIONS


# COMPUTER CHOICE


# DETERMINE THE WINNER


# DISPLAY FINAL RESULTS 






import random
print("")
print ("-------------------------")
print("Welcome to the Rock, Paper, Scissors Shoot Game!")

# Creating a List of Valid Choices to Use in Future Computer Simulations
listOfChoices = ["rock", "paper","scissors"]

# 1. User Input Section 
userSelection = input("To play the game, Please choose one of 'rock', 'paper', or 'scissors': ")

#2. Validating User Input / #3 Simulating Computer Selection / #4. Determining a Winner
if (userSelection != "rock" and userSelection != "paper" and userSelection != "scissors"):
    #INVALID INPUT - INFORM THE USER AND GRACEFULLY EXIT THE PROGRAM
    print("")
    print ("-------------------------")
    print("Unfortunately, this user input is invalid.")
    print("For reference, the valid input is either 'rock', 'paper', or 'scissors'.") 
    print("However, you inputted" + userSelection + ", which is not valid.")
    print("To replay the game, please reinsert python game.py in your command line and input an appropriate selection when prompted.")
    print("Thank you!")
    print("")
    print ("-------------------------")
    print("")
    exit()
else :
    # Simulating Computer Selection
    computerSelection = random.choice(listOfChoices)
    
    # DETERMINING THE WINNER
    userResult = ""
    if (userSelection == computerSelection): # TIE
        userResult = "tie"
    else:
        if (computerSelection == "rock"): # COMPUTER PICKS PAPER
            if (userSelection == "scissors"): # scissors (user) vs rock (comp)
                userResult = "loss"
            else: #userSelection == "paper" -- paper (user) vs rock (comp)
                userResult = "win"
        elif (computerSelection == "scissors"): # COMPUTER PICKS SCISSORS
            if (userSelection == "rock"): # rock (user) vs. scissors (comp)
                userResult = "win"
            else: #userSelection == "paper" -- paper (user) vs. scissors (comp)
                userResult = "loss"
        else: # computerSelection == "paper" -- COMPUTER PICKS PAPER
            if (userSelection == "rock"): # rock (user) vs. paper (comp)
                userResult = "loss"
            else: #userSelection == "scissors" -- scissors (user) vs paper (comp)
                userResult = "win"

#DISPLAY FINAL RESULTS 
print ("-------------------------")
print ("You chose: " + userSelection)
print ("The computer chose: " + computerSelection)
print ("-------------------------")
if (userResult == "win"):
    print("Congratulations! You won the game!")
elif (userResult == "loss"):
    print("Oh, the computer won. It's ok. Better luck next time.")
else: 
    print("You tied. Nice job!")
print ("-------------------------")
print ("Thanks for playing. Please play again!")
print ("-------------------------")
print("")



