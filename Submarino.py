from Barcos import Barcos
import random
class Submarino(Barcos):
    def __init__(self,pos_x,pos_y,vidas):
        super().__init__(pos_x,pos_y,vidas)
    
    def Posicion(self,field):
        s_y = self.pos_y
        s_x = self.pos_x
        for y in range(len(field)):
            for x in range(len(field[y])):
                if y == s_y and x == s_x and field[y][x] == "B":
                    s_y = random.randrange(10)
                    s_x = random.randrange(10)
                elif y == s_y and x == s_x and field[y][x] != "B":
                    field[y][x] = "B"
                        

        return field
        

