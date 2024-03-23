# Crear un diccionario con información personal
informacion_personal = {
    "Nombre": "Juan",
    "Cedula": 1600324567,
    "Ciudad": "Pastaza",
    "Profesion": "Doctor en medicina general"
}

# Agregar una nueva clave-valor representando la profesión
informacion_personal["Profesion"] = "Psicologo"

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal[ "Parroquia"] = "Mera"

# Verificar si la clave "Edad" existe y agregarla si no
if "Edad" not in informacion_personal:
    informacion_personal["Edad"] = "35"

# Eliminar la clave "Cedula" del diccionario
if "Cedula" in informacion_personal:
    del informacion_personal["Cedula"]

# Imprimir el diccionario final
print(informacion_personal)
