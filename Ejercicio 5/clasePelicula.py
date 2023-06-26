class Pelicula:
    __titulo = ""
    __resumen = ""
    __lenguaje = ""
    __fecha = ""
    __generos = ""

    def __init__(self, titulo, resumen, lenguaje, fecha, generos):
        self.__titulo = titulo
        self.__resumen = resumen
        self.__lenguaje = lenguaje
        self.__fecha = fecha
        self.__generos = generos

    def get_titulo(self):
        return self.__titulo

    def get_resumen(self):
        return self.__resumen

    def get_lenguaje(self):
        return self.__lenguaje

    def get_fecha(self):
        return self.__fecha

    def get_generos(self):
        return self.__generos


    def __str__(self):
        return f"titulo:{self.__titulo} resumen:{self.__resumen} lenguaje:{self.__lenguaje} fecha:{self.__fecha} genero:{self.__generos}"