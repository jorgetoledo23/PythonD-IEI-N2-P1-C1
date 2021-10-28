from Clases import Auto, Mecanico, Reparacion


autoUno = Auto(pat="JHDF56", nchas="HNGCTRSFDCX45", mar="KIA", model="RIO", color="ROJO")
autoDos = Auto(pat="hJgY34", nchas="JksjudHTsh234323", mar="NISSAN", model="VERSA", color="AZUL")


print(autoDos.VerInfoAuto())


mecanicoUno = Mecanico(rut="17123456-7", nom="Julio alberto", ape="roMan Riquelme", edad=35, direc="", email="")
mecanicoUno.Direccion = "Merced 512, Curico"


respuestosRep = ["Empaquetadura de Culata", "Aceite de Motor", "Sellante"]

reparacionUno = Reparacion(cod=1, auto=autoUno, mecanico=mecanicoUno, valor=380000, repuestos=respuestosRep)

reparacionUno.CambiarColorAuto("Rosado")

print(reparacionUno.VerInfoReparacion())
