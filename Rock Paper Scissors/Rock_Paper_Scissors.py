# Rock Paper Scissors Game
import random # Imports the random module, ignore for now

def LineBreak():
  print("\n---------------------\n") # Creates a function that puts a line break in to make the code look a bit neater

# Attempt at making an AI player
def UserInput(bAI, sPlayer1Name, sPlayer2Name):
  if bAI == True: # If the player wants to play against an AI, do this
    sOptions = ["rock", "paper", "scissors"] # Puts the options into a list
    iAIInput = random.randint(0,2) # Generate a random number between 0 and 2
    sPlayer2Input = sOptions[iAIInput] # Get the option from that position in the list
    sPlayer1Input = input(sPlayer1Name + """, please enter either Rock, Paper or Scissors
--> """)
    sPlayer1Input = sPlayer1Input.lower() # Changes sPlayer1Input to be all lower case
    print(sPlayer2Name + " picked " + sPlayer2Input) # Print what the AI picked
    return sPlayer1Input, sPlayer2Input

  elif bAI != True:
    sPlayer1Input = input(sPlayer1Name + """, please enter either Rock, Paper or Scissors
--> """)
    sPlayer1Input = sPlayer1Input.lower() # Changes sPlayer1Input to be all lower case
    sPlayer2Input = input(sPlayer2Name + """, please enter either Rock, Paper or Scissors
--> """)
    sPlayer2Input = sPlayer2Input.lower() # Changes sPlayer2Input to be all lower case
    return sPlayer1Input, sPlayer2Input

def RockPaperScissorsWinConditions(sPlayer1Input, sPlayer2Input, sPlayer1Name, sPlayer2Name, iPlayer1Score, iPlayer2Score):

  # The win conditions for the game, calculating who won and printing the winner
    if sPlayer1Input == "rock" and sPlayer2Input == "scissors": 
      print(sPlayer1Name + " Wins!\n")
      iPlayer1Score += 1
    elif sPlayer1Input == "paper" and sPlayer2Input == "rock":
      print(sPlayer1Name + " Wins!\n")
      iPlayer1Score += 1
    elif sPlayer1Input == "scissors" and sPlayer2Input == "paper":
      print(sPlayer1Name + " Wins!\n")
      iPlayer1Score += 1
    elif sPlayer2Input == "rock" and sPlayer1Input == "scissors":
      print(sPlayer2Name + " Wins!\n")
      iPlayer2Score += 1
    elif sPlayer2Input == "paper" and sPlayer1Input == "rock":
      print(sPlayer2Name + " Wins!\n")
      iPlayer2Score += 1
    elif sPlayer2Input == "scissors" and sPlayer1Input == "paper":
      print(sPlayer2Name + " Wins!\n")
      iPlayer2Score += 1
    elif sPlayer1Input == sPlayer2Input: # If the answers were the same, it's a draw
      print("It's a draw!\n")
    else:
      print("One of those entries was invalid, please try again") # If the input was different to what was expected, print this
    return iPlayer1Score, iPlayer2Score

def RockPaperScissors(iNumberOfRounds, bAI): # Creates a function to run the Rock, Paper, Scissors game
  iPlayer1Score = 0
  iPlayer2Score = 0
  sPlayer1Name = input("Please input the name of player 1: ") # Gets the user to enter the names of the players
  sPlayer2Name = input("Please input the name of player 2 (or the AI): ")

  LineBreak()

  if iNumberOfRounds == "Infinite": # If the player wants to play infinitely, do this
  
    while True: # Loop infinitely
      print("Enter 'exit' if you want to stop playing\n")
      (sPlayer1Input, sPlayer2Input) = UserInput(bAI, sPlayer1Name, sPlayer2Name) # Calls to the function for user inputs

      if sPlayer1Input == "exit" or sPlayer2Input == "exit": # If the user enters this, exit the infinite loop
        break
      
      else:
        (iPlayer1Score, iPlayer2Score) = RockPaperScissorsWinConditions(sPlayer1Input, sPlayer2Input, sPlayer1Name, sPlayer2Name, iPlayer1Score, iPlayer2Score)

      LineBreak()
  
      print("The scores are\n"+ sPlayer1Name + ": " + str(iPlayer1Score) + "\n" + sPlayer2Name + ": " + str(iPlayer2Score))

      LineBreak()

  else: # If the number of rounds is not infinite, do this
    
    for i in range(iNumberOfRounds): # For iNumberOfRounds, do this
      
      (sPlayer1Input, sPlayer2Input) = UserInput(bAI, sPlayer1Name, sPlayer2Name) # Calls the function for user inputs
      
      (iPlayer1Score, iPlayer2Score) = RockPaperScissorsWinConditions(sPlayer1Input, sPlayer2Input, sPlayer1Name, sPlayer2Name, iPlayer1Score, iPlayer2Score) # Calls the function for the win conditions
  
      print("The scores are\n"+ sPlayer1Name + ": " + str(iPlayer1Score) + "\n" + sPlayer2Name + ": " + str(iPlayer2Score)) # Prints the player scores

  return iPlayer1Score, iPlayer2Score, sPlayer1Name, sPlayer2Name # Returns the player scores and their names as a tuple

def Results(iPlayer1Score, iPlayer2Score, sPlayer1Name, sPlayer2Name): # Function for calculating the overall winner
  if iPlayer1Score > iPlayer2Score: # If player 1's score is higher, they win
      print(sPlayer1Name + " is the overall winner!")
  elif iPlayer1Score < iPlayer2Score: # If player 2's score is higher, they win
      print(sPlayer2Name + " is the overall winner!")
  elif iPlayer1Score == iPlayer2Score: # If both scores are equal, they tie
      print("It's a draw!")
  
    
print("Welcome to my Rock, Paper, Scissors Game!")

sAIPlayer = input("""Would you like to play against an AI, or with another player? Y/N
--> """)
if sAIPlayer.lower() == "y": # If the lower case of the input is equal to this, set bAI to true
  bAI = True
elif sAIPlayer.lower() == "n":
  bAI = False

bContinue = True # Creates a variable I will use to break the loop

while bContinue:

  LineBreak() # Inserts a line break to make the program look a bit neater
  
# Creates a menu of options for the user to choose from
  sUserInput = input("""Please choose an option
  1: A 1 round game
  2: A best of 3 game
  3: A best of 5 game
  4: Please enter a custom number of rounds
  5: Play an infinite number of rounds (until you say to stop)
  6: Exit the program
  --> """)

  LineBreak()

# The code below will run the if statements depending on which option the user chose
  if sUserInput == "1":

    (iPlayer1Score, iPlayer2Score, sPlayer1Name, sPlayer2Name) = RockPaperScissors(1, bAI)
# Calls the function RockPaperScissors() and gives it the number of rounds to run, if the player is playing against an AI, then unpacks the returned tuple into 2 variables
    Results(iPlayer1Score, iPlayer2Score, sPlayer1Name, sPlayer2Name)   
# Calculate who won using the scores of the players

  elif sUserInput == "2":
    (iPlayer1Score, iPlayer2Score, sPlayer1Name, sPlayer2Name) = RockPaperScissors(3, bAI)
    Results(iPlayer1Score, iPlayer2Score, sPlayer1Name, sPlayer2Name)

  elif sUserInput == "3":
    (iPlayer1Score, iPlayer2Score, sPlayer1Name, sPlayer2Name) = RockPaperScissors(5, bAI)
    Results(iPlayer1Score, iPlayer2Score, sPlayer1Name, sPlayer2Name)

  elif sUserInput == "4":
    iNumberOfRounds = int(input("Please enter the number of rounds you wish to play: "))
# Asks the user to enter the number of rounds to be played, then converts that to a number
    (iPlayer1Score, iPlayer2Score, sPlayer1Name, sPlayer2Name) = RockPaperScissors(iNumberOfRounds, bAI)
    Results(iPlayer1Score, iPlayer2Score, sPlayer1Name, sPlayer2Name)

  elif sUserInput == "5":
    (iPlayer1Score, iPlayer2Score, sPlayer1Name, sPlayer2Name) = RockPaperScissors("Infinite", bAI) # Set the number of rounds to "Infinite", which is used to tell this part to loop infinitely
    Results(iPlayer1Score, iPlayer2Score, sPlayer1Name, sPlayer2Name)
  
  elif sUserInput == "6":
    bContinue = False # If the user enters "6", set bContinue to False, which stops the program

  
  
