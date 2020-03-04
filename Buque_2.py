from Barcos import Barcos
import random
class Buque_2(Barcos):
    def __init__(self,pos_x,pos_y,vidas,orientacion):
        self.orientacion = orientacion
        super().__init__(pos_x,pos_y,vidas)

    def Posicion(self,field):
        rand_y = self.pos_y
        rand_x = self.pos_x
        orientacion2 = self.orientacion
        for y in range(len(field)):
            for x in range(len(field[y])):
                if orientacion2 == "Vertical":
                    if field[y][x] == "B":
                        rand_y = random.randrange(10)
                        rand_x = random.randrange(10)
                    elif y == rand_y and x == rand_x and field[y][x] != "B":
                        field[y][x] = "B"
                        if y == 0 and field[y+1][x] != "B" and field[y+2][x] != "BB":
                            field[1][x] = "B"
                        elif y == 9 and field[y-1][x] != "B":
                            field[8][x] = "B"
                        elif field[y+1][x] != "B":
                            field[y+1][x] = "B"
                if orientacion2 == "Horizontal":
                    if field[y][x] == "B":
                        rand_y = random.randrange(10)
                        rand_x = random.randrange(10)
                    elif y == rand_y and x == rand_x and field[y][x] != "B":
                        field[y][x] = "B"
                        if x == 0 and field[y][0] != "B":
                            field[y][1] = "B"
                        elif x == 9 and field[y][9] != "B":
                            field[y][9] = "B"   
                        elif field[y][8] != "B":
                            field[y][8] = "B" 
                                
        return field