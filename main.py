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

def main():
    """  Funcion encargada de correr todo el programa

    """
    game = True
    while game == True:
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
        #Para efectos de correccion quitar los #
        for i in range(len(creacion)):
            print(creacion[i])
        aux2 = True
        hits = 9
        shots = 0
        puntos = 0
        repetido = 0
        while aux2 == True:
            juego = Game(field)
            for i in range(len(creacion)):
                print(creacion[i])
            if juego == "Hit":
                shots += 1
                hits -= 1
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
            #Para efectos de correccion quitar los #
            print(juego)
            print(hits)
        for y in range(len(field)):
            for x in range(len(field[y])):
                if field[y][x] != "F" and field[y][x] != "X":
                    field[y][x] = "O"
    
        for user in player:
            print(user.Mensaje(shots))
            user.Write(puntos,shots)
        print("""
            ------ Estadisticas ------
            Username : {}
            Disparos: {}
            Puntaje: {}
            Disparos Repetidos: {}
                """.format(username,shots,puntos,repetido))
        for i in range(len(creacion)):
            print(creacion[i])
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
