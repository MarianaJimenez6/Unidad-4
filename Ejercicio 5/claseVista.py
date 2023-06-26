from tkinter import *
from tkinter import ttk, messagebox


class Vista(ttk.Frame):
    __ventana=None
    __lista = None
    def __init__(self, lista):
        self.__lista = lista
        self.__ventana = Tk()
        self.__ventana.geometry('450x250')
        self.__ventana.title('Listado de Peliculas themoviedb.org')
        mainframe = ttk.Frame(self.__ventana, padding="2 10 5 10")  # o,n,e,s
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 10
        mainframe['relief'] = 'sunken'