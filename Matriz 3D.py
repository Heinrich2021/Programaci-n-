# Crear una matriz 3D para representar las temperaturas diarias en varias ciudades
# La matriz tendrá la forma (ciudades, días de la semana, semanas)
temperaturas = [
    # Ciudad 1
    [
        # Semana 1
        [25, 26, 27, 28, 29, 30, 31],  # Lunes a Domingo
        # Semana 2
        [24, 25, 26, 27, 28, 29, 30],
        # Semana 3
        [23, 24, 25, 26, 27, 28, 29],
    ],

    # Ciudad 2
    [
        # Semana 1
        [20, 21, 22, 23, 24, 25, 26],
        # Semana 2
        [19, 20, 21, 22, 23, 24, 25],
        # Semana 3
        [18, 19, 20, 21, 22, 23, 24],
    ],
]

# Calcular el promedio de temperaturas para cada ciudad por semana
for ciudad in range(len(temperaturas)):
    for semana in range(len(temperaturas[ciudad])):
        suma_temperaturas = 0
        for dia in range(len(temperaturas[ciudad][semana])):
            suma_temperaturas += temperaturas[ciudad][semana][dia]
        promedio_temperaturas = suma_temperaturas / len(temperaturas[ciudad][semana])
        print(f"Promedio de temperaturas para la Ciudad {ciudad + 1}, Semana {semana + 1}: {promedio_temperaturas}")

