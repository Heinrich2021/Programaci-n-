def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"El valor {valor} se encontró en la posición ({i}, {j})."
    return f"El valor {valor} no se encontró en la matriz."

# Matriz de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 2

# Llamada a la función
resultado = buscar_valor(matriz, valor_a_buscar)

# Imprimir resultado
print(resultado)