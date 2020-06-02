"""
Fernando Hengstenberg

based on:
Minimax:
        https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/

Poda Alpha/Beta
        https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/?ref=rp
"""
#evaluate board and movements.
def evaluate(board, move,player_turn_id,isMax):
    acumulador = 0
    contador = 0
    contadorPuntos = 0

    acumulador1 = 0
    contador1 = 0
    contadorPuntos1 = 0

    for i in range(len(board[0])):
        if ((i + 1) % 6) != 0:
            if board[0][i] != 99 and board[0][i + 1] != 99 and board[1][contador + acumulador] != 99 and board[1][contador + acumulador + 1] != 99:
                contadorPuntos = contadorPuntos + 1
            acumulador = acumulador + 6
        else:
            contador = contador + 1
            acumulador = 0

    board[move[0]][move[1]] = 0

    for i in range(len(board[0])):
        if ((i + 1) % 6) != 0:
            if board[0][i] != 99 and board[0][i + 1] != 99 and board[1][contador1 + acumulador1] != 99 and board[1][contador1 + acumulador1 + 1] != 99:
                contadorPuntos1 = contadorPuntos1 + 1
            acumulador1 = acumulador1 + 6
        else:
            contador1 = contador1 + 1
            acumulador1 = 0
    if (isMax==True):
        return (contadorPuntos1 - contadorPuntos)
    if (isMax == False):
        return ( (contadorPuntos1 - contadorPuntos)*-1)

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

    if (depth == 0):
        return evaluate(board, move, player_turn_id, not isMax)
    if (isMax== True):
        player_turn_id=player_turn_id
    if (isMax == False):
        player_turn_id = (player_turn_id % 2) + 1
    if (evaluate(board, move, player_turn_id, not isMax) != 0):
        return evaluate(board, move, player_turn_id, not isMax)
       
    possibleMoves = movesLeft(board)
    #max
    if (isMax==True):
        best = -100000
        for i in possibleMoves:
            board= newMove(board, move, player_turn_id, isMax)
            val = miniMax(board, depth + 1,False, player_turn_id, alpha, beta,nodeIndex+1, i)
            best = max(best, val)
            alpha = max(alpha, val)
            if (beta <= alpha):
                break

        board[move[0]][move[1]] = 99
        return best
    #min
    if (isMax==False):
        best = +100000
        for movimiento in possibleMoves:
            board= newMove(board, move, player_turn_id, isMax)
            val = miniMax(board,depth + 1, True,  player_turn_id,  alpha, beta,nodeIndex+1, movimiento,)
            best = min(best, val)
            beta = min(beta, val)
            if (beta <= alpha):
                break
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

def newMove(board, move, player_turn_id, isMax):
    acumulador = 0
    contador = 0
    contadorPuntos = 0

    acumulador1 = 0
    contador1 = 0
    contadorPuntos1=0
#nuevo movimiento
    for i in range(len(board[0])):
        if ((i + 1) % 6) != 0:
            if board[0][i] != 99 and board[0][i + 1] != 99 and board[1][contador + acumulador] != 99 and board[1][contador + acumulador + 1] != 99:
                contadorPuntos = contadorPuntos + 1
            acumulador = acumulador + 6
        else:
            contador = contador + 1
            acumulador = 0

    board[move[0]][move[1]] = 0

    for i in range(len(board[0])):
        if ((i + 1) % 6) != 0:
            if (board[0][i] != 99 and board[0][i + 1] != 99 and board[1][contador1 + acumulador1] != 99 and board[1][contador1 + acumulador1 + 1] != 99):
                contadorPuntos1 = contadorPuntos1 + 1
            acumulador1 = acumulador1 + 6
        else:
            contador1 = contador1 + 1
            acumulador1 = 0    
    if (player_turn_id == 1):
        if (contadorPuntos1 - contadorPuntos == 2):
            board[move[0]][move[1]] = 2
        if (contadorPuntos1 - contadorPuntos == 1):
            board[move[0]][move[1]] = 1
    if (player_turn_id == 2):
        if (contadorPuntos1 - contadorPuntos == 2):
            board[move[0]][move[1]] = -2
        if (contadorPuntos1 - contadorPuntos == 1):
            board[move[0]][move[1]] = -1
    if (isMax ==True):
        return (board)
    if (isMax == False):
        return (board)