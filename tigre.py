import random

class Tigre:
    """Clase para representar un tigre."""

    def __init__(self, nombre, velocidad, agresivo):
        """Constructor para la clase Tigre."""

        self.nombre = nombre            #string
        self.velocidad = velocidad      #int(km/h)
        self.agresivo = agresivo        #bool


    def acariciar(self):
        """Método para acariciar al tigre. Si el tigre no es agresivo ronroneará.
        Si es agresivo es muy probable que te muerda, si no lo hace gruñirá. """

        if self.agresivo:
            if random.randint(0,10) < 9:
                print(f"{self.nombre} te intenta arrancar el brazo")
            else:
                print(f"{self.nombre} te gruñe")
        else:
            print(f"{self.nombre} ronronea")


    def rugir(self, potencia):
        """Método para hacer rugir al tigre indicando la potencia del rugido."""

        if potencia < 3:
            print("gr...")
        elif potencia < 5:
            print("Grr")
        elif potencia < 8:
            print("GRR!")
        else:
            print("GRRRRRRRRRRRRR!!!!!!")