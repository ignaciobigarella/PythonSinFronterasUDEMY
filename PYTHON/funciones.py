def miFuncion(): # Definir funcion siempre ():
    print("Mi pimera funcion")

miFuncion() # Escribir para ejecutar lo que pasa abajo de funcion

def imprimeDato(*nombre):
    print("El nombre completo es", nombre[1])

# Argumento cuando definimos, parametro cuando hacemos referencia
# Cantidad de parametros siempre igual a argumentos (Separados con ,)
# Con * adelante de (argumentoUno) imprime tupla
# Para acceder solo a un valor en el print argumentoUno["Posicion"]

imprimeDato("Chanchito", "feliz", "lala", "lele")

# Def sin orden

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

nombreCompleto(nombre="Chanchito", apellido="feliz") # No importa orden

# Argumento por llave

def nombreCompleto2(**kwargs): # Argumento por llave
    print(kwargs["nombre"], kwargs["apellido"])

nombreCompleto2(nombre="Chanchito", apellido="Feliz")

# Nombrar valor de argumento por defecto

def miFuncion2(argumento = "Chanchito"):
    print(argumento)

miFuncion2("Batman") # Se define nombre
miFuncion2() # Se nombra por defecto como esta en el argumento

# Imprime valores separados

def miFuncionLista(lista):
    for el in lista:
        print(el)

miFuncionLista(["Chanchito", "feliz"])

# Imprime valores en una misma oracion

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

nombres = concatenaNombres(["Chanchito", "Feliz"])
print(nombres) 

# Recursividad con condicion de salida
# Sirve para intentar varias veces algo y lanzar error tras varios intentos
# Procesar de a x cantidad de elementos

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)