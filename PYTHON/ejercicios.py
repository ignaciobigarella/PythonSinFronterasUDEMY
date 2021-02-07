# EJERCICIO JUEGO. SI EL DATO EXISTE ENTONCES LO TOMA Y LO REPITE
# SI NO EXISTE SALE QUE NO EXISTE Y REPITE TU DATO ERRONEO

dato = input("Ingrese dato: ")

lista = ["hola", "mundo", "chanchito", "feliz", "dragones"]

if lista.count(dato) == 0 or 1 or 2 or 3 or 4 or 5:
    print("El dato existe:", dato)
else:
    print("No existe", dato, ":(")

primero = input("Ingrese primer numero: ")

# TRY si o si el primero tiene que ser un INT
# EXCEPT va a chanchito feliz (Se le asigna un print)
# Si va a EXCEPT entonces sale un mensaje
# Si va a TRY realiza la suma

try:
    primero = int(primero)
except:
    primero = "chanchito feliz"

if primero == "chanchito feliz":
    print("El valor ingresado no es un entero")
    exit()

segundo = input("Ingrese segundo numero: ")

try:
    segundo = int(segundo)
except:
    segundo = "chanchito feliz"

if segundo == "chanchito feliz":
    print("El valor ingresado no es un entero")
    exit()

simbolo = input("Ingrese operacion: ")

if simbolo == "+":
    print("Suma:", primero + segundo)
elif simbolo == "-":
    print("Resta:", primero - segundo)
elif simbolo == "*":
    print("Multiplicacion", primero * segundo)
elif simbolo == "/":
    print ("Division", primero / segundo)
else:
    print("El simbolo ingresado no es valido")
# primerNumero = int(primero)
# segundoNumero = int(segundo)

# print(primero + segundo) ESTO CONCATENA NO SUMA
# print(primerNumero + segundoNumero) # INT transforma en número