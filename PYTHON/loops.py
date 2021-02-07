i = 0
while i < 5: # Se repite acción hasta que se cumpla la condición
    print(i)
    if i == 3:
        break # Detiene el while
    i += 1 # Le suma 1 al valor de i


while i < 5: # Se repite acción hasta que se cumpla la condición
    i += 1
    if i == 3:
        continue # Saltea un valor y sigue con el while
    print(i)

# En este caso se imprime 5 porque primero se incrementa el valor de i

usuarios = ["Chanchito feliz", "Felipe", "Roberto", "Nicolas"]

for usuario in usuarios: # Acceder a todos los elementos de la lista
    print(usuario)

usuario = "Chanchito feliz"

for c in usuario: # Acceder a los caracteres de lista
    print(c)

usuarios = ["Chanchito feliz", "Felipe", "Roberto", "Nicolas"]

for usuario in usuarios:
    if usuario == "Roberto":
        break # Break y continue se utilizan igual que antes
    print(usuario) 

for x in range(3, 30, 3): # Imprime valores entre uno y el otro
    # El número final indica de cuanto en cuanto aumentan
    print(x)
else: # Cuando se termina el loop del for
    print("Hemos terminado") 

usuarios = ["Chanchito feliz", "Felipe", "Roberto", "Nicolas"]

edades = [24, 25, 26, 35]

for usuario in usuarios: # For adentro de for
    for edad in edades:
        print (usuario, edad)
