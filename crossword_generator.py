
def printboard(board):
    m = len(board)
    n = len(board[0])
    for i in range(m):
        if i == 0:
            print('0123456789' * 2, end = '')
            print()
        if i == 1:
            print('_' * (m+2), end = '')
            print()
        if i >= 1:
            print('|', end = '')
            for j in range(n):
                print(board[i][j], end = '')
            print('|', str(i),end='')
            print()
        if i == m-1:
            print('_'*(m+2), end = '')
            print()
            print('0123456789'*2, end = '')
                

def addFirstWord(board, word):
    midRow = len(board)//2    
    for j in range(len(word)):
        if len(word) > len(board):
            return False
        for i in range(len(word)):
            col  = len(board)//2 - len(word)//2 + i
            board[midRow][col] = word[i]
        return True

def checkvertical(board,word,row,col):
    blank = ' '
    if len(word) > 20-row:
        return False
    same = False
    for k in range(len(word)):
        wordLetter = word[k]
        boardLetter = board[row + k][col]
        
        if wordLetter == boardLetter:
            if k == 0:
                if board[row-1][col] != blank:
                    return False
                if board[row-1][col-1]!=blank:
                    return False
                if board[row+1][col-1] != blank or board[row+1][col+1] != blank:
                    return False
            else:
                if k == len(word) - 1:
                    if board[row+1][col] != blank:
                        return False
                    for l in range(len(word)):
                        if board[row+l][col-1] != blank:
                            return False
                        if board[row+l][col+1] != blank:
                            return False
                for l in range(len(word)):
                    if board[row+l][col-1] != blank:
                        return False
                    if board[row+l][col+1] != blank:
                        return False
            if (row == 20 or col == 20) and word[k] != word[len(word)-1]:
                return False
           
            same = True
            
        
        elif boardLetter == blank:
            continue

        elif board[row][col+1] != blank:
            return False
            
        elif boardLetter != wordLetter:
            return False
     
    return same

def addvertical(board, word):
    for i in range(len(board)):
        for j in range(len(board)):
            if checkvertical(board,word,i,j):
                for k in range(len(word)):
                    board[i+k][j] = word[k]
                return True
    print()
    print("Error placing", word)
    print()
    return False

def checkhorizontal(board,word,row,col):
    blank = ' '
    if len(word) > 20-col:
        return False
    same = False
    for k in range(len(word)):
        wordLetter = word[k]
        boardLetter = board[row][col+k]
        if wordLetter == boardLetter:
            if k == 0:
                if board[row][col-1] != blank:
                    return False
                if board[row-1][col] != blank or board[row+1][col] != blank:
                    return False
            else:
                if k == len(word) - 1:
                    if board[row][col+1] != blank:
                        return False
                    if board[row-1][col] != blank or board[row+1][col] != blank:
                        return False
                    
                for l in range(len(word)):
                    if board[row-1][col] != blank or board[row+1][col] != blank:
                        return False
                if board[row-1][col] != blank or board[row+1][col] != blank:
                    return False
            if (row == 20 or col == 20) and word[k] != word[len(word)-1]:
                return False
            same = True
        
        if boardLetter == blank:
            continue
        elif boardLetter != wordLetter:
            return False
     
    return same

def addhorizontal(board, word):
    for i in range(len(board)):
        for j in range(len(board)):
            if checkhorizontal(board, word, i, j):
                for k in range(len(word)):
                    board[i][j+k] = word[k]
                return True
    print()
    print("Error placing: ", word)
    print()
    return False

blank = ' '
board = [[blank]*20 for i in range(20)]  
def addwords(board, L):
    addFirstWord(board, L[0])
    for i in range(1,len(L)):
        if i %2 == 1:
            x = str(addvertical(board, L[i]))
        elif i%2 == 0:
            x = str(addhorizontal(board, L[i]))
        
    return x
    


L = ["hippopotamus", "horse", "loon", "love", "race", "horse", "data"]
L1 = ["snake", "love", "sassy", "append", "love", "race", "horse", "data",
      "addle", "apple", "ask", "kick"]

     
def crosswords(L):
    blank = ' '
    board = [[blank]*20 for i in range(20)]
    addwords(board, L)
    printboard(board)


crosswords(L)
crosswords(L1)

