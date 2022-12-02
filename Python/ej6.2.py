class Alumno:
    nombre= None
    nota = None
    
    def __init__(self,nombre):
        self.nombre=nombre
    
    def colocarNota(self):
        nota=input('digite la nota del Alumno (1-10):')
        nota = int(nota)
        self.nota = nota
        
    def aprobo(self):
        if self.nota > 5:
            return 'el Alumno Aprobo !! felicidades !!!'
        return 'el alumno No Aprobo =('
    
    def __str__(self):
        print ('Alumno:  ',self.nombre ,'\nNota:  ',self.nota,'\n',self.aprobo())
        return ''
    
alumno = Alumno(input('Nombre del Alumno:'))
alumno.colocarNota()
print(alumno)
        