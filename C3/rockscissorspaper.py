import random







player = input( 'Enter your choice  (rock/paper/scissors): ' )
player = player.lower()
while( player != "rock" and player != "paper" and  player != "scissors"):
    print( player )
    player = input("That choice is not valid. Enter your choice (rock/paper/scissors): ")
    player = player.lower()








computerInt = random.randint(0,2)
if (computerInt == 0):
    computer = "rock"
elif (computerInt == 1):
    computer = "paper"
elif (computerInt == 2):
    computer = "scissors"
else:
    computer = "Huh? Error..."










if (player == computer):
    print("Draw!")
elif (player == "rock"):
    if (computer == "paper"):
        print("Computer wins!")
    else:
        print("You win!")
elif (player == "paper"):
    if (computer == "rock"):
        print("You win!");
    else:
        print("Computer wins!")
elif (player == "scissors"):
    if (computer == "rock"):
        print("Computer wins!")
    else:
        print("You win!")








print("Your choice: " + player + "\nComputer choice: " + computer + "\nThank you for playing!")
input("Enter any key to exit.")
