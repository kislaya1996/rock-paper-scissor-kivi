import random
class RockPaperScissor:
    POSSIBLE_MOVES = ['r',"p","s"]
    MOVE_PRIORITY_DICT = {'r':'s' ,'p':'r', 's':'p'}
    COMPUTER_WIN_MESSAGE = "COMPUTER WINS!"
    PLAYER_WIN_MESSAGE = "YOU WIN!"
    DRAW_MESSAGE = "DRAW"
    computer_move = None
    user_move = None

    @staticmethod
    def is_valid_move(user_move):
        if user_move.lower() in RockPaperScissor.POSSIBLE_MOVES:
            return True
        return False

    def set_user_move(self, user_move):
        self.user_move = user_move
        return

    def make_computer_move(self):
        self.computer_move = random.choice(self.POSSIBLE_MOVES)
        return
    
    def evaluate(self):
        if not (self.computer_move and self.user_move):
            raise Exception("missing-moves")
        if self.computer_move == self.user_move:
            return self.DRAW_MESSAGE
        if self.MOVE_PRIORITY_DICT[self.computer_move] == self.user_move:
            return self.COMPUTER_WIN_MESSAGE
        else:
            return self.PLAYER_WIN_MESSAGE

        

    