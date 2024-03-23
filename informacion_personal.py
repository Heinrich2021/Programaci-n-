# Crear un diccionario con información personal
Informacion_personal = {
    "Nombre": "Juan",
    "Cedula": 1600324567,
    "Ciudad": "Pastaza",
    "Profesion": "Doctor en medicina general"
}

# Agregar una nueva clave-valor representando la profesión
Informacion_personal["Profesion"] = "Psicologo"

# Acceder al valor de la clave "ciudad" y modificarlo
Informacion_personal[ "Parroquia"] = "Mera"

# Verificar si la clave "Edad" existe y agregarla si no
if "Edad" not in Informacion_personal:
    Informacion_personal["Edad"] = "35"

# Eliminar la clave "Cedula" del diccionario
if "Cedula" in Informacion_personal:
    del Informacion_personal["Cedula"]

# Imprimir el diccionario final
print(Informacion_personal)
