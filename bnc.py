# Import the random library
from random import randint

# get user input
player = input("Bear, Ninja, or Cowboy? > ")

# Define roles in new array named `roles`
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random number, then use that random number as an index position from list `roles`
# randint() takes arguments (beginning and end of the range for the random int to be picked from)
computer = roles[randint(0,2)]

# Compare computer and player role with conditional logic
# use while loop to keep going
player = False

while player == False:
    # Get player input
    player = input("Bear, Ninja, or Cowboy? > ")

    # Compare computer and player role

    if computer == player:
      print("DRAW!")
    elif computer == "Cowboy":
      if player == "Bear":
        print("You lose!", computer, "shoots", player)
      else: # computer is cowboy, player is ninja
        print("You win!", player, "defeats", computer)
    elif computer == "Bear":
      if player == "Cowboy":
        print("You win!", player, "shoots", computer)
      else: # computer is bear, player is ninja
        print("You lose!", computer, "eats", player)
    elif computer == "Ninja":
      if player == "Cowboy":
        print("You lose!", computer, "defeats", player)
      else: # computer is ninja, player is bear
        print("You win!", player, "eats", computer)
# there is some glitch where some combo doesn't trigger the Play Again? 
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      player = False
      computer = roles[randint(0,2)]
    else:
      break
