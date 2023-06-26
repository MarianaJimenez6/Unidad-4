from claseObjectEncoder import ObjectEncoder

from vistaContactos import ContactsView
import json
from controladorContactos import ControladorContactos
import requests



if __name__ == "__main__":

    jsonFgeneros = ObjectEncoder()
    diccionario = jsonFgeneros.leerJSONArchivo('generos.json')
    listagenero = jsonFgeneros.decodificargeneros(diccionario)

    jsonF = ObjectEncoder()
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=5d05d8c832406f737ca16767ca765638'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json() 
    else:
        print('Error:', response.status_code)

    listapeli = jsonF.decodificarpeliculas(data,listagenero)
    #print(listapeli)
    vista = ContactsView()
    ctrl = ControladorContactos(listapeli, vista)
    vista.setControlador(ctrl)
    ctrl.start()