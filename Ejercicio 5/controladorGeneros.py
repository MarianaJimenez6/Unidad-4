class ListaGeneros:
    __lista =[]

    def __init__(self):
        self.__lista = []

    def agregargenero(self, genero):
        self.__lista.append(genero)

    def __str__(self):
        s = ""
        for genero in self.__lista:
            s+=str(genero)+"\n"
        return s

    def reemplazargenero(self,generos):
        i = 0
        j=0
        while i<len(generos):
            bandera = False
            while j<len(self.__lista) and not bandera:
                if self.__lista[j].getid() == generos[i]:
                    generos[i] = self.__lista[j].getnombre()
                    bandera = True
                else:
                    j=j+1
            i+=1
            j=0
        return generos
