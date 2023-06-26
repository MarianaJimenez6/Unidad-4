class ListaPeliculas:
    __lista =[]

    def __init__(self):
        self.__lista = []

    def agregarpelicula(self, pelicula):
        self.__lista.append(pelicula)

    def __str__(self):
        s = ""
        for pelicula in self.__lista:
            s+=str(pelicula)+"\n"
        return s

    def getlistapeliculas(self):
        return self.__lista