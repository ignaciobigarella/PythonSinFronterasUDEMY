# IF

if 2 < 5: # Dos puntos siempre despues de if
     print("2 es menor que 5")

# # a == b
# # a < b
# # a > b
# # a != b
# # a <= b
# # a >= b

# if 2 == 2:
#     print("2 es igual a 2")
    
# if 2 == 3:
#     print("2 es igual a 3")

# if 2 > 5:
#     print("2 es mayor a 5")

# if 5 > 2:
#     print("5 es mayor a 2")

# if 2 != 2:
#     print("2 es distinto a 2")

# if 3 != 2:
#     print("3 es distinto a 2")

# if 3 >= 2:
#     print("3 es mayor o igual a 2")

# if 3 <= 3:
#     print("3 es menor o igual a 2") siempre tabular post if

# ELIF Y ELSE

if 2 > 2:
    print("2 es menor a 5 en if") # Si es verdadero se ejecuta esto
elif 2 < 2:
    print("2 es menor a 5 en elif") # Si es falso y elif verdadero esto
elif 2 < 5:
    print("2 es menor a 5 en 2do elif") # Se encadenan elif
else:
    print("Todo lo anterior es falso") # Si todo es falso sale esto

if 2 > 2:
    print("2 es menor a 5 en if") # Si es verdadero se ejecuta esto
else:
    print("Todo lo anterior es falso") # Si todo es falso sale esto

# IF UNA LINEA / OPERADOR TERNARIO TRUE Y FALSE

if 2 < 5: print("If de una linea")

print("Cuando devuelve true") if 5 > 2 else print("Cuando devuelve false")

# AND (TODAS SON TRUE) Y OR (UNA DE LAS DOS ES TRUE)

if 2 < 5 and 3 > 2:
    print("Ambas devuelven true") # se ejecuta

if 2 < 5 and 3 > 3:
    print("Hay una falsa") # no se ejecuta

if 1 < 0 or 1 > 0:
    print ("Una es verdadera") # se ejecuta

if 1 < 0 or 0 > 0:
    print ("Ambas son falsas") # no se ejecuta

