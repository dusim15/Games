import random

print("Welcome to Usim's game of ROCK, PAPER and SCISSORS!🤓")
print('Remember, young grasshopper, SHOW NO MERCY!!!')
while True:
    actions = ['rock', 'paper', 'scissors']
    computer = random.choice(actions)
    player = None
    while player not in actions:
        player = input("Make a move: ").lower()
        if player == 'rock':
            print('🪨🪨🪨')
        elif player == 'paper':
            print('📄📄📄')
        elif player == 'scissors':
            print('✂️✂️✂️')

    if computer == player:
        print('COMPUTER=> {}'.format(computer))
        print("Sorry, it's deuce🥲")
    elif computer == 'paper' and player.capitalize() == 'Rock':
        print('COMPUTER=> {}'.format(computer))
        print('Computer: You lost!😈')
    elif computer == 'rock' and player.capitalize() == 'Paper':
        print('COMPUTER=> {}'.format(computer))
        print('You win!🎉🎉')
    elif computer == 'scissors' and player.capitalize() == 'Rock':
        print('COMPUTER=> {}'.format(computer))
        print('You win!🎉🎉')
    elif computer == 'rock' and player.capitalize() == 'Scissors':
        print('COMPUTER=> {}'.format(computer))
        print('Computer: You lost!😈')
    elif computer == 'paper' and player.capitalize() == 'Scissors':
        print('COMPUTER=> {}'.format(computer))
        print('You win!🎉🎉')
    elif computer == 'scissors' and player.capitalize() == 'Paper':
        print('COMPUTER=> {}'.format(computer))
        print('Computer: You lost!😈')

    play_again = input('Play again?🥺 (YES/NO): ').capitalize()

    if play_again != 'Yes':
        break

print('Goodbye😊')
