from Flota import Flota
class Buque_3(Flota):
    """Clase hija de la clase Flota encargada de crear los Buques de 3 Posiciones

        Posee 3 parametros:
        pos_x: Posicion x del buque dentro de la matriz field definida por un numero aleatorio en la funcion Creacion_barcos()
        pos_y: Posicion y del buque dentro de la matriz field definida por un numero aleatorio en la funciuon Creacion_barcos()
        orientacion: variable encargada de la orientacion del barco dentro de la amtriz, definida por un numero aleatorio en la funcion Creacion_barcos()
    
    """
    def __init__(self,pos_x,pos_y,orientacion):
        self.orientacion = orientacion
        super().__init__(pos_x,pos_y)
    
    def Posicion(self,field):
        """Funcion encargada del posicionamiento del Buque de 3 posiciones dentro de la matriz field

            Recibe la matriz field

            La funcion chequea los distintos constructores de la clase Buque_3 y posiciona al barco dependiendo de los numeros aleatorios rand_x y rand_y y la orientacion del 
            barco, luego dentro de la matriz al agregar el punto donde se ubica el barco agrega "B" 2 posiciones hacia abajo si y = 0, si y = 9 agrega "B" dos posiciones hacia arriba.
            Si x = 0, agrega "B" dos posiciones a la derecha y si x = 9, agrega "B" 2 posiciones hacia la izquierda.

            Retorna la matriz field con el buque de 3 posiciones ya colocado
        
        """
        rand_y = self.pos_y
        rand_x = self.pos_x
        orientacion = self.orientacion
        for y in range(len(field)):
            for x in range(len(field[y])):
                if orientacion == "Vertical":
                    if y == rand_y and x == rand_x:
                        field[y][x] = "B"
                        if y == 0:
                            field[1][x] = "B"
                            field[2][x] = "B"
                        elif y == 9:
                            field[8][x] = "B"
                            field[7][x] = "B"
                        else:
                            field[y+1][x] = "B"
                            field[y-1][x] = "B"
                elif orientacion == "Horizontal":
                    if y == rand_y and x == rand_x:
                        field[y][x] = "B"
                        if x == 0:
                            field[y][1] = "B"
                            field[y][2] = "B"
                        elif x == 9:
                            field[y][8] = "B"
                            field[y][7] = "B"
                        else:
                            field[y][x-1] = "B"
                            field[y][x+1] = "B"
        return field
    
    def Accion(self):
        return "Aterrizando Helicopteros"