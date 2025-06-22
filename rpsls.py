import random
print('===================')
print('Rock Paper Scissors')
print('===================')
print('1) Rock: ✊')
print('2) Paper: ✋')
print('3) Scissors: ✌️')

    
def player_choice():
    player = int(input('Choose your number (1-3): '))
    if player > 3 or player < 1:
        print('Invalid choice. Please choose a number between 1 and 3.')
        return player_choice()
    else:
        print('You chose:', player)
        return player # return passes this data from this function to the next one

def computer_choice():
    computer = random.randint(1, 3)
    print('Computer chose:', computer)
    return computer
    

def winning_conditions(player, computer):
    if (player == 1 and computer == 2):
        print('Computer wins! Paper beats rock.')
    elif (player == 1 and computer == 3):
        print('You win! Rock beats scissors.')
    elif (player == 2 and computer == 1):
        print('You win! Paper beats rock.')
    elif (player == 2 and computer == 3):
        print('Computer wins! Scissors beats paper.')
    elif (player == 3 and computer == 1):
        print('Computer wins! Rock beats scissors.')
    elif (player == 3 and computer == 2):
        print('You win! Scissors beats paper.')
    else:
        print('It\'s a tie!')

if __name__ == '__main__':
    player = player_choice()
    computer = computer_choice()
    winning_conditions(player, computer)
    print('Thanks for playing!')