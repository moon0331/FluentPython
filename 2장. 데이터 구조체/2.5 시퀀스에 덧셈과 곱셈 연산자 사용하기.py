l = [1,2,3]
print(l*5)
print(5*'abcd')

print('-'*50)

board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
print(board)

board2 = []
for i in range(3):
    row = ['_'] * 3
    board2.append(row)

board2[1][2] = 'X'
print(board == board2)

weird_board = [['_'] * 3] * 3
weird_board[1][2] = 'O'
print(weird_board)

row = ['_'] * 3
weird_board2 = []
for i in range(3):
    weird_board2.append(row)

weird_board2[1][2] = 'O'
print(weird_board == weird_board2)

print('-'*50)

