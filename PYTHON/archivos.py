c = open("chanchito.txt", "w")
# R (Read) permite leer
# A (Append) permite modificar al final pero no en el medio
# W (Write) permite modificar el archivo por completo (SE BORRA TODO)
# X si el archivo no se encuentra creado lo crea, sino error

print(c.read()) # Leer la totalidad del archivo txt
print(c.readline()) # Leer linea por linea (Se van agregando)

c.write("\nagregaremos una nueva linea a nuestro archivo")
# Barra invertida con n punto y a parte

c.close()

x = open("chanchito.txt")

print(x.read())

import os # Para eliminar directorios

if os.path.exists("chanchito.txt"):
    os.remove("chanchito.txt") # Eliminar archivos
else:
    print("El archivo no existe")

os.rmdir("micarpeta") # Eliminar carpetas