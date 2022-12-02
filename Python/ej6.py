class Vehiculo:
    color='Rojo'
    ruedas='4'
    puertas='2'
    
class Coche(Vehiculo):
    velocidad='120 km/h'
    Cilindada=2500
    
    def __str__(self):
        print ('CARACTERISTICAS DEL COCHE:\n  Color: ', self.color ,'\n  Ruedas:',self.ruedas,'\n  Puertas:',self.puertas ,'\n  Velocidad:',self.velocidad, '\n  Cilindrada:',self.Cilindada)
        return ''
micoche = Coche()
print(micoche)