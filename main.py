import random
from Usuario import Usuario
from Barcos import Barcos
from Buque_3 import Buque_3
from Buque_2 import Buque_2
from Submarino import Submarino
def Datos():
    aux = True
    while aux == True:
        username = input("Introduzca su nombre de usuario: ").lower()
        user = list(username)
        if len(username) > 30:
            print("Introduzca un nombre de usuario mas corto")
        for i in range(len(user)):
            if user[i] == " ":
                print("Introduzca un nombre de usuario sin espacios")
                aux = True
                break 
        else:
            while True:
                nombre = input("Introduzca su Nombre Completo:").lower()
                if nombre == " ":
                    print("ingrese un nombre valido")
                else:
                    break

            edad = int(input("Introduzca su edad: "))
            genero = input("Introduzca su genero: ").lower()
            puntos = 0
            user = Usuario(username,nombre,edad,genero,puntos)
            aux = False
    return user

def Creacion_barcos(field):
    #Creacion de un Buque de 3 Posiciones
    rand = random.randrange(2)
    if rand == 0:
        orientacion = "Vertical"
    elif rand == 1:
        orientacion = "Horizontal"
    rand_y = random.randrange(10)
    rand_x = random.randrange(10)
    buque3 = Buque_3(rand_x,rand_y,3,orientacion)
    buque3.Posicion(field)

    #Creacion de un Buque de 2 Posiciones
    rand2 = random.randrange(2)
    if rand2 == 0:
         orientacion2 = "Vertical"
    elif rand2 == 1:
        orientacion2 = "Horizontal"
    rand_y = random.randrange(10)
    rand_x = random.randrange(10)
    buque2 = Buque_2(rand_x,rand_y,2,orientacion2)
    buque2.Posicion(field)

    #Creacion de los submarinos
    s1_y = random.randrange(10)
    s1_x = random.randrange(10)
    sub1 = Submarino(s1_x,s1_y,1)
    sub1.Posicion(field)

    s2_y = random.randrange(10)
    s2_x = random.randrange(10)
    sub2 = Submarino(s2_x,s2_y,1)
    sub2.Posicion(field)

    s3_y = random.randrange(10)
    s3_x = random.randrange(10)
    sub3 = Submarino(s3_x,s3_y,1)
    sub3.Posicion(field)

    s4_y = random.randrange(10)
    s4_x = random.randrange(10)
    sub4 = Submarino(s4_x,s4_y,1)
    sub4.Posicion(field)

    return field
    

def Game(field):
    aux = True
    while aux == True:
        pos_x = int(input("Introduzca un numero del 0 al 9 para la coordenada X: "))
        if pos_x < 0 and pos_x > 9:
            print("Introduzca una coordenada valida")
        pos_y = int(input("Introduzca un numero del 0 al 9 para la coordenada Y:"))
        if pos_y < 0 and pos_y > 9:
            print("Introduzca una coordenada valida")
        else:
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
    print("Bienvenido a Battleship")
    aux = True
    player = []
    while aux == True:
        opcion = input("Desea introducir sus datos: ").lower()
        if opcion == "si":
            user = Datos()
            player.append(user)
            aux = False
        elif opcion == "no":
            aux = False
        else:
            print("Introduzca una opcion valida")
            

    field = [["0","1","2","3","4","5","6","7","8","9"],
             ["0","1","2","3","4","5","6","7","8","9"],
             ["0","1","2","3","4","5","6","7","8","9"],
             ["0","1","2","3","4","5","6","7","8","9"],
             ["0","1","2","3","4","5","6","7","8","9"],
             ["0","1","2","3","4","5","6","7","8","9"],
             ["0","1","2","3","4","5","6","7","8","9"],
             ["0","1","2","3","4","5","6","7","8","9"],
             ["0","1","2","3","4","5","6","7","8","9"],
             ["0","1","2","3","4","5","6","7","8","9"]]
          
    creacion = Creacion_barcos(field)
    for i in range(len(creacion)):
            print(creacion[i])
    aux2 = True
    hits = 9
    shots = 0
    puntos = 0
    while aux2 == True:
        juego = Game(field)
        print(juego)
        for i in range(len(creacion)):
            print(creacion[i])
        if juego == "Hit":
            shots += 1
            hits -= 1
            puntos += 10
        elif juego == "Miss":
            shots += 1
            puntos -= 2
        if hits == 0:
            aux2 = False
        print(hits)
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] != "F" and field[y][x] != "X":
                field[y][x] = "O"
    for i in range(len(creacion)):
        print(creacion[i])
    for user in player:
        print(user.Mensaje(shots))
    print("Usted obtuvo {} Puntos".format(puntos))

main()