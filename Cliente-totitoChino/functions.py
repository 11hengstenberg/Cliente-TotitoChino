#Fernando Hengstenberg

"""based on:
        https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
"""
#evaluate board and movements.
def evaluate(board, move,playerNumber,isMax):

    board = list(map(list, board))
    punteo1 = 0
    punteo = 0
    acumulador = 0
    contador = 0

    for i in range(len(board[0])):
        if ((i + 1) % 6) != 0:
            if board[0][i] != 99 and board[0][i + 1] != 99 and board[1][contador + acumulador] != 99 and board[1][contador + acumulador + 1] != 99:
                punteo1 = punteo1 + 1
            acumulador = acumulador + 6
        else:
            contador = contador + 1
            acumulador = 0

    board[move[0]][move[1]] = 0

    acumulador = 0
    contador = 0

    for i in range(len(board[0])):
        if ((i + 1) % 6) != 0:
            if board[0][i] != 99 and board[0][i + 1] != 99 and board[1][contador + acumulador] != 99 and board[1][contador + acumulador + 1] != 99:
                punteo = punteo + 1
            acumulador = acumulador + 6
        else:
            contador = contador + 1
            acumulador = 0
  
    if punteo1 < punteo:
        if playerNumber == 1:
            if (punteo - punteo1) == 2:
                board[move[0]][move[1]] = 2
            elif (punteo - punteo1) == 1:
                board[move[0]][move[1]] = 1
        elif playerNumber == 2:
            if (punteo - punteo1) == 2:
                board[move[0]][move[1]] = -2
            elif (punteo - punteo1) == 1:
                board[move[0]][move[1]] = -1
    if (isMax==True):
        return (punteo - punteo1)
    if (isMax == False):
        return ((-1) * (punteo - punteo1))

#find the best move for play
def findBestMove(board, player_turn_id):
    best= -10000
    validateMoves= []
    possibleMove = []

    for i in range (len (board)):
        for j in range (len(board[0])):
            if (board[i][j]==99):
                possibleMove.append((i,j))
    
    for k in possibleMove:
        score = miniMax(board,0,False,player_turn_id,-100000,+100000,0,k)
    
        if (score > best):
            best=score
            validateMoves.clear()
        if (score >= best):
            validateMoves.append(k)

    return [validateMoves[0][0],validateMoves[0][1]]


def miniMax (board, depth, isMax, player_turn_id,alpha, beta,nodeIndex,move):
    idPlayerPlaying = player_turn_id if isMax else (player_turn_id % 2) + 1

    if (depth == 0 or evaluate(board, move, player_turn_id, not isMax) != 0):
        return evaluate(board, move, idPlayerPlaying, not isMax)
    possibleMoves = movesLeft(board)
    #max
    if (isMax==True):
        best = -100000
        for i in possibleMoves:
            board= newMove(board, move, idPlayerPlaying, isMax)
            value = miniMax(board, depth + 1,False, idPlayerPlaying, alpha, beta,0, i)
            best = max(best, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break

        board[move[0]][move[1]] = 99
        return best
    #min
    if (isMax==False):
        best = +100000
        for movimiento in possibleMoves:
            board= newMove(board, move, idPlayerPlaying, isMax)
            value = miniMax(board,depth + 1, True,  idPlayerPlaying,  alpha, beta,0, movimiento,)
            best = min(best, value)
            beta = min(beta, value)

        board[move[0]][move[1]] = 99
        return best
    return 0

def movesLeft(board):
    moves = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 99:
                moves.append((i, j))
    return moves

def newMove(board, move, playerNumber, isMax):
    board = list(map(list, board))
    punteo1 = 0
    punteo = 0
    acumulador = 0
    contador = 0

    for i in range(len(board[0])):
        if ((i + 1) % 6) != 0:
            if board[0][i] != 99 and board[0][i + 1] != 99 and board[1][contador + acumulador] != 99 and board[1][contador + acumulador + 1] != 99:
                punteo1 = punteo1 + 1
            acumulador = acumulador + 6
        else:
            contador = contador + 1
            acumulador = 0

    board[move[0]][move[1]] = 0
    acumulador = 0
    contador = 0

    for i in range(len(board[0])):
        if ((i + 1) % 6) != 0:
            if board[0][i] != 99 and board[0][i + 1] != 99 and board[1][contador + acumulador] != 99 and board[1][contador + acumulador + 1] != 99:
                punteo = punteo + 1
            acumulador = acumulador + 6
        else:
            contador = contador + 1
            acumulador = 0
    
    if punteo1 < punteo:
        if playerNumber == 1:
            if (punteo - punteo1) == 2:
                board[move[0]][move[1]] = 2
            elif (punteo - punteo1) == 1:
                board[move[0]][move[1]] = 1
        elif playerNumber == 2:
            if (punteo - punteo1) == 2:
                board[move[0]][move[1]] = -2
            elif (punteo - punteo1) == 1:
                board[move[0]][move[1]] = -1
    if (isMax ==True):
        return (board, punteo - punteo1)
    if (isMax == False):
        return (board, (-1) * (punteo - punteo1))