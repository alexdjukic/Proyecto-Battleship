from Flota import Flota
import random
class Submarino(Flota):
    """ Clase hija de la clase Flota encargada de la creacion de los objetos de tipo Submarino

        Posee 2 constructores:
        pos_x: posicion x del submarino dentro de la matriz, definida por un numero aleatorio en la funcion Creacion_barcos()
        pos_y: posicion y del submarino dentro de la matriz, definida por un numero aleatorio en la funcion Creacion_barcos()
    
    """
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
    
    def Posicion(self,field):
        """Funcion encargada del posicionamiento del submarino dentro de la matriz

            Recibe como parametro la matriz field

            La funcion utiliza los constructores del objeto de tipo Submarino y recorre la matriz field hasta encontrar la posicion xy igual a las variables s_x y s_y.
            Al encontrarla, chequea si esta posicion es distinta de "B", de caso contrario cambia s_x y s_y por 2 numeros aleatorios nuevos.
            Si la posicion esta disponible, la funcion chquea las posiciones al rededor de la posion xy, si no hay ninguna "B" alrededor de la posicion xy se posiciona el submarino en
            dicha posicion. En caso contrario, se cambian s_x y s_y por 2 numero aleatorios.

            Una vez se encuentra una posicion adecuada para el submarino, la funcion retorna la matriz field con el submarino posicionado.
        
        """
        s_y = self.pos_y
        s_x = self.pos_x
        aux = True
        while aux == True:
            for y in range(len(field)):
                for x in range(len(field[y])):
                    if y == s_y and x == s_x and field[y][x] == "B":
                        s_y = random.randrange(10)
                        s_x = random.randrange(10)

                    elif y == s_y and x == s_x and field[y][x] != "B":
                        if y == 0 and x == 0:
                            if field[y][x+1] != "B" and field[y+1][x] != "B":
                                field[y][x] = "B"
                                aux = False
                            else:
                                s_y = random.randrange(10)
                                s_x = random.randrange(10)
                        elif y == 0 and x == 9:
                            if field[y][x-1] != "B" and field[y+1][x] != "B":
                                field[y][x] == "B"
                                aux = False
                            else:
                                s_y = random.randrange(10)
                                s_x = random.randrange(10)
                        elif y == 9 and x == 9:
                            if field[y][x-1] != "B" and field[y-1][x] != "B":
                                field[y][x] = "B"
                                aux = False
                            else:
                                s_y = random.randrange(10)
                                s_x = random.randrange(10)
                        elif y == 9 and x == 0:
                            if field[y-1][x] != "B" and field[y][x+1] != "B":
                                field[y][x] = "B"
                                aux = False
                            else:
                                s_y = random.randrange(10)
                                s_x = random.randrange(10)
                        elif y == 0:
                            if field[y][x-1] != "B" and field[y][x+1] != "B" and field[y+1][x] != "B":
                                field[y][x] == "B"
                                aux = False
                            else:
                                s_y = random.randrange(10)
                                s_x = random.randrange(10)
                        elif y == 9:
                            if field[y][x-1] != "B" and field[y-1][x] != "B" and field[y][x+1] != "B":
                                field[y][x] = "B"
                                aux = False
                            else:
                                s_y = random.randrange(10)
                                s_x = random.randrange(10)
                        elif x == 0:
                            if field[y-1][x] != "B" and field[y][x+1] != "B" and field[y+1][x] != "B":
                                field[y][x] = "B"
                                aux = False
                            else:
                                s_y = random.randrange(10)
                                s_x = random.randrange(10)
                        elif x == 9:
                            if field[y-1][x] != "B" and field[y][x-1] != "B" and field[y+1][x] != "B":
                                field[y][x] = "B"
                                aux = False
                            else:
                                s_y = random.randrange(10)
                                s_x = random.randrange(10)
                        else:
                            if field[y-1][x] != "B" and field[y][x-1] != "B" and field[y+1][x] != "B" and field[y][x+1] != "B":
                                field[y][x] = "B"
                                aux = False
                            else:
                                s_y = random.randrange(10)
                                s_x = random.randrange(10)

                                
        return field
    
    def Accion(self):
        return "Descendiendo a las Profundidades"
        

