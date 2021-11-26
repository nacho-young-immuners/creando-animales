from tigre import Tigre

# Primero creamos un tigre con las siguientes características
#       Nombre: Shere Khan
#       Velocidad: 60km/h
#       Agresivo: sí
tigre_salvaje = Tigre("Shere Khan", 60, True)

# Método acariciar()
# Probaremos a intentar acariciar al tigre 5 veces seguidas
for _ in range(0, 5):
    tigre_salvaje.acariciar()