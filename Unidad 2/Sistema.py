from Model.Clases import *
from ConexionMySql import DAO

dao = DAO()
mP = MenuPrincipal()

while True:
    mP.LimpiarConsola()
    mP.MostrarMenu()

    oP = str(input(" : "))

    if oP == "1":
        mP.LimpiarConsola()
        mP.MenuSecundario("Cliente")
        oP = str(input(" : "))

        if oP == "1":
            #Insertar data Cliente a la Base de Datos
            mP.LimpiarConsola()
            print("======= Agregando Cliente =======")
            print("Complete la Informacion Solicitada:")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))

            C = Cliente(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)

            dao.InsertarCliente(C)

            mP.ConfirmacionIngreso("Cliente")