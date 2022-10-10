from board import Board
from art import logo

print(logo)

board = Board()
board.display()

player = {
    1: 'X',
    2: 'O'
}

player1 = True
game_active = True

possible_plays = [
    '1A', '1B', '1C',
    '2A', '2B', '2C',
    '3A', '3B', '3C'
]

while game_active:
    # Execute current players turn then switch to other players turn
    if player1:
        position = input("Player1! It's your turn! Where do you want to play? 'Ex. 2C': ").upper()
        if position in possible_plays:
            if board.play(position, player[1]):
                player1 = False
        else:
            print('Invalid input, please try again.')
    else:
        position = input("Player2! It's your turn! Where do you want to play? 'Ex. 2C': ").upper()
        if position in possible_plays:
            if board.play(position, player[2]):
                player1 = True
        else:
            print('Invalid input, please try again.')

    # Check if the game is still on
    if board.check_winner() or board.is_full():
        if board.check_winner():
            board.reveal_winner()
        elif board.is_full():
            print("There was no winner this round")

        still_playing = input("Would you like to play again? 'Yes' or 'No'\n").lower()
        if still_playing == 'yes':
            board.new_board()
            board.display()
        else:
            game_active = False
            print("THANKS FOR PLAYING!!!")
