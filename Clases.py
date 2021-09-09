class Auto:
    
    #Constructor (Se ejecuta automaticamente cuando el Objeto es creado!)
    def __init__(self, pat, nchas, mar, model, color):

        self.__Patente = str(pat).upper()
        self.Nchasis = str(nchas).upper()
        self.Marca = mar
        self.Modelo = model
        self.__Color = color

    def VerInfoAuto(self):
        return f"Auto Patente {self.__Patente}, Numero Chasis: {self.Nchasis}, Marca: {self.Marca}, Modelo: {self.Modelo}, Color: {self.__Color}"

    def VerPatente(self):
        """ Metodo que retorna la Patente del Vehiculo"""
        return self.__Patente

    def VerColor(self):
        """ Metodo que retorna el Color del Vehiculo"""
        return self.__Color

    def CambiarColor(self, color):
        self.__Color = color
    

class Mecanico:

    #Constructor
    def __init__(self, rut, nom, ape, edad, direc, email):

        self.Rut = rut #17.123.456-7 #Tarea
        self.Nombres = nom #Juan Ignacio #Tarea
        self.Apellidos = ape #Roman Riquelme #Tarea
        self.Edad = edad
        self.Direccion = direc
        self.CorreoElectronico = email

        if (edad >= 18):self.MayorEdad = True
        else: self.MayorEdad = False

    def VerInfoMecanico(self):
        return f"RUT: {self.Rut}, Nombres: {self.Nombres}, Apellidos: {self.Apellidos}"


class Reparacion:
    
    def __init__(self, cod, auto, mecanico, valor, repuestos):
        self.Codigo = cod
        self.AutoAsignado = auto
        self.Mecanico = mecanico
        self.Valor = valor
        self.RepuestoUtilizados = repuestos

    def VerInfoReparacion(self): 
        """Metodo que retorna la informacion detallada de la reparacion"""      
        return f"INFO REPARACION: AUTO REPARADO: {self.AutoAsignado.VerInfoAuto()}, MECANICO ASIGNADO: {self.Mecanico.VerInfoMecanico()}, VALOR: ${self.Valor}"

    def CambiarColorAuto(self, color):
        self.AutoAsignado.CambiarColor(color)