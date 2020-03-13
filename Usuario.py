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
        with open("Data.txt","a") as data:
            data.write(self.username + ",")
            data.write(self.nombre + ",")
            data.write(str(self.edad) + ",")
            data.write(self.genero + ",")
            data.write(str(self.puntos) + ",")
            data.write(str(self.shots) + "\n")

    def Estadisticas(self):
        """Funcion encargada del calculo de las estadisticas de todos los juegos previamente jugados

            Es la funcion encargada de calcular el promedio de las edades de los jugadores, los puntos de los jugadores masculinos y 
            femeninos y el promedio de disparos utilizados por los jugadores.

            Posee varias variables:
            prom_edad: variable encargada de definir en que rango de edades se encuentra la mayoria de los jugadores
            prom_puntosm: variable encargada de calcular el promedio de puntos de los jugadores Masculinos
            prom_puntosf: variable encargad del calculo del promedio de puntos de los jugadores femeninos
            prom_shots: variable encargada del calculo del promedio de tiros entre todos los juegos

            La funcion recorre el archivo Data.txt y pasa todo su contenido a la lista estadisticas. una vez ha hecho esto, la recorre cambiando
            los datos numericos de strings a ints y eliminando el \n del ultimo dato que es el numero de disparos. Luego entra en una serie de condicionales
            para la edad del los jugadores, sumando 1 a varios auxiliares presentes para definir el rango en el que la mayoria de los jugadores se encuentran.
            Mas tarde, procede a verificar si el jugador en la posicion i es de genero Masculino o Femenino, sumando sus puntos a la variable prom_puntosm o prom_puntosf
            respectivamente y finalmente divide las sumas por el numero de jugadores masculinos o femeninos. Al final se calcula el promedio de disparos entre todos
            los juegos con la variable prom_shots

            La funcion retorna un print en el cual se muestran las estadisticas de todos los juegos almacenados en Data.txt
        """
        estadisticas = []
        prom_edad = " "
        prom_puntosm = 0
        prom_puntosf = 0
        prom_shots = 0
        edad5 = 0
        edad19 = 0
        edad46 = 0
        edad61 = 0
        auxm = 0
        auxf = 0
        auxshots = 0
        with open("Data.txt","r") as data:
            for user in data:
             estadisticas.append(user.split(","))
            
            for i in range(len(estadisticas)):
                estadisticas[i][2] = int(estadisticas[i][2])
                estadisticas[i][4] = int(estadisticas[i][4])
                estadisticas[i][5] = int(estadisticas[i][5].strip())
                if estadisticas[i][2] >= 5 and estadisticas[i][2] <= 18:
                    edad5 += 1
                elif estadisticas[i][2] >= 19 and estadisticas[i][2] <= 45:
                    edad19 += 1
                elif estadisticas[i][2] >= 46 and estadisticas[i][2] <= 60:
                    edad46 += 1
                elif estadisticas[i][2] >= 61 and estadisticas[i][2] <= 100:
                    edad61 += 1
                if estadisticas[i][3] == "Masculino":
                    auxm += 1
                    prom_puntosm += estadisticas[i][4]

                elif estadisticas[i][3] == "Femenino":
                    auxf += 1
                    prom_puntosf += estadisticas[i][4]
                
                if estadisticas[i][5]:
                    auxshots += 1
                    prom_shots += int(estadisticas[i][5])

            if edad5 > edad19 and edad5 > edad46 and edad5 > edad61:
                    prom_edad = "5-18"
            elif edad19 > edad5 and edad19 > edad46 and edad19 > edad61:
                    prom_edad = "19-46"
            elif edad46 > edad5 and edad46 > edad19 and edad46 > edad61:
                    prom_edad = "46-60"
            elif edad61 > edad5 and edad61 > edad19 and edad61 > edad46:
                    prom_edad = "61-100"   
            

            prom_puntosm = prom_puntosm/auxm
            prom_puntosf = prom_puntosf/auxf
            prom_shots = prom_shots/auxshots
                

        return """      ------ Estadisticas ------
            Promedio de edad: {} años
            Promedio de Puntos Masculino: {} pts
            Promedio de puntos Femenino: {} pts
            Promedio de Disparos: {} disparos
        
        """.format(prom_edad,prom_puntosm,prom_puntosf,prom_shots)
            

