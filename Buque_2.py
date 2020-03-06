from Flota import Flota
import random
class Buque_2(Flota):
    def __init__(self,pos_x,pos_y,orientacion):
        self.orientacion = orientacion
        super().__init__(pos_x,pos_y)

    def Posicion(self,field):
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
                            elif y == 0:
                                if field[y][x-1] != "B" and field[y+1][x-1] != "B" and field[y][x+1] != "B" and field[y+1][x+1] != "B" and field[y+2][x] != "B" and field[y+1][x] != "B":
                                    field[y][x] = "B"
                                    field[y+1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 9:
                                if field[y][x-1] != "B" and field[y-1][x-1] != "B" and field[y][x+1] != "B" and field[y-1][x+1] != "B" and field[y-2][x] != "B" and field[y-1][x] != "B":
                                    field[y][x] = "B"
                                    field[y-1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif x == 0:
                                if field[y-1][x] != "B" and field[y][x+1] != "B" and field[y+1][x+1] != "B" and field[y+2][x] != "B" and field[y+1][x] != "B":
                                    field[y][x] = "B"
                                    field[y+1][x] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif x == 9:
                                if field[y-1][x] != "B" and field[y][x-1] != "B" and field[y+1][x-1] != "B" and field[y+2][x] != "B" and field[y+1][x] != "B":
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
                            elif y == 0:
                                if field[y][x-1] != "B" and field[y+1][x] != "B" and field[y+1][x+1] != "B" and field[y][x+2] != "B" and field[y][x+1] != "B":
                                    field[y][x] = "B"
                                    field[y][x+1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif y == 9:
                                if field[y][x-1] != "B" and field[y-1][x] != "B" and field[y-1][x+1] != "B" and field[y][x+2] != "B" and field[y][x+1] != "B":
                                    field[y][x] = "B"
                                    field[y][x+1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif x == 0:
                                if field[y-1][x] != "B" and field[y-1][x+1] != "B" and field[y+1][x] != "B" and field[y+1][x+1] != "B" and field[y][x+2] != "B" and field[y][x+1] != "B":
                                    field[y][x] = "B"
                                    field[y][x+1] = "B"
                                    aux = False
                                else:
                                    rand_y = random.randrange(10)
                                    rand_x = random.randrange(10)
                            elif x == 9:
                                if field[y-1][x-1] != "B" and field[y-1][x] != "B" and field[y][x-2] != "B" and field[y+1][x-1] != "B" and field[y+1][x] != "B" and field[y][x-1] != "B":
                                    field[y][x] = "B"
                                    field[y][x-1] = "B"
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