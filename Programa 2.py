def ordenar_fila(matriz, fila):
    matriz[fila] = sorted(matriz[fila])
    return matriz

# Matriz de ejemplo
matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Fila a ordenar
fila_a_ordenar = 1

# Llamada a la función
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Imprimir matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Imprimir matriz con fila ordenada
print("\nMatriz con fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
