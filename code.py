board = {'A1': ' ', 'A2': ' ', 'A3': ' ',
         
         'B1': ' ', 'B2': ' ', 'B3': ' ',
         
         'C1': ' ', 'C2': ' ', 'C3': ' '}

player= 1      
total_moves= 0  
checking = 0


def check():
    #horizontal
   
    if board['A1']== 'X' and board['A2']== 'X' and board['A3'] == 'X':
        print('Player one WINNER , PLAYER::2=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
   
    if board['B1']== 'X' and board['B2']== 'X' and board['B3'] == 'X':
        print('Player One WINNER, PLAYER::2=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
   
    if board['C1']== 'X' and board['C2']== 'X' and board['C3'] == 'X':
        print('Player One WINNER, PLAYER::2=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
   
    #horizontal(end)
    if board['A1']== 'X' and board['B2']== 'X' and board['C3']== 'X':
        print('Player One WINNER, PLAYER::2=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
   

    #vertically(start)
    if board['A1']== 'X' and board['B1']== 'X' and board['C1']== 'X':
        print('Player One WINNER, PLAYER::2=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
   
    if board['A2']== 'X' and board['B2']== 'X' and board['C2']== 'X':
        print('Player One WINNER, PLAYER::2=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
   
    if board['A3']== 'X' and board['B3']== 'X' and board['C3']== 'X':
        print('Player One WINNER, PLAYER::2=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
   
    #vertical(end)

    """P2"""
    if board['A1']== 'O' and board['A2']== 'O' and board['A3']== 'O':
        print('Player Two WINNER, PLAYER::1=  IS LOSS THE GAME ')
        print('//BETTER LUCK NEXT TIME\\')
        return 1  # used to end the game
   
    if board['B1']== 'O' and board['B2']== 'O' and board['B3']== 'O':
        print('Player Two WINNER, PLAYER::1=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
   
    if board['C1']== 'O' and board['C2']== 'O' and board['C3']== 'O':
        print('Player Two WINNER, PLAYER::1=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
   
   
   
   
    if board['A1']== 'O' and board['B2']== 'O' and board['C3']== 'O':
        print('Player Two WINNER, PLAYER::1=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
   
    if board['A1']== 'O' and board['B1']== 'O' and board['C1']== 'O':
        print('Player Two WINNER, PLAYER::1=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
   
    if board['A2']== 'O' and board['B2']== 'O' and board['C2']== 'O':
        print('Player Two WINNER, PLAYER::1=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
   
    if board['A3']== 'O' and board['B3']== 'O' and board['C3']== 'O':
        print('Player Two WINNER, PLAYER::1=  IS LOSS THE GAME')
        print('//BETTER LUCK NEXT TIME\\')
        return 1
        return 0


print('A1|A2|A3')
print('________')
print('B1|B2|B3')
print('--------')
print('C1|C2|C3')
print('"*"*"*"*"*"*"*"*"*"*"*"')

while (True):
    print(board['A1']+ '|' + board['A2'] + '|' + board['A3'])
    print('_|_|_')
    print(board['B1']+ '|' + board['B2'] + '|' + board['B3'])
    print('_|_|_')
    print(board['C1']+ '|' + board['C2'] + '|' + board['C3'])
   
    checking = check()
    if total_moves== 9 or checking== 1:
        break
    while True:    
        if player == 1:
            p1= input('player one= ')
            if p1.upper() in board and board[p1.upper()]== ' ':
                board[p1.upper()]= 'X'
                player = 2
                break
       
            else:
                print('Incorrect input, try again')
                continue
        else:
            p2= input('player two= ')
            if p2.upper() in board and board[p2.upper()]== ' ':
                board[p2.upper()] = 'O'
                player = 1
                break
            else:  
                print('Invalid input, please try again')
            continue
       
    total_moves+= 1
    print('"*"*"*"*"*"*"*"*"*"*"*"')

    print( 'Play Again ')