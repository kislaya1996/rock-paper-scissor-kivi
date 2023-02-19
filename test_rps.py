from rps import RockPaperScissor
import unittest

class TestingRPS(unittest.TestCase):

    def test_correct_is_valid_move(self):
        self.assertTrue(RockPaperScissor.is_valid_move('r'))
        self.assertTrue(RockPaperScissor.is_valid_move('p'))
        self.assertTrue(RockPaperScissor.is_valid_move('s'))
        self.assertTrue(RockPaperScissor.is_valid_move('R'))
        self.assertTrue(RockPaperScissor.is_valid_move('P'))
        self.assertTrue(RockPaperScissor.is_valid_move('S'))
        

    def test_incorrect_is_valid_move(self):
        self.assertFalse(RockPaperScissor.is_valid_move(' '))
        self.assertFalse(RockPaperScissor.is_valid_move('$'))
        self.assertFalse(RockPaperScissor.is_valid_move('2'))
        
    def test_set_user_move(self):
        game = RockPaperScissor()
        game.set_user_move('r')
        self.assertEqual(game.user_move,'r')

    def test_make_computer_move(self):
        game = RockPaperScissor()
        game.make_computer_move()
        self.assertIn(game.computer_move, RockPaperScissor.POSSIBLE_MOVES)

    def test_evaluate_with_inputs(self):
        game = RockPaperScissor()
        game.user_move = "r"
        game.computer_move = "p"
        self.assertEqual(game.evaluate(), RockPaperScissor.COMPUTER_WIN_MESSAGE)

    def test_evaluate_missing_inputs(self):
        game = RockPaperScissor()
        game.user_move = "r"
        game.computer_move = None
        self.assertRaises(Exception)




if __name__ == "__main__":
    unittest.main()