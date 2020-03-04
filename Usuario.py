class Usuario:
    def __init__(self,username,nombre,edad,genero,puntos):
        self.username = username
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.puntos = puntos

    def Mensaje(self,shots):
        if shots == 9:
            return "¿Eres un Robot? lo que acabas de hacer es poco probable …"
        elif shots > 9 and shots <= 45:
            return "Excelente Estrategia"
        elif shots > 45 and shots <= 70:
            return "Buena Estrategia; pero hay que mejorar"
        elif shots > 70 and shots <= 100:
            return "Considérese Perdedor, tiene que mejorar notablemente"
    

