print("Reglas del juego: para colocar una X o un O debera seleccionar fila.columna, ejemplo 1.3 seria primera fila tercera columna")

fila1 = ["_", "_", "_"]
fila2 = ["_", "_", "_"]
fila3 = ["_", "_", "_"]

print("\n", fila1, "\n", fila2, "\n", fila3)

def Jugada1():
    jugador1 = input("Donde desea ingresar la X?:")
    if jugador1 == "exit":
        exit()
    if jugador1 == "1.1":
        if fila1[0] == "_": 
            fila1[0] = "X"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada1()
    elif jugador1 == "1.2":
        if fila1[1] == "_": 
            fila1[1] = "X"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada1()
    elif jugador1 == "1.3":
        if fila1[2] == "_": 
            fila1[2] = "X"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada1()
    elif jugador1 == "2.1":
        if fila2[0] == "_": 
            fila2[0] = "X"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada1()
    elif jugador1 == "2.2":
        if fila2[1] == "_": 
            fila2[1] = "X"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada1()
    elif jugador1 == "2.3":
        if fila2[2] == "_": 
            fila2[2] = "X"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada1()
    elif jugador1 == "3.1":
        if fila3[0] == "_": 
            fila3[0] = "X"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada1()
    elif jugador1 == "3.2":
        if fila3[1] == "_": 
            fila3[1] = "X"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada1()
    elif jugador1 == "3.3":
        if fila3[2] == "_": 
            fila3[2] = "X"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada1()
    else:
        print("Por favor ingrese una casilla valida")
        Jugada1()
        
def Jugada2():
    jugador2 = input("Donde desea ingresar la O?:")
    if jugador2 == "exit":
        exit()
    if jugador2 == "1.1":
        if fila1[0] == "_": 
            fila1[0] = "O"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada2()
    elif jugador2 == "1.2":
        if fila1[1] == "_": 
            fila1[1] = "O"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada2()
    elif jugador2 == "1.3":
        if fila1[2] == "_": 
            fila1[2] = "O"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada2()
    elif jugador2 == "2.1":
        if fila2[0] == "_": 
            fila2[0] = "O"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada2()
    elif jugador2 == "2.2":
        if fila2[1] == "_": 
            fila2[1] = "O"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada2()
    elif jugador2 == "2.3":
        if fila2[2] == "_": 
            fila2[2] = "O"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada2()
    elif jugador2 == "3.1":
        if fila3[0] == "_": 
            fila3[0] = "O"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada2()
    elif jugador2 == "3.2":
        if fila3[1] == "_": 
            fila3[1] = "O"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada2()
    elif jugador2 == "3.3":
        if fila3[2] == "_": 
            fila3[2] = "O"
            print("\n", fila1, "\n", fila2, "\n", fila3)
        else: 
            print("Esa casilla esta ocupada")
            Jugada2()
    else:
        print("Por favor ingrese una casilla valida")
        Jugada2()

Jugada1()
Jugada2()
Jugada1()
Jugada2()
Jugada1()
Jugada2()
Jugada1()

def Ganador():
    if fila1[0] == "X" and fila2[0] == "X" and fila3[0] == "X":
        print ("FELICITACIONES JUGADOR 1")
        exit()
    elif fila1[1] == "X" and fila2[1] == "X" and fila3[1] == "X":
        print ("FELICITACIONES JUGADOR 1")
        exit()
    elif fila1[2] == "X" and fila2[2] == "X" and fila3[2] == "X":
        print ("FELICITACIONES JUGADOR 1")
        exit()
    elif fila1[0] == "X" and fila1[1] == "X" and fila1[2] == "X":
        print ("FELICITACIONES JUGADOR 1")
        exit()
    elif fila2[0] == "X" and fila2[1] == "X" and fila2[2] == "X":
        print ("FELICITACIONES JUGADOR 1")
        exit()
    elif fila3[0] == "X" and fila3[1] == "X" and fila3[2] == "X":
        print ("FELICITACIONES JUGADOR 1")
        exit()
    elif fila1[0] == "X" and fila2[1] == "X" and fila3[2] == "X":
        print ("FELICITACIONES JUGADOR 1")
        exit()
    elif fila1[2] == "X" and fila2[1] == "X" and fila3[0] == "X":
        print ("FELICITACIONES JUGADOR 1")
        exit()
    elif fila1[0] == "O" and fila2[0] == "O" and fila3[0] == "O":
        print ("FELICITACIONES JUGADOR 2")
        exit()
    elif fila1[1] == "O" and fila2[1] == "O" and fila3[1] == "O":
        print ("FELICITACIONES JUGADOR 2")
        exit()
    elif fila1[2] == "O" and fila2[2] == "O" and fila3[2] == "O":
        print ("FELICITACIONES JUGADOR 2")
        exit()
    elif fila1[0] == "O" and fila1[1] == "O" and fila1[2] == "O":
        print ("FELICITACIONES JUGADOR 2")
        exit()
    elif fila2[0] == "O" and fila2[1] == "O" and fila2[2] == "O":
        print ("FELICITACIONES JUGADOR 2")
        exit()
    elif fila3[0] == "O" and fila3[1] == "O" and fila3[2] == "O":
        print ("FELICITACIONES JUGADOR 2")
        exit()
    elif fila1[0] == "O" and fila2[1] == "O" and fila3[2] == "O":
        print ("FELICITACIONES JUGADOR 2")
        exit()
    elif fila1[2] == "O" and fila2[1] == "O" and fila3[0] == "O":
        print ("FELICITACIONES JUGADOR 2")
        exit()
    elif fila1.count("_") == 0 and fila2.count("_") == 0 and fila3.count("_") == 0:
        print("Ha sido un empate")
        exit()

Ganador()
Jugada2()
Ganador()
Jugada1()
Ganador()

# TicTacToe by Nacho Bigarella