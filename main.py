from tigre import Tigre
import random

# Primero creamos un tigre con las siguientes características
#       Nombre: Shere Khan
#       Velocidad: 60km/h
#       Agresivo: sí
tigre_salvaje = Tigre("Shere Khan", 60, True)

# Método acariciar()
# Probaremos a intentar acariciar al tigre 5 veces seguidas
for _ in range(0, 5):
    tigre_salvaje.acariciar()

# Método rugir()
# Haremos rugir al tigre con una potencia aleatoria
potencia = random.randint(0, 10)
tigre_salvaje.rugir(potencia)

# Método echar_carrera()
# Necesitaremos crear otro tigre para ambos tigres compitan
tigre_zoo = Tigre("Toby", 45, False)
tigre_salvaje.echar_carrera(tigre_zoo)