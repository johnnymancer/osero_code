from osero.game.game import Game

def print_board(board):
    header = ' ' + ' '.join(str(i) for i in range(board.size))
    print(header)
    for r_idx, row in enumerate(board.board):
        row_str = str(r_idx)
        for piece in row:
            if piece == 1:
                row_str += ' B'
            elif piece == 2:
                row_str += ' W'
            else:
                row_str += ' .'
        print(row_str)
    print()

def main():
    game = Game()
    player_map = {1: "Black (B)", 2: "White (W)"}

    while not game.is_game_over():
        print_board(game.board)

        player_name = player_map[game.current_player]
        print(f"Player's turn: {player_name}")

        valid_moves = game.board.get_valid_moves(game.current_player)
        if not valid_moves:
            print("No valid moves. Skipping turn.")
            game.switch_player()
            continue

        print("Valid moves:", ", ".join(map(str, valid_moves)))

        try:
            move_str = input("Enter your move as row,col: ")
            row, col = map(int, move_str.split(','))

            if (row, col) in valid_moves:
                game.play_move(row, col)
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input format. Please use row,col.")

    print("Game Over!")
    print_board(game.board)
    winner = game.get_winner()
    if winner == 0:
        print("It's a draw!")
    else:
        print(f"Winner is: {player_map[winner]}")

    counts = game.board.count_pieces()
    print(f"Final score: Black {counts.get(1,0)} - White {counts.get(2,0)}")


if __name__ == "__main__":
    main()
