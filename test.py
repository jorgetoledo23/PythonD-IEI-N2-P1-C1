Rut = '1.123.123-0'

data = (Rut)
#DELETE FROM tbl_clientes WHERE Rut = 1.123.123-0  => MAL

data2 = (Rut,) #Forma Correcta

#DELETE FROM tbl_clientes WHERE Rut = '1.123.123-0'  => BIEN

print(data)

print(data2)





