#Fernando Hengstenberg
 
#importamos las librerias
import socketio
from functions import findBestMove

#data

#url host
host= "http://localhost:4000"
#host=input("Inserte el host\n")

#pedimos el id del torneo
tournament_id=12
#tournament_id=input("Inserte el ID del torneo\n")

#pedimos el usuario
username=input("Inserte su ID\n")



#sockets of server
socket = socketio.Client()
#connect server
@socket.on("connect")
def on_connect():
    socket.emit("signin",
        {
            "user_name": username,
            "tournament_id": tournament_id,
            "user_role": "player"
        } 
    )

#play movement
@socket.on("ready")
def on_ready(data):
    print (data["board"])
   
    #print (data["board"])
    #get data
    #turn
    #Gameid
    socket.emit("play",
    {
        "tournament_id": tournament_id,
        "game_id" : data["game_id"],
        "player_turn_id": data["player_turn_id"],
        #random movement
        "movement": findBestMove(data["board"],data["player_turn_id"])
        
       }
    ) 
#game finish and readty for play
@socket.on("finish")
def finish(data):    
    
    socket.emit("player_ready",
    {
        "tournament_id": tournament_id,
        "game_id": data["game_id"],
        "player_turn_id": data["player_turn_id"]
    }
    )


#conectamos al host
socket.connect(host)