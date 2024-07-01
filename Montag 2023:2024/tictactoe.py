def check_for_winner(game_board: list[list]):
	for i in range(3):
		if game_board[0][i] == 1 and game_board[1][i] == 1 and game_board[2][i] == 1:
			return 1
		if game_board[0][i] == -1 and game_board[1][i] == -1 and game_board[2][i] == -1:
			return -1
		if game_board[i][0] == 1 and game_board[i][1] == 1 and game_board[i][2] == 1:
			return 1
		if game_board[i][0] == -1 and game_board[i][1] == -1 and game_board[i][2] == -1:
			return -1
		
	if game_board[0][0] == 1 and game_board[1][1] == 1 and game_board[2][2] == 1:
			return 1
	if game_board[0][2] == 1 and game_board[1][1] == 1 and game_board[2][0] == 1:
			return 1
	
	if game_board[0][0] == -1 and game_board[1][1] == -1 and game_board[2][2] == -1:
			return -1
	if game_board[0][2] == -1 and game_board[1][1] == -1 and game_board[2][0] == -1:
			return -1
	
	return 0

def return_free_fields(game_board: list[list]):
	help = []
	
	for i in range(len(game_board)):
		for j in range(len(game_board[i])):
			if game_board[i][j] == 0:
				help.append([i,j])
	
	return help	

def best_move(game_board: list[list], color):
	if check_for_winner(game_board) == 0 and return_free_fields(game_board) == []:
		return "draw"
	else: 
		move_rating =  best_move_continue(game_board, color)

def best_move_continue(game_board: list[list], color):
	if check_for_winner(game_board) == color:
		return 1
	elif check_for_winner(game_board) == color * -1:
		return -1
	elif return_free_fields(game_board) == []:
		return 0
	
	free_fields = return_free_fields(game_board)
	move_rating = []
	for i in range(len(free_fields)):
		help = game_board
		help[free_fields[i][0]][free_fields[i][1]].append(color)
		move_rating.append(best_move_continue(help, color * -1)[])

	highest = [move_rating[i], 0]
	for i in range(1, len(move_rating)):
		if move_rating[i] > highest[0]:
			highest[0] = move_rating[i]
			highest[1] = i

	return highest
	


gameboard = [[0,0,0 ],
			 [0,-1,0],
			 [0,0,0]]

print(return_free_fields(gameboard, 1))

#gameboard = best_move(gameboard)
#print(gameboard)