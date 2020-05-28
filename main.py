#Fernando Hengstenberg

#libreria
import socketio
import random
from funciones import miniMax
from funciones import contador
from funciones import findBestMove




#pedimos la direccion del host
host= "http://localhost:4000"
#host=input("Inserte el host\n")

#contador de juegos
gamesF = 0
gamesW = 0
gamesL = 0


#pedimos el id del torneo
tournament_id=12
#tournament_id=input("Inserte el ID del torneo\n")

#pedimos el usuario
username=input("Inserte su ID\n")


socket = socketio.Client()

@socket.on("connect")
def on_connect():
    #contador de juegos
    socket.emit("signin",
        {
            "user_name": username,
            "tournament_id": tournament_id,
            "user_role": "player"
        } 
    )


@socket.on("ready")
def on_ready(data):
    print(data["board"])
    
    #miniMax(data["player_turn_id"], data["game_id"],data["board"],data["movementNumber"])
    #print (data["board"])
    #obtener informacion y tablero.
    #turno
    #Gameid
    socket.emit("play",
    {
        "tournament_id": tournament_id,
        "game_id" : data["game_id"],
        "player_turn_id": data["player_turn_id"],
        #movimiento random
        "movement":  findBestMove(data["board"],data["player_turn_id"])
        
       }
    ) 
@socket.on("finish")
def finish(data):
    

    #evaluate(data["board"],data["player_turn_id"])
    if (data["player_turn_id"] == data["winner_turn_id"]):
        contador(1,0)

    if (data["player_turn_id"] != data["winner_turn_id"]):
        contador(0,1)
        
    
    socket.emit("player_ready",
    {
        "tournament_id": tournament_id,
        "game_id": data["game_id"],
        "player_turn_id": data["player_turn_id"]
    }
    )


"""    
@socket.on("fin")
def fin(data): 
    ejemplo()
    #Fernando Hengstenberg
    #recibimos la informacion.
    #gameid
    #turno del jugador
    #winer-id
    #board
    #limpiar variables
	socket.emit("player_ready",
    {
        	"tournament_id":tournament_id,
        	"game_id":data["game_id"],
        	"player_turn_id":data["player_turn_id"]
    }
    )
"""




#conectamos al host
socket.connect(host)