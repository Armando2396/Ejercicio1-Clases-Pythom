class Vehiculo():
    color = "Gris"
    Ruedas = 4
    Puertas = 4


class Coche(Vehiculo):
    Velocidad = "300km"
    Cilindrada = 4


C = Coche()

print("El auto es de color: " + C.color)
print("La velocidad del auto es: " + C.Velocidad)