# Escritura de Archivo de Texto
# Crear un nuevo archivo llamado my_colores.txt

with open("my_colores.txt", "w") as file:

    # Escribir al menos tres líneas de colores personales en el archivo

    file.write("Rojo 1: Es mi automovil.\n")
    file.write("Verde 2: Es mi color favorito.\n")
    file.write("Blanco 3: De blanco me voy a vestir el dia martes.\n")

# Lectura de Archivo de Texto
# Abrir el archivo my_colores.txt
with open("my_colores.txt", "r") as file:

    # Leer el contenido del archivo línea por línea
    for line in file.readlines():

        # Mostrar en la consola cada línea leída
        print(line.strip())

# Cierre de Archivos
# El archivo se cierra automáticamente al salir del bloque "with"
