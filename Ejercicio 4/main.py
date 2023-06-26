# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 23:03:53 2020

@author: morte
"""
from tkinter import *
from tkinter import ttk
from functools import partial

import re


class Imaginario:
    def __init__(self, real, imag):
        self.real = int(real)
        self.imag = int(imag)

    def __add__(self, other):
        if isinstance(other, Imaginario):
            return Imaginario(self.real + other.real, self.imag + other.imag)
        else:
            raise ValueError("debe ser instancia de la clase Imaginario")

    def __sub__(self, other):
        if isinstance(other, Imaginario):
            return Imaginario(self.real - other.real, self.imag - other.imag)
        else:
            raise ValueError("debe ser instancia de la clase Imaginario")

    def __mul__(self, other):
        if isinstance(other, Imaginario):
            real = (self.real * other.real) - (self.imag * other.imag)
            imag = (self.real * other.imag) + (self.imag * other.real)
            return Imaginario(real, imag)
        else:
            raise ValueError("debe ser instancia de la clase Imaginario")

    def __truediv__(self, other):
        if isinstance(other, Imaginario):
            denominador = (other.real ** 2) + (other.imag ** 2)
            real = ((self.real * other.real) + (self.imag * other.imag)) / denominador
            imag = ((self.imag * other.real) - (self.real * other.imag)) / denominador
            return Imaginario(real, imag)
        else:
            raise ValueError("debe ser instancia de la clase Imaginario")


class Calculadora(object):
    __ventana = None
    __operador = None
    __panel = None
    __operadorAux = None
    __primerOperando = None
    __segundoOperando = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        self.__panel = StringVar()
        self.__operador = None
        self.__operadorAux = None
        self.__operador1 = StringVar()
        self.__operador2 = StringVar()
        self.__operacion = StringVar()

        self.operador1Entry = ttk.Entry(mainframe, width=5, textvariable=self.__operador1, justify='center')
        self.operador1Entry.grid(column=1, row=1, columnspan=1, sticky=(W, E))

        operacionEntry = ttk.Entry(mainframe, width=5, textvariable=self.__operacion, justify='center',state='disabled')
        operacionEntry.grid(column=2, row=1, sticky=(N))

        self.operador2Entry = ttk.Entry(mainframe, width=9, textvariable=self.__operador2)
        self.operador2Entry.grid(column=3, row=1, sticky=(W))

        ttk.Label(mainframe, text="re:").grid(column=4, row=1, sticky=(W))
        panelEntry = ttk.Entry(mainframe, width=9, textvariable=self.__panel, justify='right', state='disabled')
        panelEntry.grid(column=4, row=1, columnspan=1, sticky=(E))

        ttk.Button(mainframe, text='suma', command=lambda: self.asignar("+")).grid(column=1, row=2, sticky=W)
        ttk.Button(mainframe, text='resta', command=lambda: self.asignar("-")).grid(column=2, row=2, sticky=W)
        ttk.Button(mainframe, text='mul', command=lambda: self.asignar("*")).grid(column=3, row=2, sticky=W)
        ttk.Button(mainframe, text='div', command=lambda: self.asignar("/")).grid(column=4, row=2, sticky=W)

        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO, '2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO, '3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='i', command=partial(self.ponerNUMERO, 'i')).grid(column=4, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO, '4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO, '5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO, '6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO, '7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO, '8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO, '9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerNUMERO, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='=', command=lambda: self.operacion("=")).grid(column=4, row=6, sticky=W)
        ttk.Button(mainframe, text='AC', command=self.borrarPaneles).grid(column=3, row=6, sticky=W)

        self.__panel.set('0')
        self.operador1Entry.focus()
        self.__ventana.mainloop()
    def borrarPaneles(self):
        self.__panel.set('0')
        self.__operadorAux = None
        self.__primerOperando = None
        self.__segundoOperando = None
        self.__operador1.set("")
        self.__operador2.set("")
    def asignar(self, op):
        self.__operadorAux = op
        self.__operacion.set(op)
        self.operador2Entry.focus()
        valor = self.__operador1.get()
        valor = re.split('[+i.]', valor)
        self.__primerOperando = Imaginario(valor[0], valor[1])
    def ponerNUMERO(self, numero):
        if self.__primerOperando == None:
            if self.__operadorAux == None:
                valor = self.__operador1.get()
                self.__operador1.set(valor + numero)
            else:
                return
        else:
            if self.__operador == None:
                valor = self.__operador2.get()
                self.__operador2.set(valor + numero)
            else:
                return

    def operacion(self, operacion):
        self.__operador = operacion
        valor = self.__operador2.get()
        valor = re.split('[+i.]', valor)
        self.__segundoOperando = Imaginario(valor[0], valor[1])
        self.realizaroperacion(self.__primerOperando, self.__operadorAux, self.__segundoOperando)


    def realizaroperacion(self, operando1, operacion, operando2):
        resultado = 0
        if operacion == '+':
            resultado = operando1 + operando2
        else:
            if operacion == '-':
                resultado = operando1 - operando2
            else:
                if operacion == '*':
                    resultado = operando1 * operando2
                else:
                    if operacion == '/':
                        resultado = operando1 / operando2

        self.__panel.set(str(resultado.real) + str("+") + str(resultado.imag) + str("i"))


def main():
    calculadora = Calculadora()


if __name__ == '__main__':
    main()