import os

class Auto:
    
    #Constructor (Se ejecuta automaticamente cuando el Objeto es creado!)
    def __init__(self, pat, nchas, color, mar, model, year):

        self.__Patente = str(pat).upper()
        self.__Nchasis = str(nchas).upper()
        self.__Marca = mar
        self.__Modelo = model
        self.__Color = color
        self.__Year = year

    def GetInfo(self):
        """ Metodo que retorna la Informacion Completa del Auto"""
        return f"Auto Patente {self.__Patente}, Numero Chasis: {self.__Nchasis}, Marca: {self.__Marca}, Modelo: {self.__Modelo}, Color: {self.__Color}, Año: {self.__Year}"

    def VerPatente(self):
        """ Metodo que retorna la Patente del Vehiculo"""
        return self.__Patente

    def setPatente(self, pat):
        """ Metodo que modifica la Patente del Vehiculo"""
        self.__Patente = pat

    def VerColor(self):
        """ Metodo que retorna el Color del Vehiculo"""
        return self.__Color

    def CambiarColor(self, color):
        self.__Color = color
    

class Mecanico:

    #Constructor
    def __init__(self, rut, nom, ape, edad, direc):

        self.__Rut = rut #17.123.456-7 #Tarea
        self.__Nombres = nom #Juan Ignacio #Tarea
        self.__Apellidos = ape #Roman Riquelme #Tarea
        self.__Edad = edad
        self.__Direccion = direc


    def GetInfo(self):
        return f"RUT: {self.__Rut}, Nombres: {self.__Nombres}, Apellidos: {self.__Apellidos}"


class Reparacion:
    
    def __init__(self, auto, mecanico, valor, repuestos):
        self.AutoAsignado = auto
        self.Mecanico = mecanico
        self.Valor = valor
        self.RepuestoUtilizados = repuestos

    def GetInfo(self): 
        """Metodo que retorna la informacion detallada de la reparacion"""      
        return f"INFO REPARACION: AUTO REPARADO: {self.AutoAsignado.GetInfo()}, MECANICO ASIGNADO: {self.Mecanico.GetInfo()}, VALOR: ${self.Valor}"

    def CambiarColorAuto(self, color):
        self.AutoAsignado.CambiarColor(color)


class MenuPrincipal:

    def MostrarMenu():
        print("Bienvenido al Sistema de Reparacion Mi Taller Mecanico")
        print("-------------------------------------------------------")
        print(" ")
        print("Seleccione una Opcion:")


        print("OPCION 1: Ingresar un Vehiculo")
        print("OPCION 2: Ingresar un Mecanico")
        print("OPCION 3: Generar una Reparacion")


        print("OPCION 4: Ver Autos")
        print("OPCION 5: Ver Mecanicos")
        print("OPCION 6: Ver Reparaciones")

        print("OPCION 7: Editar Auto")
        print("OPCION 8: Eliminar Auto")


        print("Escriba Salir para terminar")
        print(" ")


    def LimpiarConsola():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

