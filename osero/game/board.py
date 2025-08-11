import collections

class Board:
    def __init__(self):
        self.size = 9
        self.board = [[0] * self.size for _ in range(self.size)]
        # Initial pieces
        center = self.size // 2
        self.board[center - 1][center - 1] = 2  # White
        self.board[center - 1][center] = 1      # Black
        self.board[center][center - 1] = 1      # Black
        self.board[center][center] = 2          # White
        self.directions = [(-1, -1), (-1, 0), (-1, 1),
                           (0, -1),           (0, 1),
                           (1, -1), (1, 0), (1, 1)]

    def is_on_board(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def get_valid_moves(self, player):
        valid_moves = []
        for r in range(self.size):
            for c in range(self.size):
                if self.is_valid_move(r, c, player):
                    valid_moves.append((r, c))
        return valid_moves

    def is_valid_move(self, row, col, player):
        if not self.is_on_board(row, col) or self.board[row][col] != 0:
            return False

        opponent = 3 - player
        for dr, dc in self.directions:
            r, c = row + dr, col + dc
            if self.is_on_board(r, c) and self.board[r][c] == opponent:
                r += dr
                c += dc
                while self.is_on_board(r, c):
                    if self.board[r][c] == player:
                        return True
                    if self.board[r][c] == 0:
                        break
                    r += dr
                    c += dc
        return False

    def place_piece(self, row, col, player):
        if not self.is_valid_move(row, col, player):
            return False

        self.board[row][col] = player
        opponent = 3 - player
        pieces_to_flip = []

        for dr, dc in self.directions:
            r, c = row + dr, col + dc
            line = []
            while self.is_on_board(r, c) and self.board[r][c] == opponent:
                line.append((r, c))
                r += dr
                c += dc
            if self.is_on_board(r, c) and self.board[r][c] == player:
                pieces_to_flip.extend(line)

        for r, c in pieces_to_flip:
            self.board[r][c] = player

        return True

    def count_pieces(self):
        return collections.Counter(piece for row in self.board for piece in row)
