import random
from Usuario import Usuario
from Flota import Flota
from Buque_3 import Buque_3
from Buque_2 import Buque_2
from Submarino import Submarino
def Datos(username):
    """ Funcion encargada de recopilar todos los datos del usuario para luegos enviarlos a la clase Usuario.

        Recibe la variable username 

        Parametros:
        nombre: variable del nombre completo del usuario
        edad: variable de la edad del usuario
        genero: variable de genero del usuario
        puntos: variable de puntos siempre igual a 0 al iniciar el juego

        La funcion crea un objeto de la clase usuario con todos estos parametros y luego lo retorna
    """
    aux = True
    while aux == True:
        nombre = input("Introduzca su Nombre Completo: ").lower()
        name = list(nombre)
        if nombre == " ":
            print("Ingrese un nombre valido")
        elif nombre.isdecimal():
            print("Ingrese un nombre valido")
        else:
            aux2 = True
            i = 0
            while aux2 == True:
                if i == len(name):
                    aux2 = False
                    aux = False
                elif name[i].isdecimal():
                    print("Ingrese un nombre valido")
                    aux2 = False
                else:
                    i += 1
                
    aux = True
    while aux == True:
        edad = input("Introduzca su edad: ")
        if edad.isdecimal():
            edad = int(edad)
            if edad >= 1:
                aux = False
            else:
                print("Ingrese una edad valida")    
        else:
            print("Introduzca una edad valida")
    while True:
        genero = input("Introduzca (m) para Masculino o (f) para Femenino: ").lower()
        if genero == "m":
            genero = "Masculino"
            break
        elif genero == "f":
            genero = "Femenino"
            break
        else:
            print("Introduzca una opcion valida")
    
    puntos = 0
    shots = 0
    user = Usuario(username,nombre,edad,genero,puntos,shots)
    return user

def Creacion_barcos(field):
    """ Funcion encargada de la creacion del barco de 3 posiciones, el barco de 2 posiciones y de los 4 submarinos ademas de sus respectivos posicionamientos en el tablero de juego

        Recibe la variable field que es la matriz utilizada como tablero de juego

        Parametros:
        buque3: variable del tipo Buque_3 que recibe como parametros 3 variables aleatorias (orientacion,pos_x,pos_y) para luego crear un objeto de la clase Buque_3 y luego posicionarlo
        buque2: variable del tipo Buque_2 que recibe como parametros 3 variables aleatorias para luego crear un objeto de l aclase Buque_2 y posicionarlo
        submarinos: 4 variables del tipo Submarino que reciben como parametro 2 variables aleatorias (s_x,s_y) para luego crear 4 objetos de la clase Submarino

        Cada una de las variables utiliza la funcion Posicion() de su respectiva clase para posicionar los barcos dentro de la matriz

        Retorna la matriz field con los barcos posicionados en ella identificados con "B"
    
    """
    #Creacion de un Buque de 3 Posiciones
    rand = random.randrange(2)
    if rand == 0:
        orientacion = "Vertical"
    elif rand == 1:
        orientacion = "Horizontal"
    rand_y = random.randrange(10)
    rand_x = random.randrange(10)
    buque3 = Buque_3(rand_x,rand_y,orientacion)
    buque3.Posicion(field)

    #Creacion de un Buque de 2 Posiciones
    rand2 = random.randrange(2)
    if rand2 == 0:
         orientacion2 = "Vertical"
    elif rand2 == 1:
        orientacion2 = "Horizontal"
    rand_y = random.randrange(10)
    rand_x = random.randrange(10)
    buque2 = Buque_2(rand_x,rand_y,orientacion2)
    buque2.Posicion(field)

    #Creacion de los submarinos
    s1_y = random.randrange(10)
    s1_x = random.randrange(10)
    sub1 = Submarino(s1_x,s1_y)
    sub1.Posicion(field)

    s2_y = random.randrange(10)
    s2_x = random.randrange(10)
    sub2 = Submarino(s2_x,s2_y)
    sub2.Posicion(field)

    s3_y = random.randrange(10)
    s3_x = random.randrange(10)
    sub3 = Submarino(s3_x,s3_y)
    sub3.Posicion(field)

    s4_y = random.randrange(10)
    s4_x = random.randrange(10)
    sub4 = Submarino(s4_x,s4_y)
    sub4.Posicion(field)

    return field
    

def Game(field):
    """ Funcion encargada del juego de Battleship

        Recibe como parametros la matriz field con los barcos ya posicionados en ella

        Parametros:
        pos_x: El usuario seleciona una posicion x entre el 0 y el 9 que corresponden a las distintas posiciones horizontales dentro de la matriz
        pos_y: El usuario selecciona una posicion y entre el 0 y el 9 que cooresponden a las posiciones verticales dentro de la matriz

        El programa luego recorre la matriz, si la posicion xy introducida cooresponde a una "B" la iguala a "F" y la funcion retorna "Hit",
        si esta posicion no es igual a "B" la iguala a "X" y retorna "Miss". Por otro lado, si esta posicion es igual a "F" o "X", la funncion retorna 
        un mensaje de que el tiro ya fue realizado

    """
    aux = True
    x = False
    y = False
    while aux == True:
        pos_x = input("Introduzca un numero del 0 al 9 para la coordenada X: ")
        if pos_x.isdecimal():
            pos_x = int(pos_x)
            if pos_x < 0 and pos_x > 9:
                print("Introduzca una coordenada valida")
            else:
                x = True
        else:
            print("Introduzca una coordenada valida")
        pos_y = input("Introduzca un numero del 0 al 9 para la coordenada Y:")
        if pos_y.isdecimal():
            pos_y = int(pos_y)
            if pos_y < 0 and pos_y > 9:
                print("Introduzca una coordenada valida")
            else:
                y = True
        else:
            print("Introduzca una coordenada valida")
        if x == True and y == True:
            aux = False
    for y in range(len(field)):
        for x in range(len(field[y])):
            if y == pos_y and x == pos_x and field[y][x] != "B" and field[y][x] != "X" and field[y][x] != "F":
                field[y][x] = "X"
                return "Miss"
            elif y == pos_y and x == pos_x and field[y][x] == "B":
                field[y][x] = "F"
                return "Hit"
            elif y == pos_y and x == pos_x and field[y][x] == "X":
                return "Tiro Realizado intente de nuevo"
            elif y == pos_y and x == pos_x and field[y][x] == "F":
                return "Tiro Realizado intente de nuevo"
def Leaderboard():
    """ Funcion encargada de escribir los datos del top 10 en su respectivo archivo txt

        La funcion se encarga de leer el archivo Data.txt y crea una lista con el nombre de usuario del jugador,sus puntos y el numero
        de disparos. Luego, esa lista la ordena de mayor a menor dependiendo de los puntos del jugador y crea una nueva lista llamada top10
        la cual toma los primeros 10 jugadores de la lista ordenada y los guarda en esta nueva lista. Finalmente, toma la lista top10 y escribe
        sus datos en el archivo Leaderboard.txt.

        La funcion no retorna nada y es llamada desde el main
    """
    leaderboard = []
    users = []
    top10 = []
    with open("Data.txt","r") as data:
        for user in data:
            users.append(user.split(","))
        for i in range(len(users)):
            leader = []
            users[i][4] = int(users[i][4])
            users[i][5] = users[i][5].strip()
            leader.append(users[i][4])
            leader.append(int(users[i][5]))
            leader.append(users[i][0])
            leaderboard.append(leader)

    s_leader = sorted(leaderboard)
    s_leader.reverse()
    aux = True
    i = 0
    while aux == True:
        if len(s_leader) < 9:
            if i == len(s_leader):
                aux = False
            else:
                top10.append(s_leader[i])
                i += 1
        elif len(s_leader) >= 9:
            if i == 9:
                aux = False
            else:
                top10.append(s_leader[i])
                i += 1
    with open("Leaderboard.txt","w") as leader:
        for i in range(len(top10)):
            leader.write(top10[i][2] + "/")
            leader.write(str(top10[i][0]) + "/")
            leader.write(str(top10[i][1]) + "\n")

def Top10():
    """ Funcion encargada de imprimir el Top 10 al principio de cada partida

        La funcion se encarga de leer el archivo Leaderboard.txt y luego imprime cad uno de sus jugadores con sus puntajes y 
        sus disparos al inicio del juego.

        la funcion no retorna nada solo imprime 
    
    """
    with open("Leaderboard.txt","r") as leader:
        print("---Top 10---")
        for player in leader:
            player = player.strip()
            print(player)
        
def main():
    """  Funcion encargada de correr todo el programa

        La funcion primero llama a Top 10 para imprimir los 10 mejores jugadores con sus puntajes, luego se encarga de pedir el nombre de 
        usuario al jugador y llama a la funcion Datos para pedir los respectivos datos del jugador. Luego de recibir todos los datos, procede a 
        iniciar el juego llamando a la funcion Creacion_barcos y utiliza un ciclo while para dar inicio al juego. Dentro de este ciclo, se llama
        a la funcion Game y esta dependiendo si retorna "Hit","Miss" o "Tiro repetido", la funcion main suma o resta puntos y enel caso de
        tiro repetido suma al contador de tiros repetidos ademas de sumar al contador de tiros. Una vez el jugador le ha dado a todos los barcos,
        el juego finaliza y se hace llamado a los metodos de usuario Mensaje, Write y Estadisticas para que cada uno haga su funcion y tambien se 
        llama a la funcion Leaderboard para chequear si el usuario entra en el top 10 de los jugadores. Finalmente, se muestra un resumen de los
        datos de la partida y el mapa con las posiciones de los barcos ya hundidos, las posiciones falladas y las posiciones que el jugador no
        golpeo. Al finalizar se le pregunta al jugador si desea volver a jugar, en caso afirmativo inicia el juego nuevamente y en caso negativo
        se agradece al jugador por participar en el juego.

    """
    game = True
    while game == True:
        Top10()
        print("Bienvenido a Battleship")
        player = []
        aux = True
        while aux == True:
            username = input("Introduzca su nombre de usuario: ").lower()
            usuario = list(username)
            if len(username) > 30:
                print("Introduzca un username mas corto")
            else:
                aux2 = True
                i = 0
                while aux2 == True:
                    if i == len(usuario):
                        aux2 = False
                        aux = False
                    elif usuario[i] == " ":
                        print("Introduzca un username mas corto")
                        aux2 = False
                    else:
                        i += 1

        us = Datos(username)
        player.append(us)
        aux = True
        while aux == True:
            opcion = input("Desea introducir un cheat: (1) Si, (2) No: ")
            if opcion == "1":
                aux1 = True
                while aux1 == True:
                    clave = input("Introduzca el cheat: ")
                    if clave == "correccion":
                        print("Radar Activado")
                        aux1 = False
                        aux = False
                    else:
                        print("Introduzca un cheat valido")
            elif opcion == "2":
                clave = "none"
                aux = False
            else:
                print("Introduzca una opcion valida")

            
        field = [["■","■","■","■","■","■","■","■","■","■"],
                 ["■","■","■","■","■","■","■","■","■","■"],
                 ["■","■","■","■","■","■","■","■","■","■"],
                 ["■","■","■","■","■","■","■","■","■","■"],
                 ["■","■","■","■","■","■","■","■","■","■"],
                 ["■","■","■","■","■","■","■","■","■","■"],
                 ["■","■","■","■","■","■","■","■","■","■"],
                 ["■","■","■","■","■","■","■","■","■","■"],
                 ["■","■","■","■","■","■","■","■","■","■"],
                 ["■","■","■","■","■","■","■","■","■","■"]]
          
        creacion = Creacion_barcos(field)
        if clave == "correccion":
            for i in range(len(creacion)):
                print(creacion[i])
        elif clave == "none":
            print("Buena Suerte")
        aux2 = True
        shots = 0
        puntos = 0
        repetido = 0
        while aux2 == True:
            juego = Game(field)
            if clave == "correccion":
                for i in range(len(creacion)):
                    print(creacion[i])
            elif clave == "none":
                print(".")
            if juego == "Hit":
                shots += 1
                puntos += 10
            elif juego == "Miss":
                shots += 1
                puntos -= 2
            elif juego == "Tiro Realizado intente de nuevo":
                repetido += 1
            boat = True
            x = 0
            y = 0
            while boat == True:
                if field[y][x] == "B":
                    boat = False
                elif x == 9 and y == 9:
                    aux2 = False
                    boat = False
                elif x == 9:
                    x = 0
                    y += 1
                else:
                    x += 1
            print(juego)
        for y in range(len(field)):
            for x in range(len(field[y])):
                if field[y][x] != "F" and field[y][x] != "X":
                    field[y][x] = "O"
    
        for user in player:
            print(user.Mensaje(shots))
            user.Write(puntos,shots)
        print("""
            ------ Resumen de Juego ------
            Username : {}
            Disparos: {}
            Puntaje: {}
            Disparos Repetidos: {}
                """.format(username,shots,puntos,repetido))
        for i in range(len(creacion)):
            print(creacion[i])
        for user in player:
            print(user.Estadisticas())
        Leaderboard()
        aux3 = True
        while aux3 == True:
            opcion = input("Desea volver a jugar: (1) Si , (2) No: ")
            if opcion == "2":
                print("Gracias por jugar")
                aux3 = False
                game = False
            elif opcion == "1":
                aux3 = False
            else:
                print("Introduzca 1 o 2")

main()
