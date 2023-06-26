from tkinter import *
from tkinter import ttk, messagebox
class Aplicacion():
    __ventana=None
    __cantidad=None
    __preciobase=None
    __precioactual=None
    __cantidadAli=None
    __preciobaseAli=None
    __precioactualAli=None
    __cantidadEdu=None
    __preciobaseEdu=None
    __precioactualEdu=None
    __ipc=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('450x250')
        self.__ventana.title('Cálculo del Índice de Precios al Consumidor (IPC)')
        mainframe = ttk.Frame(self.__ventana, padding="2 10 5 10") #o,n,e,s
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 10
        #mainframe['relief'] = 'sunken'
        self.__cantidad = StringVar()
        self.__preciobase = StringVar()
        self.__precioactual = StringVar()
        self.__ipc = StringVar()
        ttk.Label(mainframe, text="Item").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text="Cantidad").grid(column=2, row=1, sticky=W)
        ttk.Label(mainframe, text="Precio año Base").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="Precio año Actual").grid(column=4, row=1, sticky=W)
        ttk.Label(mainframe, text="Vestimenta").grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text="Alimentos").grid(column=1, row=3, sticky=W)
        ttk.Label(mainframe, text="Educacion").grid(column=1, row=4, sticky=W)
        ttk.Label(mainframe, text="IPC%").grid(column=1, row=7, sticky=W)
        ttk.Label(mainframe, text="%").grid(column=2, row=7, sticky=(W,E))

        #caja de entrada cantidad segunda fila
        self.cantidadEntry = ttk.Entry(mainframe, width=10, textvariable=self.__cantidad)
        self.cantidadEntry.grid(column=2, row=2, sticky=W)

        self.preciobaseEntry= ttk.Entry(mainframe, width=10, textvariable=self.__preciobase)
        self.preciobaseEntry.grid(column=3, row=2, sticky=E)

        self.precioactualEntry = ttk.Entry(mainframe, width=10, textvariable=self.__precioactual)
        self.precioactualEntry.grid(column=4, row=2, sticky=E)

        # cajas de entradas de la Tercera fila
        self.cantidad_alimentosEntry = ttk.Entry(mainframe, width=10, textvariable=self.__cantidadAli)
        self.cantidad_alimentosEntry.grid(column=2, row=3, sticky=W)

        self.preciobase_alimentosEntry= ttk.Entry(mainframe, width=10, textvariable=self.__preciobaseAli)
        self.preciobase_alimentosEntry.grid(column=3, row=3, sticky=E)

        self.precioactual_alimentosEntry = ttk.Entry(mainframe, width=10, textvariable=self.__precioactualAli)
        self.precioactual_alimentosEntry.grid(column=4, row=3, sticky=E)

        # cajas de entradas de la cuarta fila
        self.cantidad_eduEntry = ttk.Entry(mainframe, width=10, textvariable=self.__cantidadEdu)
        self.cantidad_eduEntry.grid(column=2, row=4, sticky=W)

        self.preciobase_eduEntry = ttk.Entry(mainframe, width=10, textvariable=self.__preciobaseEdu)
        self.preciobase_eduEntry.grid(column=3, row=4, sticky=E)

        self.precioactual_eduEntry = ttk.Entry(mainframe, width=10, textvariable=self.__precioactualEdu)
        self.precioactual_eduEntry.grid(column=4, row=4, sticky=E)


        # este label muestra el resultado
        ttk.Label(mainframe, textvariable=self.__ipc).grid(column=1,row=7, sticky=E)
        ttk.Button(mainframe, text="Calcular IPC",command=self.calcular).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=4, row=6, sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=10, pady=7)
        self.cantidadEntry.focus()
        self.__ventana.mainloop()

    def calcular(self):
        try:
            valorcant=int(self.cantidadEntry.get())
            valorpreciobase=float(self.preciobaseEntry.get().replace(",", "."))
            valorprecioactual=float(self.precioactualEntry.get().replace(",", "."))
            ipcvestimenta=((valorcant*valorprecioactual)/(valorcant*valorpreciobase))%1
            #aliementos
            valorcantA=int(self.cantidad_alimentosEntry.get())
            valorbaseA=float(self.preciobase_alimentosEntry.get().replace(",", "."))
            valoractualA = float(self.precioactual_alimentosEntry.get().replace(",", "."))
            ipcAli=((valorcant*valoractualA)/(valorcant*valorbaseA))%1
            #educacion
            valorcantE = int(self.cantidad_eduEntry.get())
            valorbaseE = float(self.preciobase_eduEntry.get().replace(",", "."))
            valoractualE = float(self.precioactual_eduEntry.get().replace(",", "."))
            ipcEdu = ((valorcantE * valoractualE) / (valorcantE * valorbaseE)) % 1
            #totales
            ipc=ipcvestimenta+ipcAli+ipcEdu
            self.__ipc.set("{:.2f}".format(ipc * 100))
        except:
            messagebox.showerror(title="Error", message="Debe ingresar un numero o debe ingresar todos los campos")
            self.__precioactual.set("")
            self.__preciobase.set("")
            self.__cantidad.set("")
            self.cantidadEntry.focus()

def testAPP():
    mi_app = Aplicacion()
if __name__ == '__main__':
    testAPP()