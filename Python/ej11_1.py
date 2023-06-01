# para ver el programa funcional, debe crear una base de datos sqlite3 llamada mydb.db 
# y posteriormente crear una tabla llamada "alumnos" con la estructura de id INTEGER, nombre STRING, apellido STRING
# como ejemplo se encuentra el archivo mydb.db en este repositorio
import sqlite3

def main():
    for alumno in range(8):
        nombre = input(f'Digite nombre de alumno {alumno + 1}:\n')
        apellido = input(f'Digite nombre de alumno {alumno + 1}\n')
        creaAlumnos(alumno+1,nombre,apellido)
    alumnoBuscar = input('Digite el nombre del alumno a buscar:\n')
    verAlumno(alumnoBuscar)
        
def creaAlumnos(id,nombre,apellido):
    conn = sqlite3.connect("mydb.db")
    c = conn.cursor()
    query = ''' INSERT INTO alumnos (id,nombre,apellido) VALUES (?,?,?) '''
    c.execute(query,(id,nombre,apellido))
    conn.commit()
    conn.close()
    print('Alumno creado\n')

def verAlumno(nombre):
    conn = sqlite3.connect("mydb.db")
    c = conn.cursor()
    query = f''' SELECT * FROM alumnos WHERE nombre = "{nombre}" '''
    row = c.execute(query)
    print(row.fetchall())
    conn.close()
    
if __name__ == '__main__':
    main()
