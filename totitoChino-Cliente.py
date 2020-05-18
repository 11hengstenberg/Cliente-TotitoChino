#Fernando Hengstenberg

#libreria
import socketio
import random


#pedimos la direccion del host
#host= "http://localhost:4000"
host=input("Inserte el host\n")

#pedimos el id del torneo
#tournament_id=12
tournament_id=input("Inserte el ID del torneo\n")

#pedimos el usuario
username=input("Inserte su ID\n")




socket = socketio.Client()

@socket.on("connect")
def on_connect():
    socket.emit("signin",
        {
            "user_name": username,
            "tournament_id": tournament_id,
            "user_role": "player"
        } 
    )

@socket.on("ready")
def on_ready(data):
    print (data["board"])
    #obtener informacion y tablero.
    #turno
    #Gameid
    socket.emit("play",
    {
        "tournament_id": tournament_id,
        "game_id" : data["game_id"],
        "player_turn_id": data["player_turn_id"],
        #movimiento random
        "movement": [random.randint(0,1),random.randint(0,29)]
        
       
    }) 

@socket.on('finish')
def finish(data): 
    #recibimos la informacion.
    #gameid
    #turno del jugador
    #winer-id
    #board
    #limpiar variables
	socket.emit('player_ready', 
		{
        	"tournament_id":tournament_id,
        	"game_id":data['game_id'],
        	"player_turn_id":data['player_turn_id']
        }
    )


#conectamos al host
socket.connect(host)