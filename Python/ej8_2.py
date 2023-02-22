import pickle
class Vehiculo:
    color=''
    marca=''
    tipo=''
    precio=0.0
    
    def __init__(self,color,marca,tipo,precio):
        self.color = color
        self.marca = marca
        self.tipo = tipo
        self.precio = precio
        
    def __str__(self):
        return f'{self.marca} {self.color} {self.tipo} {self.precio}'
        
v1 = Vehiculo('Azul','lamborgini','deportivo',1300000)
f = open('vehiculo.txt','w+b')
pickle.dump(v1,f)
f.close()

# Abrir archivo y leerlo

fichero = open('vehiculo.txt','r+b')
datos = pickle.load(fichero)
fichero.close()
print(datos)