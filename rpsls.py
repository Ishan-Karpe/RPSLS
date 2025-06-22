import random
print('===================')
print('Rock, Paper, Scissors')
print('===================')

def get_player_choice():
    print('1) Rock: ✊')
    print('2) Paper: ✋')
    print('3) Scissors: ✌️')

    

    player = int(input('Choose your number (1-3): '))
    if player > 3 or player < 1:
        print('Invalid choice. Please choose a number between 1 and 3.')
        return get_player_choice()