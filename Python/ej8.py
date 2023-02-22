import os
def main():
    nombre = input('digite el nombre del fichero:\n')
    nombre = f'./{nombre}.txt'
    print(creaArchivo(nombre))
    while True:
        operacion = input('Digite:\n1.ver\n2.editar\n3.salir\n')
        os.system('clear')
        match operacion:
            case '1':
                print(verArchivo(nombre))
            case '2':
                print(editarArchivo(nombre))
            case _:
                break


def creaArchivo(name):
    fichero = open(name, 'x')
    fichero.close()
    return 'se creo fichero con exito !!!'


def verArchivo(name):
    f = open(name, 'r')
    r = f.read()
    f.close()
    return r

def editarArchivo(name):
    f = open(name,'w')
    datos = []
    salir = True
    while salir:
        op = input('\n1. agregar linea\n2.salir\n')
        os.system('clear')
        match op:
            case '1':
                linea = input('=>')
                datos.append(f'{linea}\n')
            case '2':
                salir=False
    f.writelines(datos)
    f.close()
    return 'Se edito el archivo exitosamente!!!'     
        
                


if __name__ == '__main__':
    main()
