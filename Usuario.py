class Usuario:
    """Clase encargada de la creacion de los objetos de tipo Usuario

        Posee 5 constructores que estan definidos en la funcion Datos():
        username: variable definida por el nombre de usuario del jugador
        nombre: variable definida por el nombre completo del jugador
        edad: variable definida por la edad del jugador
        genero: variable definida por el genero del jugador
        puntos: variable definida por los puntos del jugador, al principio es igual a 0 pero cambia a medida se desarrolla el juego

    """
    def __init__(self,username,nombre,edad,genero,puntos,shots):
        self.username = username
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.puntos = puntos
        self.shots = shots

    def Mensaje(self,shots):
        """ Funcion encargada de desplegar los dintintos mensajes dependiendo del numero de tiros empleados para hundir la flota

            Recibe como parametro la variable shots de la funcion main()

            Esta funcion chequea si el numero de tiros esta en uno de los rangos desplegados en la funcion y retorna un mensaje al jugador dependiendo de
            la cantidad de tiros empleados para hundir la flota.
        
        """
        if shots == 9:
            return "¿Eres un Robot? lo que acabas de hacer es poco probable …"
        elif shots > 9 and shots <= 45:
            return "Excelente Estrategia"
        elif shots > 45 and shots <= 70:
            return "Buena Estrategia; pero hay que mejorar"
        elif shots > 70 and shots <= 100:
            return "Considérese Perdedor, tiene que mejorar notablemente"
    def Write(self,puntos,shots):
        """ Funcion encargada de escribir los datos del jugador dentro del archivo "Data.txt"

            Recibe como parametro los puntos del jugador para cambiarlos en el constructor

            La funcion escribe en el archivo los datos del Usuario para llevar un registro de las personas que han jugado Battleship
        
        """
        self.puntos = puntos
        self.shots = shots
        datos = []
        datos.append(self.username)
        datos.append(self.nombre)
        datos.append(str(self.edad))
        datos.append(self.genero)
        datos.append(str(self.puntos))
        datos.append(str(shots))
        with open("Data.txt","a") as data:
            data.write(str(datos) + "\n")
            

