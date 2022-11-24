# funcion para saber si un año es Bisiesto
def Bisiesto(a):
    if (a%4 == 0):
        return 'el año es Bisiesto'
    else:
        return 'el año No es Bisiesto'
anio = input('Digite un año: ')
print(Bisiesto(int(anio)))