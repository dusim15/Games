import random

print("Welcome to Usim's game of ROCK, PAPER and SCISSORS!π€")
print('Remember, young grasshopper, SHOW NO MERCY!!!')
while True:
    actions = ['rock', 'paper', 'scissors']
    computer = random.choice(actions)
    player = None
    while player not in actions:
        player = input("Make a move: ").lower()
        if player == 'rock':
            print('πͺ¨πͺ¨πͺ¨')
        elif player == 'paper':
            print('πππ')
        elif player == 'scissors':
            print('βοΈβοΈβοΈ')

    if computer == player:
        print('COMPUTER=> {}'.format(computer))
        print("Sorry, it's deuceπ₯²")
    elif computer == 'paper' and player.capitalize() == 'Rock':
        print('COMPUTER=> {}'.format(computer))
        print('Computer: You lost!π')
    elif computer == 'rock' and player.capitalize() == 'Paper':
        print('COMPUTER=> {}'.format(computer))
        print('You win!ππ')
    elif computer == 'scissors' and player.capitalize() == 'Rock':
        print('COMPUTER=> {}'.format(computer))
        print('You win!ππ')
    elif computer == 'rock' and player.capitalize() == 'Scissors':
        print('COMPUTER=> {}'.format(computer))
        print('Computer: You lost!π')
    elif computer == 'paper' and player.capitalize() == 'Scissors':
        print('COMPUTER=> {}'.format(computer))
        print('You win!ππ')
    elif computer == 'scissors' and player.capitalize() == 'Paper':
        print('COMPUTER=> {}'.format(computer))
        print('Computer: You lost!π')

    play_again = input('Play again?π₯Ί (YES/NO): ').capitalize()

    if play_again != 'Yes':
        break

print('Goodbyeπ')
