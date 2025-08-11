import unittest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from osero.game.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        """Set up a new board for each test."""
        self.board = Board()

    def test_initial_board(self):
        """Test the initial setup of the board."""
        self.assertEqual(self.board.size, 9)
        # Check initial piece counts
        counts = self.board.count_pieces()
        self.assertEqual(counts[1], 2)  # 2 Black pieces
        self.assertEqual(counts[2], 2)  # 2 White pieces
        # Check initial positions
        self.assertEqual(self.board.board[3][4], 1)
        self.assertEqual(self.board.board[4][3], 1)
        self.assertEqual(self.board.board[3][3], 2)
        self.assertEqual(self.board.board[4][4], 2)

    def test_get_valid_moves_initial(self):
        """Test valid moves at the beginning of the game for Black."""
        valid_moves = self.board.get_valid_moves(1) # Player Black
        expected_moves = {(2, 3), (3, 2), (5, 4), (4, 5)}
        self.assertEqual(set(valid_moves), expected_moves)

    def test_is_valid_move(self):
        """Test is_valid_move method."""
        # Valid moves for Black at start
        self.assertTrue(self.board.is_valid_move(2, 3, 1))
        self.assertTrue(self.board.is_valid_move(3, 2, 1))
        # Invalid moves
        self.assertFalse(self.board.is_valid_move(0, 0, 1)) # No adjacent opponent
        self.assertFalse(self.board.is_valid_move(3, 3, 1)) # Occupied cell
        self.assertFalse(self.board.is_valid_move(9, 9, 1)) # Out of bounds

    def test_place_piece_and_flip(self):
        """Test placing a piece and the subsequent flip."""
        player = 1 # Black
        row, col = 2, 3
        self.board.place_piece(row, col, player)
        # Check if the new piece is placed
        self.assertEqual(self.board.board[row][col], player)
        # Check if the opponent's piece was flipped
        self.assertEqual(self.board.board[3][3], player)
        # Check piece count after move
        counts = self.board.count_pieces()
        self.assertEqual(counts[1], 4) # Black should have 4 pieces now
        self.assertEqual(counts[2], 1) # White should have 1 piece now

    def test_place_piece_multiple_flips(self):
        """Test a move that flips pieces in multiple directions."""
        # Set up a custom board state
        self.board.board = [[0] * 9 for _ in range(9)]
        self.board.board[4][4] = 1 # Player (Black)
        self.board.board[4][3] = 2 # Opponent (White)
        self.board.board[4][5] = 2 # Opponent (White)
        self.board.board[3][4] = 2 # Opponent (White)
        self.board.board[5][4] = 2 # Opponent (White)

        # Place a piece that should flip in 4 directions
        self.board.place_piece(4, 2, 1) # Black places at (4,2) - should not work
        self.board.place_piece(4, 6, 1) # Black places at (4,6)
        self.board.place_piece(2, 4, 1) # Black places at (2,4)
        self.board.place_piece(6, 4, 1) # Black places at (6,4)

        self.board.place_piece(3, 3, 1)
        self.assertEqual(self.board.board[3][4], 1)
        self.assertEqual(self.board.board[4][3], 1)

if __name__ == '__main__':
    unittest.main()
