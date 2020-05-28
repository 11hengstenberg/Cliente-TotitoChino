#Fernando Hengstenberg

#variables
gamesF = 0
gamesW = 0
gamesL = 0

#juego terminado
def miniMax(board, depth, isMax, player_turn_id):


    
    """
    #contador de cuadros.
    acumulador1 = 0
    contador1 = 0
    contadorPuntos1 = 0
    
    for aa in range(len(board[0])):
        if ((aa + 1) % 6) != 0:
            if board[0][aa] != 99 and board[0][aa + 1] != 99 and board[1][contador1 + acumulador1] != 99 and board[1][contador1 + acumulador1 + 1] != 99:
                contadorPuntos1 = contadorPuntos1 + 1

            acumulador1 = acumulador1 + 6

        else:
            contador1 = contador1 + 1
            acumulador1 = 0


    score =evaluate(board,player_turn_id)
    if (score == 10):
        return score
    if (score == -10):
        return score
    
    if (isMoveLeft(board)== False):
        return 0
    
    


    if (isMax== True):
        best = -90000000
        for i in range (len(board)):
            for j in range (len(board[0])):
                if (board[i][j]==99):
                    ##meter el valor correcto para hacer el tiro
                    board[i][j] = 0


                    acumulador3 = 0
                    contador3 = 0
                    contadorPuntos3 = 0
    
                    for q in range(len(board[0])):
                        if ((q + 1) % 6) != 0:
                            if board[0][q] != 99 and board[0][q + 1] != 99 and board[1][contador3 + acumulador3] != 99 and board[1][contador3 + acumulador3 + 1] != 99:
                                contadorPuntos3 = contadorPuntos3 + 1

                            acumulador3 = acumulador3 + 6

                        else:
                            contador3 = contador3 + 1
                            acumulador3 = 0
                    if(contador3-contador1==1 and player_turn_id ==1):
                        board[i][j]=1
                    if (contador3-contador1==2 and player_turn_id ==1):
                        board[i][j]=2
                    if(contador3-contador1==1 and player_turn_id ==2):
                        board[i][j]=-1
                    if (contador3-contador1==2 and player_turn_id ==2):
                        board[i][j]=-2

                    best = max(best,miniMax(board,depth+1,False,player_turn_id))
                    
                    board[i][j] = 99

        return best

    if (isMax==False):
        best = 90000000

        for i in range (len(board)):
            for j in range (len(board[0])):
                if (board[i][j] == 99):

                    #movimiento del enemigo.
                    board[i][j] = 0

                    acumulador2 = 0
                    contador2 = 0
                    contadorPuntos2 = 0
    
                    for r in range(len(board[0])):
                        if ((r + 1) % 6) != 0:
                            if board[0][r] != 99 and board[0][r + 1] != 99 and board[1][contador2 + acumulador2] != 99 and board[1][contador2 + acumulador2 + 1] != 99:
                                contadorPuntos2 = contadorPuntos2 + 1

                            acumulador2 = acumulador2 + 6

                        else:
                            contador2 = contador2 + 1
                            acumulador2 = 0
                    if(contador2-contador1==1 and player_turn_id ==2):
                        board[i][j]=1
                    if (contador2-contador1==2 and player_turn_id ==2):
                        board[i][j]=2
                    if(contador2-contador1==1 and player_turn_id ==1):
                        board[i][j]=-1
                    if (contador2-contador1==2 and player_turn_id ==1):
                        board[i][j]=-2
                    best= min(best,miniMax(board,depth+1,True,player_turn_id))
                    board[i][j] = 99
                    

        return best
"""



def findBestMove (board,player_turn_id):
    bestVal = -90000000000
    bestMoveLocation = -1
    bestMovePosition = -1
    

    for i in range (len(board)):
        for j in range (len(board[0])):
            if (board[i][j]== 99):
              
                #movimiento.
                board[i][j]=0
                moveVal = miniMax(board, 0, False, player_turn_id)

                board[i][j] = 99

                if (moveVal>bestVal):
                    bestMoveLocation = i
                    bestMovePosition = j
                    bestVal=moveVal

    bestMove = [bestMoveLocation,bestMovePosition]
    return bestMove




                





#verificamos si el el movimiento esta disponible.   
def isMoveLeft (board):
    fullBoard=board[0]+board[1]

    for i in range (len(fullBoard)):
        if (fullBoard[i]==99):
            return True
    return False


        




#funcion para evaluar el tablero final.
def evaluate(board,player_turn_id):
    acumulador = 0
    contador = 0
    contadorPuntos = 0
    
    for i in range(len(board[0])):
        if ((i + 1) % 6) != 0:
            if board[0][i] != 99 and board[0][i + 1] != 99 and board[1][contador + acumulador] != 99 and board[1][contador + acumulador + 1] != 99:
                contadorPuntos = contadorPuntos + 1

            acumulador = acumulador + 6

        else:
            contador = contador + 1
            acumulador = 0
    #print("Cantidad de cuadritos cerrados: ", contadorPuntos)

    ## Aqui está como se cuentan los puntos de cada jugador cuando reciben el tablero
    player1 = 0
    player2 = 0
    FILLEDP11 = 1
    FILLEDP12 = 2
    FILLEDP21 = -1
    FILLEDP22 = -2


    for i in range(len(board[0])):
        if board[0][i] == FILLEDP12:
            player1 = player1 + 2
        elif board[0][i] == FILLEDP11:
            player1 = player1 + 1
        elif board[0][i] == FILLEDP22:
            player2 = player2 + 2
        elif board[0][i] == FILLEDP21:
            player2 = player2 + 1

    for j in range(len(board[1])):
        if board[1][j] == FILLEDP12:
            player1 = player1 + 2
        elif board[1][j] == FILLEDP11:
            player1 = player1 + 1
        elif board[1][j] == FILLEDP22:
            player2 = player2 + 2
        elif board[1][j] == FILLEDP21:
            player2 = player2 + 1

 
    if ((player_turn_id==1 and player1>player2) or (player_turn_id==2 and player2>player1)):
        return +1
    if ((player_turn_id==2 and player1>player2) or (player_turn_id==1 and player2>player1)):
        return -1
    if ((player_turn_id==2 and player1==player2) or (player_turn_id==1 and player2==player1)):
        return 0



"""
    ## Aqui imprimimos los punteos de cada jugador
    if (player_turn_id == 1):
        print("-------------punteos-------------")
        print("Punteo de: ",username, player1)
        print("Punteo del contrincante: ", player2)
    
    if (player_turn_id == 2):
        print("-------------punteos-------------")
        print("Punteo de: ",username, player2)
        print("Punteo del contrincante: ", player1)
"""




#contador de los juegos
def contador(winner,losses):
   global gamesF
   global gamesL
   global gamesW
   if (winner == 1):
       gamesW+=1
       gamesF+=1
       print("----------partida:",gamesF,"----------")
       print("juegos terminados:", gamesF)
       print("juegos ganados:", gamesW)
       print("juegos perdidos: ", gamesL)
       print (" ")
   if (losses ==1):
       gamesL+=1
       gamesF+=1
       print("----------partida:",gamesF,"----------")
       print("juegos terminados:", gamesF)
       print("juegos ganados:", gamesW)
       print("juegos perdidos: ", gamesL)
       print (" ")
