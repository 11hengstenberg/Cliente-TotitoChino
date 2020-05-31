#Fernando Hengstenberg

import random
#variables
gamesF = 0
gamesW = 0
gamesL = 0

#juego terminado
def miniMax(board, depth, isMax, player_turn_id):

        if (player_turn_id==1):
            posicionCorrecta=1
        if (player_turn_id==2):
            posicionCorrecta=-1
        cuadrosL1=cuadrosCompletos(board)

        score =evaluate(board,player_turn_id)

        if(depth==3):
            return score

        if  (score== 1):
            return score
        if (score == -1):
            return score


        #score =  evaluate(board,player_turn_id)
        if(isMoveLeft(board) == False):
            return score
        
        #maximizar
        if (isMax==True):
            best = -1000
            for i in range (len(board)):
                for j in range (len(board[0])):
                    if (board[i][j]==99):
                        board[i][j]=0
                        cuadrosL2=cuadrosCompletos(board)
                        if (cuadrosL2-cuadrosL1==1):
                            board[i][j]=1*posicionCorrecta
                        if (cuadrosL2-cuadrosL1==2):
                            board[i][j]=2*posicionCorrecta
                        best = max(best,miniMax(board,depth+1,False,player_turn_id))
                        print(best)
                        board[i][j]=99
 
            return best
        #minimizar
        if (isMax == False):
            best=1000
            for i in range (len(board)):
                for j in range (len(board[0])):
                    if (board[i][j]==99):
                        board[i][j]=0
                        cuadrosL2=cuadrosCompletos(board)
                        if (cuadrosL2-cuadrosL1==1):
                            board[i][j]=1*-1*posicionCorrecta
                        if (cuadrosL2-cuadrosL1==2):
                            board[i][j]=2*-1*posicionCorrecta
                        best = min(best,miniMax(board,depth+1,True,player_turn_id))
                        board[i][j]=99
            return best




def findBestMove (board,player_turn_id):
    bestVal = -90000000000
    bestMoveLocation = -1
    bestMovePosition = -1

    if (player_turn_id==1):
        posicionCorrecta=1
    if (player_turn_id==2):
        posicionCorrecta=-1

    cuadrosL1=cuadrosCompletos(board)

    for i in range (len(board)):
        for j in range (len(board[0])):
            if (board[i][j]==99):
                board[i][j]=0
                cuadrosL2=cuadrosCompletos(board)
                if (cuadrosL2-cuadrosL1==1):
                    board[i][j]=1*posicionCorrecta
                if (cuadrosL2-cuadrosL1==2):
                    board[i][j]=2*posicionCorrecta
                moveVal = (miniMax(board, 0, False, player_turn_id))

                board[i][j]=99

                if (moveVal>=bestVal):
                    bestMoveLocation = i
                    bestMovePosition = j
                    bestVal=moveVal
             
    print(bestMoveLocation,bestMovePosition)                    
    return[bestMoveLocation,bestMovePosition]
    #dreturn [random.randint(0,1), random.randint(0,29)]
    





#verificamos si el el movimiento esta disponible.   
def isMoveLeft (board):
    pisiblesJugadas=0
    for i in range (len(board)):
        for j in range (len(board[0])):
            if (board[i][j]==99):
                pisiblesJugadas=pisiblesJugadas+1
    
    if (pisiblesJugadas >0):
        return True
    if (pisiblesJugadas==0):
        return False

    



#funcion para evaluar el tablero final.
def evaluate(board,player_turn_id):

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


def cuadrosCompletos(board):
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
    
    return contadorPuntos