#!/usr/bin/python

# import random

def game_introduction():
    print("Welcome to the Tic Tac Toe game", "\n")
    print("Game's rules: Player 1 is X , player 2 is O."
          "Players take turns putting their marks in empty squares."
          "The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner." 
          "When all 9 squares are full, the game is over.", "\n")

def create_grid(array):
    row_1 = " {} | {} | {} ".format(array[0], array[1], array[2])
    row_2 = " {} | {} | {} ".format(array[3], array[4], array[5])
    row_3 = " {} | {} | {} ".format(array[6], array[7], array[8])

    print("", row_1, "\n", row_2, "\n", row_3, "\n")

def player_move(turn, array):
   if turn  == "X":
      player = 1
   elif turn == "O":
      player = 2
   print("Your turn player {}". format(player))

   user_input= int(input("Enter your move (1-9): "))
   if array[user_input - 1] == "-":
      array[user_input - 1] = turn
   else:
      print()
      print("This space is already taken!! ")


def check_winner(turn, array):
   if(array[0] == turn and array[1] == turn and array[2] == turn) or \
     (array[3] == turn and array[4] == turn and array[5] == turn) or \
     (array[6] == turn and array[7] == turn and array[8] == turn) or \
     (array[0] == turn and array[3] == turn and array[6] == turn) or \
     (array[1] == turn and array[4] == turn and array[7] == turn) or \
     (array[2] == turn and array[5] == turn and array[8] == turn) or \
     (array[0] == turn and array[4] == turn and array[8] == turn) or \
     (array[2] == turn and array[4] == turn and array[6] == turn):
      return True
   else:
      return False

def main():
    
    array = ["-" for i in range(9)]

    game_introduction()
    
    while True:
      create_grid(array)
      player_move("X", array)
      create_grid(array)
      if check_winner("X", array):
         print("X player wins")
         break
      player_move("O", array)
      if check_winner("O", array):
        create_grid(array)
        print("O player wins ")
        break
    
if __name__ == "__main__":
  main()
