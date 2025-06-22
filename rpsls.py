import random

def menu():
    print('================================')
    print('Rock Paper Scissors Lizard Spock')
    print('================================')
    print('1) Rock: ✊')
    print('2) Paper: ✋')
    print('3) Scissors: ✌️')
    print('4) Lizard: 🦎')
    print('5) Spock: 🖖')

menu()
def player_choice():
    player = int(input('Choose your number (1-5): '))
    if player > 5 or player < 1:
        print('Invalid choice. Please choose a number between 1 and 5.')
        return player_choice()
    else:
        print('You chose:', player)
        return player # return passes this data from this function to the next one

def computer_choice():
    computer = random.randint(1, 5)
    print('Computer chose:', computer)
    return computer
    

def winning_conditions(player, computer):
    if (player == computer):
        print("It's a tie!")
    elif (player == 1 and computer == 2):
        print('Computer wins! Paper ✋ covers Rock ✊.')
    elif (player == 1 and computer == 3):
        print('You win! Rock ✊ breaks Scissors ✌️.')
    elif (player == 1 and computer == 4):
        print('You win! Rock ✊ crushes Lizard 🦎.')
    elif (player == 1 and computer == 5):
        print('Computer wins! Spock 🖖 vaporizes Rock ✊.')
    elif (player == 2 and computer == 1):
        print('You win! Paper ✋ covers Rock ✊.')
    elif (player == 2 and computer == 3):
        print('Computer wins! Scissors ✌️ cut Paper ✋.')
    elif (player == 2 and computer == 4):
        print('Computer wins! Lizard 🦎 eats Paper ✋.')
    elif (player == 2 and computer == 5):
        print('You win! Paper ✋ disproves Spock 🖖.')
    elif (player == 3 and computer == 1):
        print('Computer wins! Rock ✊ breaks Scissors ✌️.')
    elif (player == 3 and computer == 2):
        print('You win! Scissors ✌️ cut Paper ✋.')
    elif (player == 3 and computer == 4):
        print('You win! Scissors ✌️ beat Lizard 🦎.')
    elif (player == 3 and computer == 5):
        print('Computer wins! Spock 🖖 smashes Scissors ✌️.')
    elif (player == 4 and computer == 1):
        print('Computer wins! Rock ✊ crushes Lizard 🦎.')
    elif (player == 4 and computer == 2):
        print('You win! Lizard 🦎 eats Paper ✋.')
    elif (player == 4 and computer == 3):
        print('Computer wins! Scissors ✌️ beat Lizard 🦎.')
    elif (player == 4 and computer == 5):
        print('You win! Lizard 🦎 poisons Spock 🖖.')
    elif (player == 5 and computer == 1):
        print('You win! Spock 🖖 vaporizes Rock ✊.')
    elif (player == 5 and computer == 2):
        print('Computer wins! Paper ✋ disproves Spock 🖖.')
    elif (player == 5 and computer == 3):
        print('You win! Spock 🖖 smashes Scissors ✌️.')
    elif (player == 5 and computer == 4):
        print('Computer wins! Lizard 🦎 poisons Spock 🖖.')
    else:
        print('Oops! You encountered an ultra rare error that requires a restart.')


def playAgain():
    print('\n' + '='*40 + '\n')
    play_again = input('Do you want to play again? (y/n) OR (yes/no): ').lower()
    if play_again == 'yes' or play_again == 'y':
        print('\n' + '='*40 + '\n')
        menu()
        main()  # Restart the game
    elif play_again == 'no' or play_again == 'n':
        print('Thanks for playing!')
    else:
        print('\033[1mInvalid input. Should be y/n OR yes/no.\033[0m')
        playAgain()  # Ask again if input is invalid

def main():
    print('\n' + '='*40 + '\n')
    player = player_choice()
    computer = computer_choice()
    winning_conditions(player, computer)
    playAgain()

if __name__ == '__main__': # This ensures the code runs only when this file is executed directly
    main()