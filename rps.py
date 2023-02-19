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
    def is_valid_move(user_move: str) -> bool:
        '''
        Checks if a user input lies in the domain of moves within the game
        '''
        if user_move.lower() in RockPaperScissor.POSSIBLE_MOVES:
            return True
        return False

    def set_user_move(self, user_move: str) -> None:
        '''
        user_move setter in the game object
        '''
        self.user_move = user_move
        return

    def make_computer_move(self) -> None:
        '''
        computer_move setter in the game object.
        Random selection made from within the domain of moves in the game
        '''
        self.computer_move = random.choice(self.POSSIBLE_MOVES)
        return
    
    def evaluate(self) -> str:
        '''
        returns str:
            The message declaring the result of the game

        Evaluates the user move vs the computer move in the game. 
        Follows the priority order same the game, ie paper beats rock, rock beats scissor, and scissor beats paper
        '''
        if not (self.computer_move and self.user_move):
            raise Exception("missing-moves")
        if self.computer_move == self.user_move:
            return self.DRAW_MESSAGE
        if self.MOVE_PRIORITY_DICT[self.computer_move] == self.user_move:
            return self.COMPUTER_WIN_MESSAGE
        else:
            return self.PLAYER_WIN_MESSAGE

        

    