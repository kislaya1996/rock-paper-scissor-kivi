import random
class RockPaperScissor:
    POSSIBLE_MOVES = ['r',"p","s"]
    MOVE_PRIORITY_DICT = {'r':'s' ,'p':'r', 's':'p'}
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
            return "Cannot evaluate game"
        if self.computer_move == self.user_move:
            return "DRAW"
        if self.MOVE_PRIORITY_DICT[self.computer_move] == self.user_move:
            return "COMPUTER WINS!"
        else:
            return "YOU WIN!"

        

    