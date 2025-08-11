from osero.game.board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 1  # Black starts

    def switch_player(self):
        self.current_player = 3 - self.current_player

    def play_move(self, row, col):
        if self.board.place_piece(row, col, self.current_player):
            self.switch_player()
            return True
        return False

    def is_game_over(self):
        # Game is over if board is full or no player has a valid move
        if not self.board.get_valid_moves(1) and not self.board.get_valid_moves(2):
            return True

        counts = self.board.count_pieces()
        if counts[1] + counts[2] == self.board.size * self.board.size:
            return True

        return False

    def get_winner(self):
        if not self.is_game_over():
            return None  # Game not over yet

        counts = self.board.count_pieces()
        black_count = counts.get(1, 0)
        white_count = counts.get(2, 0)

        if black_count > white_count:
            return 1  # Black wins
        elif white_count > black_count:
            return 2  # White wins
        else:
            return 0  # Draw
