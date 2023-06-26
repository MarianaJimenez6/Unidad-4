import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

import requests
import json


class Aplicacion(tk.Tk):
    __dolar = None
    __pesos = None

    def __init__(self):
        super().__init__()  # o,n,e,s
        self.geometry('260x100')
        self.__dolar = tk.StringVar()
        self.__pesos = tk.StringVar()
        self.dolarventa = tk.StringVar()

        self['relief'] = 'sunken'

        #importar el contenido del sitio web
        res = requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
        dolar = res.text

        # Convertir la cadena JSON en un objeto Python
        dolar_objeto = json.loads(dolar)
        dicccioario = dolar_objeto[0]
        self.dolarventa = float((dicccioario['casa']['venta']).replace(",","."))
        self.__dolar.trace('w', self.calcular)

        self.dolarEntry = tk.Entry(width=10, textvariable=self.__dolar)
        self.dolarEntry.place(x=100, y=10)

        labelDolar = tk.Label(text="dólares")
        labelDolar.place(x=160, y=10)

        labelequivalente = tk.Label(text="es equivalente a")
        labelequivalente.place(x=0,y=30)

        tk.Label(textvariable=self.__pesos).place(x=100, y=30)

        labelpesos = tk.Label(text="pesos")
        labelpesos.place(x=160, y=30)

        botonsalir = tk.Button(text="Salir", width=10, command=self.destroy)
        botonsalir.place(x=160, y=60)
    def calcular(self,*args):
        if self.dolarEntry.get() != "":
            try:
                valor = float(self.dolarEntry.get().replace(",","."))
                self.__pesos.set("{:.2f}".format(valor*self.dolarventa))
            except ValueError:
                messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
        else:
            self.dolarEntry.set("")


if __name__ == '__main__':
    app = Aplicacion()
    app.mainloop()