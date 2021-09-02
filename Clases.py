class Botella:
    capacidadMaxima = None
    color = None
    marca = None
    alto = None
    ancho = None
    materialConstruccion = None
    capacidadActual = 0

    def rellenarBotella(self, ml):
        if ((self.capacidadActual + ml) > self.capacidadMaxima):
            return "No se puede llenar la botella, SUPERA LA CAPACIDAD MAXIMA!"
        else:
            #self.capacidadActual += ml
            self.capacidadActual = self.capacidadActual + ml
            return "Botella Rellenada!"









class Animal:
    pass


class Auto:
   pass 
