def calcular_temperatura_promedio(datos):
    promedios = {}
    for produccion, semanas in datos.items():
        suma_temperaturas = 0
        total_dias = 0
        for semana in semanas:
            suma_temperaturas += sum(semana)
            total_dias += len(semana)
        promedio = suma_temperaturas / total_dias
        promedios[produccion] = promedio
    return promedios

# Ejemplo de datos
datos = {
    'produccion A': [
        [20, 21, 22, 23, 24, 25, 26],
        [19, 20, 21, 22, 23, 24, 25],
        [18, 19, 20, 21, 22, 23, 24],
        [17, 18, 19, 20, 21, 22, 23]
    ],
    'produccion B': [
        [22, 23, 24, 25, 26, 27, 28],
        [21, 22, 23, 24, 25, 26, 27],
        [20, 21, 22, 23, 24, 25, 26],
        [19, 20, 21, 22, 23, 24, 25]
    ],
    'produccion C': [
        [18, 19, 20, 21, 22, 23, 24],
        [17, 18, 19, 20, 21, 22, 23],
        [16, 17, 18, 19, 20, 21, 22],
        [15, 16, 17, 18, 19, 20, 21]
    ]
}

# Calculamos la temperatura promedio para cada cantidad de produccion
temperaturas_promedio = calcular_temperatura_promedio(datos)

# Mostramos los resultados
print("Bienvenidos")
print("Cada lista interior representa una semana de temperaturas")
for produccion, promedio in temperaturas_promedio.items():
    print(f"Temperatura promedio de la cantidad de {produccion}: {promedio}")

