from Clases import *

#Simular nuestras tablas de la Base de Datos

listaAutos = []

listaMecs = []

listaReps = []

def insertarDatosTesting():
    A = Auto('GHFG23','GTSFDRSF343434','ROJO', 'KIA','RIO 5', 2013)
    A2 = Auto('WESD17','HSTDGDRSF34332','BLANCO', 'NISSAN','TERRANO', 2010)
    A3 = Auto('HTDG22','IKYUHHFTDG2323','GRIS', 'MAZDA','CX 5', 2020)
    listaAutos.append(A)
    listaAutos.append(A2)
    listaAutos.append(A3)

    M = Mecanico('1.123.123-1','ALEXIS', 'SANCHEZ', 35, 'CURICO')
    M2 = Mecanico('2.123.123-1','ARTURO', 'VIDAL', 30, 'MOLINA')
    M3 = Mecanico('3.123.123-1','GARY', 'MEDEL', 40, 'TENO')
    listaMecs.append(M)
    listaMecs.append(M2)
    listaMecs.append(M3)

insertarDatosTesting()

while True:
    MenuPrincipal.LimpiarConsola()
    MenuPrincipal.MostrarMenu()

    opcionSeleccionada = input(' : ')


    if opcionSeleccionada == "7":
        i = 1
        for A in listaAutos:
            print(f"OPCION {i} : {A.GetInfo()}")
            i += 1
        print(' ')
        opcion = int(input("Seleccione el Auto a Editar: "))

        #Modificamos el Atributo Deseado
        listaAutos[opcion -1].setPatente(input("Ingrese Nueva Patente: "))
        print(" ")
        input("Auto Editado con Exito! Presione Enter para Continuar... ")

    if opcionSeleccionada == "8":
        i = 1
        for A in listaAutos:
            print(f"OPCION {i} : {A.GetInfo()}")
            i += 1
        print(' ')
        opcion = int(input("Seleccione el Auto a Eliminar: "))

        #Modificamos el Atributo Deseado
        listaAutos.remove(listaAutos[opcion-1])
        print(" ")
        input("Auto Eliminado con Exito! Presione Enter para Continuar... ")



    if opcionSeleccionada == "3":
        MenuPrincipal.LimpiarConsola()
        print("------ Opcion Seleccionada Ingresar Reparacion! ------------")
        print(' ')

        #Logica para Seleccionar Auto
        i = 1
        for A in listaAutos:
            print(f"OPCION {i} : {A.GetInfo()}")
            i += 1
        print(' ')
        opcion = int(input("Seleccione el Auto a Reparar: "))
        autoSeleccionado = listaAutos[opcion - 1]

        #Logica para Seleccionar Mecanico
        i = 1
        for A in listaMecs:
            print(f"OPCION {i} : {A.GetInfo()}")
            i += 1
        print(' ')
        opcion = int(input("Seleccione el Mecanico Asignado: "))
        mecanicoSeleccionado = listaMecs[opcion - 1]

        valorRep = input("Ingrese Costo de la Reparacion: ")
        repuesto = input("Ingrese Repuesto Utilizado en la Reparacion: ")

        #Crear Instancia Reparacion
        Rep = Reparacion(autoSeleccionado,mecanicoSeleccionado,valorRep,repuesto)

        #Insertamos en la Base de Datos (LISTA)
        listaReps.append(Rep)

        input("Reparacion Ingresada con Exito! Presione Enter para Continuar... ")


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
            print(' ')

        print(" ")
        input("Autos Listados! Presione Enter para Continuar... ")

    if opcionSeleccionada == "5":
        MenuPrincipal.LimpiarConsola()
        print("------Opcion Seleccionada Ver Mecanicos!------------")
        print(' ')

        for M in listaMecs:
            print(M.GetInfo())
            print(' ')

        print(" ")
        input("Mecanicos Listados! Presione Enter para Continuar... ")

    if opcionSeleccionada == "6":
        MenuPrincipal.LimpiarConsola()
        print("------Opcion Seleccionada Ver Reparaciones!------------")
        print(' ')

        for M in listaReps:
            print(M.GetInfo())
            print(' ')

        print(" ")
        input("Reparaciones Listadas! Presione Enter para Continuar... ")


    if opcionSeleccionada == "Salir":
        print("Saliendo...")
        break