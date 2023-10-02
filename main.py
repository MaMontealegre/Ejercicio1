print("Hola desde Replit")

#crear una clase Automovil que tenga por defecto atributo ruedas
#inicializado en 4, con un constructor con los parametros de color,
#marca, aceleracion y velocidad


class Automovil:
  ruedas = 4

  def __init__(self, color, marca, aceleracion):
    self.color = color
    self.marca = marca
    self.aceleracion = aceleracion
    self.velocidad = 0

  def acelera(self):
    self.velocidad=self.aceleracion+self.velocidad
  def frena(self):
    self.velocidad=self.aceleracion-self.velocidad

#crear un coche, mostrar por consola las ruedas y la aceleracion
coche1 = Automovil("rojo", "Toyota", 20)
print(coche1.ruedas)
print(f'El coche tiene una aceleracion de: {coche1.aceleracion}')
#modificar la aceleracion y mostrar por pantalla ambas aceleraciones
coche1.aceleracion = 30
print(coche1.aceleracion)

#crear metodo acelera() que aumentara la velocidad + aceleracion
#crear metodo frena() que restara a la velocidad la aceleracion
print(f'El coche tiene una velocidad de {coche1.velocidad}')
coche1.acelera()
print(f'El coche tiene una velocidad de {coche1.velocidad}')
coche1.frena()
print(f'El coche tiene una velocidad de {coche1.velocidad}')

#crear clase AutomovilVolador que herede de Automovil con atributo 6 ruedas
class AutomovilVolador(Automovil):
  ruedas=6

#agregar al constructor esta_volando=true
  def __init__(self,color,marca,aceleracion,esta_volando=True):
    super().__init__(color,marca,aceleracion)
    esta_volando=True
    