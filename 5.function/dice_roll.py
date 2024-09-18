import random

def roll_dice():
    total_dice = random.randint(1,6) + random.randint(1,6)
    return total_dice
def main():
    player1 = input("Enter player1's name:\n")
    player2 = input("Enter player2's name:\n")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1,'rolled', roll1)
    print(player2,'rolled', roll2)

    if(roll1 > roll2):
        print(player1, 'win!')
    elif roll1 < roll2:
        print(player2, 'win!') 
    else:
        print('You tie!!!')

main()
