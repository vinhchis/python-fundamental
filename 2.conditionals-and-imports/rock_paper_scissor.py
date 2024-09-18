import random
#computer_choice = 'scissors'

computer_choice = random.choice(['rock', 'paper', 'scissors']) 

user_choice = input('Do you want rock, paper or scissors?\n')

if computer_choice == user_choice:
    print("TIE, computer's choice: " + str(computer_choice))
elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
    print("WIN, computer's choice: " + str(computer_choice))
else:
    print("You lose, computer win with computer's choice: " + str(computer_choice))
