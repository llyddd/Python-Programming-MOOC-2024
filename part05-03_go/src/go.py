# Write your solution here
def who_won(game_board: list):
    onectr = 0
    twoctr = 0
    for i in range(len(game_board)): # using the number of rows in the matrix
        for j in range(len(game_board[i])): # using the number of items on each row 
            if game_board[i][j] == 1:
                onectr += 1
            elif game_board[i][j] == 2:
                twoctr += 1
    if onectr > twoctr:
        return 1
    elif twoctr > onectr:
        return 2
    else:
        return 0
   

if __name__ == "__main__":
    goList = [
  [1, 1, 1, 1, 1, 1,1, 1, 1],
  [2, 0, 0, 2, 1, 1, 1, 1, 0],
  [0, 2, 0, 1, 1, 0, 0, 0, 2],
  [2, 2, 1, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 2, 0, 1, 1, 0],
  [1, 0, 1, 0, 1, 0, 2, 0, 0],
  [0, 0, 1, 1, 0, 1, 1, 0, 0],
  [2, 2, 1, 0, 0, 0, 0, 0, 1],
  [2, 2, 2, 2, 2, 0, 0, 0, 2]
    ] 
    print(who_won(goList))