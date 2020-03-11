class Flota:
    """Clase Padre de los dintintos tipos de barcos dentro del juego

    Posee solo dos parametros que son la pos_x y la pos_y que son las definidas por los numeros aleatorios en la pagina principal del programa

    No posee ninguna funcion solo actua como clase padre para los demas Buques
"""
    def __init__(self,pos_x,pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y