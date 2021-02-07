class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print("Hola, soy un", self.tipo, "y mi sonido es el", self.onomatopeya)

class Gato(Animal): # Tiene extension de init forma 1
    tipo = "gato"
    def __init__(self, nombre, onomatopeya): # Ignora primer init
        Animal.__init__(self, nombre, onomatopeya) # Recuerda primer init hay que pasar self
        print ("Hola soy un gato extendido!")


class Perro(Animal): # Tiene extension de init forma 2
    tipo = "perro"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya) # Super clase padre no se pasa self
        print("Instanciando un perro")

class Canario(Animal):
    tipo = "canario"

gato = Gato("Fluffy", "maullido")
gato.saludo()

perro = Perro("Firulais", "ladrido")
perro.saludo()

canario = Canario("Piolin", "silbido")
canario.saludo()

# Todo lo que se define dentro de una class es exclusivo de esa class
# Sirve para hacer clases padre y Admin