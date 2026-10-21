import random
choice = ["rock","paper","scissors"]
computer = random.randint(0,2)
player = input("Enter your choice (rock, paper, scissors): ")
if player == "rock" and computer == 0:
 print("draw")
elif player == "rock" and computer == 1:
 print("computer win")
elif player == "rock"and computer == 2:
 print("you win")  
elif player == "paper" and computer == 0:
 print("you win")
elif player == "paper"and computer == 1:
 print("draw")
elif player == "paper" and computer == 2:
 print("computer win")
elif player == "scissors"and computer == 0:
 print("computer win")  
elif player == "scisscors" and computer == 1:
 print("you win")
elif player == "scisscors"and computer == 2:
 print("draw")  