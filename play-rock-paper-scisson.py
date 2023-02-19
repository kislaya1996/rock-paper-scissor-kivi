import time
from rps import RockPaperScissor

def setup_game():
  return RockPaperScissor()
  
def play_game(game):
  user_move = input()
  while not RockPaperScissor.is_valid_move(user_move):
    print("You wrote something which I don't understand")
    time.sleep(1)
    print("You can choose r for rock, p for paper, or s for scissor. Try again")
    user_move = input()
  game.set_user_move(user_move)
  game.make_computer_move()
  result = game.evaluate()
  print('\n\n')
  print(result+'\n\n')



def main():
  game = setup_game()
  print("Welcome to the rock paper scissor game")
  time.sleep(2)
  print("Enter r for rock, p for paper and s for scissor, or the whole word if you are a lunatic")
  time.sleep(2)
  play_game(game)

  while True:
    user_input = input("To play again, press y\n")
    if user_input.lower()!='y':
      print("Thank you for playing")
      return
    else:
      print("Enter r for rock, p for paper and s for scissor, or the whole word if you are a lunatic")
      play_game(game)



if __name__ == '__main__':
  main()