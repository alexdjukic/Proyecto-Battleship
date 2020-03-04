from Barcos import Barcos
class Buque_3(Barcos):
    def __init__(self,pos_x,pos_y,vidas,orientacion):
        self.orientacion = orientacion
        super().__init__(pos_x,pos_y,vidas)
    
    def Posicion(self,field):
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
