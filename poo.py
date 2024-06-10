class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


class Arquero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arco):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arco = arco

    def cambiar_arco(self):
        opcion = int(input("Elige un arco: (1) Arco Largo, daño 5. (2) Arco Compuesto, daño 7"))
        if opcion == 1:
            self.arco = 5
        elif opcion == 2:
            self.arco = 7
        else:
            print("Número de arco incorrecto")

    def atributos(self):
        super().atributos()
        print("·Arco:", self.arco)

    def daño(self, enemigo):
        return self.fuerza * self.arco - enemigo.defensa


class Clerigo(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, baston):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.baston = baston

    def atributos(self):
        super().atributos()
        print("·Bastón:", self.baston)

    def curar(self, aliado):
        if self.esta_vivo():
            cura = self.inteligencia * self.baston
            aliado.vida = aliado.vida + cura
            print(self.nombre, "ha curado a", aliado.nombre, "por", cura, "puntos de vida")
            print("Vida de", aliado.nombre, "es", aliado.vida)

    def daño(self, enemigo):
        return self.inteligencia - enemigo.defensa


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


# Ejemplo de uso
personaje_1 = Arquero("Legolas", 15, 8, 5, 80, 4)
personaje_2 = Clerigo("Gandalf", 8, 20, 6, 90, 2)

personaje_1.atributos()
personaje_2.atributos()

# Ejemplo de combate
combate(personaje_1, personaje_2)
