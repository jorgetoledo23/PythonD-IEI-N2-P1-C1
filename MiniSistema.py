from Clases import *

#Simular nuestras tablas de la Base de Datos

listaAutos = []

listaMecs = []

listaReps = []



while True:
    MenuPrincipal.LimpiarConsola()
    MenuPrincipal.MostrarMenu()

    opcionSeleccionada = input(' : ')

    if opcionSeleccionada == "1":
        #Logica para Guardar Auto
        MenuPrincipal.LimpiarConsola()
        print("------Opcion Seleccionada Agregar Auto!------------")
        print(' ')

        pat = input("Ingrese Patente: ")
        chas = input("Ingrese Numero de Chasis: ")
        marca = input("Ingrese Marca: ")
        modelo = input("Ingrese Modelo: ")
        color = input("Ingrese Color: ")
        year = input("Ingrese Año: ")

        A = Auto(pat,chas,marca,modelo,color,year)

        listaAutos.append(A)

        input("Auto Ingresado con Exito! Presione Enter para Continuar... ")


    if opcionSeleccionada == "2":
        #Logica para Guardar Mecanico
        MenuPrincipal.LimpiarConsola()
        print("------Opcion Seleccionada Agregar Mecanico!------------")
        print(' ')

        rut = input("Ingrese Rut: ")
        nom = input("Ingrese Nombres: ")
        ape = input("Ingrese Apellidos: ")
        correo = input("Ingrese Correo Electronico: ")
        edad = input("Ingrese Edad: ")
        dir = input("Ingrese Direccion: ")

        M = Mecanico(rut,nom,ape,edad,dir,correo)

        listaMecs.append(M)

        input("Mecanico Ingresado con Exito! Presione Enter para Continuar... ")




    if opcionSeleccionada == "4":
        MenuPrincipal.LimpiarConsola()
        print("------Opcion Seleccionada Ver Autos!------------")
        print(' ')

        for A in listaAutos:
            print(A.GetInfo())

        print(" ")
        input("Autos Listados! Presione Enter para Continuar... ")

    if opcionSeleccionada == "5":
        MenuPrincipal.LimpiarConsola()
        print("------Opcion Seleccionada Ver Mecanicos!------------")
        print(' ')

        for M in listaMecs:
            print(M.GetInfo())

        print(" ")
        input("Mecanicos Listados! Presione Enter para Continuar... ")


    if opcionSeleccionada == "Salir":
        print("Saliendo...")
        break