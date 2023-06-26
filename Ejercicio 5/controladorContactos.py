from vistaContactos import ContactsView

from controladorPeliculas import listaPeliculas

class ControladorContactos(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.contactos = list(repo.getlistapeliculas())
    # comandos de que se ejecutan a través de la vista

    def seleccionarContacto(self, index):
        self.seleccion = index
        contacto = self.contactos[index]
        self.vista.verContactoEnForm(contacto)

    def start(self):
        for c in self.contactos:
            self.vista.agregarContacto(c)
        self.vista.mainloop()
    def salirGrabarDatos(self):
        self.repo.grabarDatos()