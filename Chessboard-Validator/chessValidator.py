chessBoard = {
     '8a': ' ', '8b': ' ', '8c': ' ', '8d': ' ', '8e': ' ', '8f': ' ', '8g': ' ', '8h': ' ',
     '7a': ' ', '7b': ' ', '7c': ' ', '7d': ' ', '7e': ' ', '7f': ' ', '7g': ' ', '7h': ' ',
     '6a': ' ', '6b': ' ', '6c': ' ', '6d': ' ', '6e': ' ', '6f': ' ', '6g': ' ', '6h': ' ',
     '5a': ' ', '5b': ' ', '5c': ' ', '5d': ' ', '5e': ' ', '5f': ' ', '5g': ' ', '5h': ' ',
     '4a': ' ', '4b': ' ', '4c': ' ', '4d': ' ', '4e': ' ', '4f': ' ', '4g': ' ', '4h': ' ',
     '3a': ' ', '3b': ' ', '3c': ' ', '3d': ' ', '3e': ' ', '3f': ' ', '3g': ' ', '3h': ' ',
     '2a': ' ', '2b': ' ', '2c': ' ', '2d': ' ', '2e': ' ', '2f': ' ', '2g': ' ', '2h': ' ',
     '1a': ' ', '1b': ' ', '1c': ' ', '1d': ' ', '1e': ' ', '1f': ' ', '1g': ' ', '1h': ' ',
}


# Create a visual model of the chess board
def printBoard(board):
     print(board['8a'] + '|' + board['8b'] + '|' + board['8c'] + '|' + board['8d'] + '|' + board['8e'] + '|' + board['8f'] + '|' + board['8g'] + '|' + board['8h'])
     print('-+-+-+-+-+-+-+-')
     print(board['7a'] + '|' + board['7b'] + '|' + board['7c'] + '|' + board['7d'] + '|' + board['7e'] + '|' + board['7f'] + '|' + board['7g'] + '|' + board['7h'])
     print('-+-+-+-+-+-+-+-')
     print(board['6a'] + '|' + board['6b'] + '|' + board['6c'] + '|' + board['6d'] + '|' + board['6e'] + '|' + board['6f'] + '|' + board['6g'] + '|' + board['6h'])
     print('-+-+-+-+-+-+-+-')
     print(board['5a'] + '|' + board['5b'] + '|' + board['5c'] + '|' + board['5d'] + '|' + board['5e'] + '|' + board['5f'] + '|' + board['5g'] + '|' + board['5h'])
     print('-+-+-+-+-+-+-+-')
     print(board['4a'] + '|' + board['4b'] + '|' + board['4c'] + '|' + board['4d'] + '|' + board['4e'] + '|' + board['4f'] + '|' + board['4g'] + '|' + board['4h'])
     print('-+-+-+-+-+-+-+-')
     print(board['3a'] + '|' + board['3b'] + '|' + board['3c'] + '|' + board['3d'] + '|' + board['3e'] + '|' + board['3f'] + '|' + board['3g'] + '|' + board['3h'])
     print('-+-+-+-+-+-+-+-')
     print(board['2a'] + '|' + board['2b'] + '|' + board['2c'] + '|' + board['2d'] + '|' + board['2e'] + '|' + board['2f'] + '|' + board['2g'] + '|' + board['2h'])
     print('-+-+-+-+-+-+-+-')
     print(board['1a'] + '|' + board['1b'] + '|' + board['1c'] + '|' + board['1d'] + '|' + board['1e'] + '|' + board['1f'] + '|' + board['1g'] + '|' + board['1h'])


# Check if pieces are on a valid board
def isValidChessBoard(board):
     # Pieces
     wpawns = 0 # Max 8
     wking = 0 # Max 1
     wqueen = 0 # Max 1
     wbishop = 0 # Max 2
     wrook = 0 # Max 2
     wknight = 0 # Max 2
     bpawns = 0 # Max 8
     bking = 0 # Max 1
     bqueen = 0 # Max 1
     bbishop = 0 # Max 2
     brook = 0 # Max 2
     bknight = 0 # Max 2
     
     # Keep track of turn
     turn = "w"

     for i in range(32):
          printBoard(chessBoard)
          print("Turn for " + turn + ". What piece? (p)awn (k)ing (q)ueen (b)ishop (kn)ight (r)ook")
          piece = input()

          # Check for right input
          while True:
               if turn == 'w':
                    if piece == 'p':
                         if wpawns == 8:
                              print('Insufficient pawns. Choose different piece: ', end='')
                              piece = input()
                         else:
                              wpawns += 1
                              piece = 'wpawn'
                              break
                    elif piece == 'k':
                         if wking == 1:
                              print('Insufficient kings. Choose different piece: ', end='')
                              piece = input()
                         else:
                              wking += 1
                              piece = 'wking'
                              break
                    elif piece == 'q':
                         if wqueen == 1:
                              print('Insufficient queens. Choose different piece: ', end='')
                              piece = input()
                         else:
                              wqueen += 1
                              piece = 'wqueen'
                              break
                    elif piece == 'b':
                         if wbishop == 2:
                              print('Insufficient bishops. Choose different piece: ', end='')
                              piece = input()
                         else:
                              wbishop += 1
                              piece = 'wbishop'
                              break
                    elif piece == 'kn':
                         if wknight == 2:
                              print('Insufficient knights. Choose different piece: ', end='')
                              piece = input()
                         else:
                              wknight += 1
                              piece = 'wknight'
                              break
                    elif piece == 'r':
                         if wrook == 2:
                              print('Insufficient rooks. Choose different piece: ', end='')
                              piece = input()
                         else:
                              wrook += 1
                              piece = 'wrook'
                              break                    
                    else:
                         print('Wrong piece. Type p, k, q, b, kn or r: ', end='')
                         piece = input()
               else:
                    if piece == 'p':
                         if bpawns == 8:
                              print('Insufficient pawns. Choose different piece: ', end='')
                              piece = input()
                         else:
                              bpawns += 1
                              piece = 'bpawn'
                              break
                    elif piece == 'k':
                         if bking == 1:
                              print('Insufficient kings. Choose different piece: ', end='')
                              piece = input()
                         else:
                              bking += 1
                              piece = 'bking'
                              break
                    elif piece == 'q':
                         if bqueen == 1:
                              print('Insufficient queens. Choose different piece: ', end='')
                              piece = input()
                         else:
                              bqueen += 1
                              piece = 'bqueen'
                              break
                    elif piece == 'b':
                         if bbishop == 2:
                              print('Insufficient bishops. Choose different piece: ', end='')
                              piece = input()
                         else:
                              bbishop += 1
                              piece = 'bbishop'
                              break
                    elif piece == 'kn':
                         if bknight == 2:
                              print('Insufficient knights. Choose different piece: ', end='')
                              piece = input()
                         else:
                              bknight += 1
                              piece = 'bknight'
                              break
                    elif piece == 'r':
                         if brook == 2:
                              print('Insufficient rooks. Choose different piece: ', end='')
                              piece = input()
                         else:
                              brook += 1
                              piece = 'brook'
                              break                    
                    else:
                         print('Wrong piece. Type p, k, q, b, kn or r: ', end='')
                         piece = input()

          # Ask for which space on the board
          print("On which space?")
          space = input()

          # Check if it's a valid space
          while True:
               if space in board.keys():
                    break
               else:
                    print('Invalid space. Choose between 1a to 8h: ', end='')
                    space = input()

          # Change the turn
          if turn == 'w':
               turn = 'b'
          else:
               turn = 'w'

          # Validate space
          board[space] = piece


# Print the board on the screen
printBoard(isValidChessBoard(chessBoard))
