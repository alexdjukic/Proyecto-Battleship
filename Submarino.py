from Flota import Flota
import random
class Submarino(Flota):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
    
    def Posicion(self,field):
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
        

