#mkdir crea carpeta touch crea archivo cd ingreso a carpetas
if 3 > 5: # Acá va un comentario
    print('esto no se va a imprimir')

# if 5 > 3: # Acá va otro comentario
  #  print('5 es mayor a 3')

x = 5
y = 'chanchito feliz'

print(x, y)

email = 'chanchito@feliz.com'
print(email)

MIVAR = "chanchito1" #Variables constantes
mi_var = "chanchito2" #Separar palabras nunca guión medio
miVar = "chanchito3" #Separar palabras CamelCase

a, b, c = "Lala", "Lele", "Lili"

# print(a, b, c)

valor1 = valor2 = valor3 = "Chanchito feliz"
# print(valor1, valor2, valor3)

inicio = "Hola"
final = "Mundo"

# print(inicio, final) #Cuando se pone , van con espacio, con + juntas

palabra = 'hola mundo' #Strings se definen con comilla simple o doble
oracion = "hola mundo comillas dobles"

entero = 20 #Número INTEGER
conDecimales = 20.2 #Número FLOAT
complejo = 1j #Número COMPLEJO agregando J

# print(palabra, oracion, entero, conDecimales, complejo)

lista = ['Hola', 'Mundo', 'Chanchito feliz'] #Corchetes para definir lista vacía
lista2 = lista.copy() #Copiar lista sin append 
lista.append('Chanchito triste') #Agregar elementos a la lista
lista.clear() #Elimina elementos de lista

print(lista, lista2.count(3)) #.Count(valor) cuantas veces se repite un valor
print(len(lista), len(lista2)) #len(nombreLista) cantidad de elementos en lista
largoLista = len(lista)
largoLista2 = len(lista2)
# print(largoLista, largoLista2)

print(lista[0]) #Elemento 0 primer elemento de una lista

lista.pop() #Elimina el último elemento de la lista
lista.pop() #Y así sucesivamente (elimina nuevo último elemento)
lista.remove("Valor") #Elimina un elemento por su valor

lista.reverse() #Invierte orden de lista
lista.sort() #No se puede utilizar cuando hay STRINGS y NÚMEROS (ordenar)
tupla = ('Hola', 'Mundo', 'Somos', 'Tupla') #Tupla no tiene append
# tupla.count se puede utilizar al igual que en lista
# tupla.index("Valor") nos dice en que posición se encuentra el elemento
# (tupla[posición]) accede al elemento en esa posición
listaDeTupla = list(tupla) #Transforma tupla en lista
# listaDeTupla.append(4) ya se puede modificar ahora
# print(listaDeTupla)

rango = range(6)
# print(rango)

#Diccionario siempre con llaves y la coma va para agregar valores
diccionario = {
  "nombre": "Chanchito feliz",
  "raza": "Persa",
  "edad": 5
}

# print(diccionario)
print(diccionario['nombre']) # Corchetes para ir a valor
print(diccionario.get('nombre')) # .get('Valor') igual a corchetes
diccionario['nombre'] = 'Fluffy' #diccionario['Valor'] = cambiar valor
print(len(diccionario)) #Cantidad de elementos del diccionario
diccionario['ronronea'] = 'Si' #Tambien sirve para agregar

# print(diccionario)
diccionario.pop('ronronea') # .pop('Valor) para eliminar valor
diccionario.popitem() # elimina ultimo valor agregado al diccionario
del diccionario['ronronea'] # del (sin punto) elimina valor
diccionario.clear() # Elimina todos los valores del diccionario
copiaGatito = diccionario.copy() # Copia de diccionario
copiaGatito = dict(diccionario) # Copia de diccionario
# print(diccionario, copiaGatito)

# Creacion 1 de diccionario
Fluffy = {
  "nombre": "Fluffy",
  "edad": 4
}
Mamba = {
  "nombre": "Black Mamba",
  "edad": 12
}
gatitos = {
  "Fluffy": Fluffy,
  "Mamba": Mamba
}

print(gatitos)

# Creacion 2 de diccionarios
perritos = dict(nombre="Chanchito Feliz", edad=6)
print(perritos)

#Booleans
verdadero = True
falso = False

print(verdadero, falso)