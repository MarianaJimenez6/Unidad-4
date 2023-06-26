import tkinter as tk
from tkinter import messagebox
from clasePelicula import Pelicula

class ContactList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

    def insertar(self, contacto, index=tk.END):
        text = "{}".format(contacto.get_titulo())
        self.lb.insert(index, text)


class ContactForm(tk.LabelFrame):
    fields = ("Titulo", "Lenguaje", "Fecha", "Generos", "Resumen")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Pelicula", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        if text == "Resumen":
            entry = tk.Text(self.frame, width=40, height=10, font=('Calibri',10))  # Usar tk.Text para el campo "Resumen"
        else:
            entry = tk.Entry(self.frame, width=30)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoContactoEnFormulario(self, pelicula):
        values = (
            pelicula.get_titulo(), pelicula.get_generos(),
            pelicula.get_lenguaje(), pelicula.get_fecha(), pelicula.get_resumen()
        )
        for entry, value in zip(self.entries, values):
            if isinstance(entry, tk.Text):  # Verificar si el campo es una instancia de tk.Text
                entry.delete("1.0", tk.END)  # Borrar el contenido existente en el campo de texto
                entry.insert("1.0", value)  # Insertar el valor en el campo de texto
            else:
                entry.delete(0, tk.END)
                entry.insert(0, value)


    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
        self.text_field.delete(0, tk.END)


class ContactsView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de peliculas")
        self.list = ContactList(self, height=20, width=35)
        self.form = UpdateContactForm(self)
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        #self.btn_new.pack(side=tk.BOTTOM, pady=5)
    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.list.bind_doble_click(ctrl.seleccionarContacto)

    def agregarContacto(self, contacto):
        self.list.insertar(contacto)
    #Ver estado de Contacto en formulario de contactos
    def verContactoEnForm(self, contacto):
        self.form.mostrarEstadoContactoEnFormulario(contacto)


class UpdateContactForm(ContactForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)