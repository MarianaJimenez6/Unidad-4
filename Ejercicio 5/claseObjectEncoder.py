import json
from pathlib import Path

from controladorPeliculas import  listaPeliculas

from clasePelicula import Pelicula

from controladorGeneros import ListaGeneros

from claseGenero import Genero

class ObjectEncoder(object):
    def decodificarpeliculas(self, d,listagenero):
        resultados = d['results']
        lista_peliculas = listaPeliculas()

        for resultado in resultados:
            titulo = resultado['title']
            lenguaje = resultado['original_language']
            resumen = resultado['overview']
            fecha = resultado['release_date']
            gen = resultado['genre_ids']
            genero = listagenero.reemplazargenero(gen)
            pelicula = Pelicula(titulo, resumen, lenguaje, fecha, genero)
            lista_peliculas.agregarpelicula(pelicula)
        return lista_peliculas

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def decodificargeneros(self,d):
        resultados = d['genres']
        lista_genero = ListaGeneros()

        for resultado in resultados:
            id = resultado['id']
            nombre = resultado['name']
            genero = Genero(id,nombre)
            lista_genero.agregargenero(genero)
        return lista_genero