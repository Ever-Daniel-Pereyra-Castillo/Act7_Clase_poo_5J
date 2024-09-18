print("Programacion POO")
# Definicion de clases
class perro:

    def morder(self):
        print("El perro me mordio")
    def Datos_perro(self,nombre,edad):
        print(f" Nombre: {nombre} edad: {edad}")    


# Zona de creacion de objeto
pitbull=perro()


# Zona de uso de clases
pitbull.Datos_perro("boby",4)
pitbull.morder()

