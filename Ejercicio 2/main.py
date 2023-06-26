import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox


class Aplicacion(tk.Tk):
    __precio = None
    __iva = None
    __precioiva = None

    def __init__(self):
        super().__init__()  # o,n,e,s
        self.__ivaradio = tk.IntVar()
        self.__precio = tk.StringVar()
        self.__iva = tk.StringVar()
        self.__precioiva = tk.StringVar()
        self.prueba = tk.IntVar()
        label_a = tk.Label(self, text="Calculo IVA", bg="#DAE8FC")
        label_a.pack(ipadx=10, ipady=10, fill=tk.X)
        # ipadx se utiliza Crea relleno interno a izquierda y derecha, o relleno a lo largo del eje x.(a los widgets)
        # ipady Crea relleno superior e inferior, o relleno a lo largo del eje Y.
        # self.separ1 = ttk.Separator(self, orient=HORIZONTAL

        frametop=tk.Frame(self)
        frametop.pack(side=tk.TOP)

        PRECIO = tk.Label(frametop,text="Precio sin IVA")
        PRECIO.pack(padx=20,side=tk.LEFT,fill=tk.BOTH)
        
        #fill=tk.X, side=tk.LEFT
        self.precioEntry = ttk.Entry(frametop,width=15, textvariable=self.__precio)
        self.precioEntry.pack(pady=20, padx=20,fill=tk.BOTH,side=tk.LEFT)

        #Radio Button iva 21 y iva 10.5
        ttk.Radiobutton(self,text='Iva 21 %', value=0, variable=self.__ivaradio
                        ).pack(fill=tk.X,pady=5, padx=5)

        ttk.Radiobutton(self,text='Iva 10.5 %', value=1, variable=self.__ivaradio
                        ).pack(fill=tk.X,pady=5, padx=5)

        #Frame de IVA
        framedown = tk.Frame()
        framedown.pack(side=tk.TOP)

        label_iva = tk.Label(framedown,text="IVA")
        label_iva.pack(padx=10,ipadx=40,side=tk.LEFT,fill=tk.BOTH)

        self.iva21Entry = ttk.Entry(framedown,width=15, textvariable=self.__iva)
        self.iva21Entry.pack(pady=10, padx=10,side=tk.LEFT,fill=tk.BOTH)

        #Frame de Precio con iVA
        Framepreciototal = tk.Frame()
        Framepreciototal.pack(side=tk.TOP)

        label_preciototal = tk.Label(Framepreciototal, text="Precio con IVA")
        label_preciototal.pack(pady=20, padx=20,side=tk.LEFT,fill=tk.BOTH)

        self.precioivaEntry = tk.Entry(Framepreciototal, width=15, textvariable=self.__precioiva)
        self.precioivaEntry.pack(pady=20, padx=20,side=tk.LEFT,fill=tk.BOTH)

        #Frame botones
        Framebotones = tk.Frame()
        Framebotones.pack(side=tk.TOP)

        tk.Button(Framebotones,text="Calcular",bg="light green", command=self.cambiaValorMM).pack(padx=20,pady=20,ipadx=10,side=tk.LEFT,fill=tk.BOTH)
        tk.Button(Framebotones,text="Salir",bg="salmon",borderwidth=3,command=self.destroy).pack(padx=20,pady=20,ipadx=20,side=tk.LEFT,fill=tk.BOTH)


    def cambiaValorMM(self):
        if self.__ivaradio.get() == 0 :
            precio = float(self.precioEntry.get().replace(",", "."))
            iva = precio * 0.21
            precio += iva
            self.__iva.set(iva)
            self.__precioiva.set(precio)
        else:
            if self.__ivaradio.get() ==1 :
                precio = float(self.precioEntry.get().replace(",", "."))
                iva = precio * 0.105
                precio += iva
                self.__iva.set(iva)
                self.__precioiva.set(precio)


if __name__ == '__main__':
    app = Aplicacion()
    app.mainloop()