from Flota import Flota
import random
class Buque_2(Flota):
    """Clase hija de la clase Flota encargada de la creacion de los Buques de 2 posicones

        Posee 3 constructores:
        pos_x: Posicion x del barco dentro de la matriz field, definida por un numero aleatorio en la funcion Creacion_barcos()
        pos_y: Posicon y del barco dentro de la amtriz field, definida por un numero aleatorio en la funcion Creacion_barcos()
        orientacion: variable encargada de la orientacion del Buque dentro de la matriz, definida por un string en la funcion Creacion_barcos()
    
    """
    def __init__(self,pos_x,pos_y,orientacion):
        self.orientacion = orientacion
        super().__init__(pos_x,pos_y)

    def Posicion(self,field):
        """Funcion encargada del posicionamiento del Buque de 2 posicones dentro de la amtriz field

            Recibe como parametro la matriz field

            Esta funcion chequea los distintos constructores del Buque de 2 posiciones y luego recorre la matriz field.
            Una vez entra en esta funcion, esta cheque si la posicion xy definida por el constructor no coorresponde a un barco ya colocado, de ser asi, esta cambia los
            numeros aleatorios por 2 nuevos para chequear de nuevo, en cambio, si la posiicon xy esta disponible, esta chequea 9 posibilidades si la orientacion es vertical y
            9 posibilidades si la oriencacion es horizontal. Estas posibilidades estan definidas para que alrededor del Buque de 2 posiciones no se encuentre otro barco. De caso contrario,
            esta cambia las posiones xy por nuevos numeros aleatorios para las posiciones x e y.

            Una vez se han encontrado una posicion para el buque de 2 posiciones sin ninguna "B" al rededor, el barco es posicionado dentro de la matriz con una posicion mas hacia arriba o hacia abajo
            dependiendo si y = 0 o y = 9 o una posicion mas hacia la izquierda o hacia la derecha si x = 0 o x = 9

            La funcion retorna la matriz field con el buque de 2 posiciones ya en su lugar.
        
        """
        rand_y = self.pos_y
        rand_x = self.pos_x
        orientacion2 = self.orientacion
        aux = True
        while aux == True:
            for y in range(len(field)):
                for x in range(len(field[y])):
                    if orientacion2 == "Vertical":
                        if y == rand_y and x == rand_x and field[y][x] == "B":
                            rand_y = random.randrange(10)
                            rand_x = random.randrange(10)
                        elif y == rand_y and x == rand_x and field[y][x] != "B":
                            if y == 0 and x == 0:
                                if field[y][x+1] != "B" and field[y+1][x+1] != "B" and field[y+1][x] != "B" and field[y+2][x] != "B":
                                    field[y][x] = "B"
                                    field[y+1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 0 and x == 9:
                                if field[y][x-1] != "B" and field[y+1][x-1] != "B" and field[y+1][x] != "B" and field[y+2][x] != "B":
                                    field[y][x] = "B"
                                    field[y+1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 9 and x == 0:
                                if field[y-2][x] != "B" and field[y-1][x+1] != "B" and field[y][x+1] != "B" and field[y-1][x] != "B":
                                    field[y][x] = "B"
                                    field[y-1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 9 and x == 9:
                                if field[y-2][x] != "B" and field[y-1][x-1] != "B" and field[y][x-1] != "B" and field[y-1][x] != "B":
                                    field[y][x] = "B"
                                    field[y-1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 0 and x != 9 and x != 0:
                                if field[y][x-1] != "B" and field[y+1][x-1] != "B" and field[y][x+1] != "B" and field[y+1][x+1] != "B" and field[y+2][x] != "B" and field[y+1][x] != "B":
                                    field[y][x] = "B"
                                    field[y+1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 9 and x != 9 and x != 0:
                                if field[y][x-1] != "B" and field[y-1][x-1] != "B" and field[y][x+1] != "B" and field[y-1][x+1] != "B" and field[y-2][x] != "B" and field[y-1][x] != "B":
                                    field[y][x] = "B"
                                    field[y-1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif x == 0 and y != 9 and y != 0:
                                if field[y-1][x] != "B" and field[y][x+1] != "B" and field[y+1][x+1] != "B" and field[y+2][x] != "B" and field[y+1][x] != "B":
                                    field[y][x] = "B"
                                    field[y+1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif x == 9:
                                if field[y-1][x] != "B" and field[y][x+1] != "B" and field[y+1][x+1] != "B" and field[y+2][x] != "B" and field[y+1][x] != "B":
                                    field[y][x] = "B"
                                    field[y+1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 8 and x != 9 and x != 0:
                                if field[y-1][x] != "B" and field[y][x-1] != "B" and field[y+1][x-1] != "B" and field[y+1][x] != "B" and field[y+1][x+1] != "B" and field[y][x+1] != "B":
                                    field[y][x] = "B"
                                    field[y+1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            else:
                                if field[y-1][x] != "B" and field[y][x-1] != "B" and field[y+1][x-1] != "B" and field[y+2][x] != "B" and field[y+1][x] != "B" and field[y+1][x+1] != "B" and field[y][x+1] != "B":
                                    field[y][x] = "B"
                                    field[y+1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)

                    elif orientacion2 == "Horizontal":
                        if y == rand_y and x == rand_x and field[y][x] == "B":
                            rand_y = random.randrange(10)
                            rand_x = random.randrange(10)
                        elif y == rand_y and x == rand_x and field[y][x] != "B":
                            if y == 0 and x == 0:
                                if field[y+1][x] != "B" and field[y+1][x+1] != "B" and field[y][x+2] != "B" and field[y][x+1] != "B":
                                    field[y][x] = "B"
                                    field[y][x+1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 0 and x == 9:
                                if field[y][x-2] != "B" and field[y+1][x-1] != "B" and field[y][x-1] != "B" and field[y+1][x] != "B":
                                    field[y][x] = "B"
                                    field[y][x-1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 9 and x == 0:
                                if field[y-1][x] != "B" and field[y-1][x+1] != "B" and field[y][x+2] != "B" and field[y][x+1] != "B":
                                    field[y][x] = "B"
                                    field[y][x+1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 9 and x == 9:
                                if field[y-1][x] != "B" and field[y-1][x-1] != "B" and field[y][x-2] != "B" and field[y][x-1] != "B":
                                    field[y][x] = "B"
                                    field[y][x-1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 0 and x != 9 and x != 0:
                                if field[y][x-1] != "B" and field[y+1][x] != "B" and field[y+1][x+1] != "B" and field[y][x+2] != "B" and field[y][x+1] != "B":
                                    field[y][x] = "B"
                                    field[y][x+1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 9 and x != 0 and x != 9:
                                if field[y][x-1] != "B" and field[y-1][x] != "B" and field[y-1][x+1] != "B" and field[y][x+2] != "B" and field[y][x+1] != "B":
                                    field[y][x] = "B"
                                    field[y][x+1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif x == 0 and y != 0 and y != 9:
                                if field[y-1][x] != "B" and field[y-1][x+1] != "B" and field[y+1][x] != "B" and field[y+1][x+1] != "B" and field[y][x+2] != "B" and field[y][x+1] != "B":
                                    field[y][x] = "B"
                                    field[y][x+1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif x == 9 and y != 0 and y != 9:
                                if field[y-1][x-1] != "B" and field[y-1][x] != "B" and field[y][x-2] != "B" and field[y+1][x-1] != "B" and field[y+1][x] != "B" and field[y][x-1] != "B":
                                    field[y][x] = "B"
                                    field[y][x-1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif x == 8 and y != 0 and y != 9:
                                if field[y-1][x] != "B" and field[y][x-1] != "B" and field[y+1][x] != "B" and field[y+1][x+1] != "B" and field[y][x+1] != "B":
                                    field[y][x] = "B"
                                    field[y][x+1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            else:
                                if field[y-1][x] != "B" and field[y-1][x+1] != "B" and field[y][x+2] != "B" and field[y][x-1] != "B" and field[y+1][x] != "B" and field[y+1][x+1] != "B" and field[y][x+1] != "B":
                                    field[y][x] = "B"
                                    field[y][x+1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                      
        return field
    def Accion(self):
        return "Comunicando con Tierra y Miembros de la flota"