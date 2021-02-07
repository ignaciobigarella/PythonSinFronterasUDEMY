class Usuario: # Clase siempre primera letra mayuscula
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("Hola!, mi nombre es", self.nombre, self.apellido)

class Admin(Usuario): # Herencia (Admin clase padre)
    def superSaludo(self):
        print("Hola!, me llamo", self.nombre, "y soy administrador")

usuario = Usuario("Felipe", "Feliz") # Instancias de la clase siempre con minuscula

usuario.nombre = "Chanchito" # Cambiar propiedad de instancia
usuario.saludo()
usuario.supersaludo()

# del usuario.nombre # Borrar propiedad de instancia
# del usuario # Borrar instancia

admin = Admin("Super", "Feliz")
admin.saludo()
admin.superSaludo()

# usuario.superSaludo() # No se puede ejecutar porque es clase hijo



