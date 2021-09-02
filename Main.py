from Clases import Botella

#Intancia
miBotella = Botella()
miBotella.capacidadMaxima = 1000
miBotella.color = "Plateado" #Set el atributo
#print("Mi botella es de color: ", miBotella.color) #Get el atributo

botellaJuanito = Botella()
botellaJuanito.capacidadMaxima = 500
botellaJuanito.color = "Blanco"

print(miBotella.capacidadActual)
print(miBotella.rellenarBotella(1100))
print(miBotella.capacidadActual)

print(botellaJuanito.rellenarBotella(500))
print(botellaJuanito.capacidadActual)



#print(miBotella) #<Clases.Botella object at 0x000001F3D0210520>
#print(botellaJuanito) #<Clases.Botella object at 0x000001F3D021AA90>