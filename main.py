import random



player_choice = input("Enter a choice(scicissor, rock , paper): ")
options = ["rock" , "paper" , "scissor"]
computer_choice = random.choice(options)
  
result = {"You choose ": player_choice , "computer choose" : computer_choice}
print(result)

if player_choice == "rock" and computer_choice == "paper":
  print("You loose")
elif player_choice == "paper" and computer_choice == "rock":
  print("computer loose")
elif player_choice == "rock" and computer_choice == "scissor":
  print("you win")
elif player_choice == "scissor" and computer_choice == "rock":
  print("you lose")
elif player_choice == "paper" and computer_choice == "scissor":
  print("computer win")
elif player_choice == "scissor" and computer_choice == "paper":
  print("You win")
elif player_choice == "rock" and computer_choice == "rock":
  print("its a tie")
elif player_choice == "paper" and computer_choice == "paper":
  print("its a tie")  
elif player_choice == "scissor" and computer_choice == "scissor":
  print("its a tie") 
  
else:
  Print("errorr")

  




