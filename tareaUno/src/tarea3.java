public class tarea3 {
    public static void main(String[] args) {
        Persona persona = new Persona();
        persona.setNombre("william");
        persona.setEdad(20);
        persona.setTelefono(456123789);
    }

}

class Persona {
    // propiedades privadas de la clase persona

    private int edad;
    private String nombre;
    private int telefono;

    // getters de las propiedades

    public int getEdad() {
        return this.edad;
    }

    public String getNombre() {
        return this.nombre;
    }

    public int getTelefono() {
        return this.telefono;
    }

    // setters de las propiedades
    public void setEdad(int edad) {
        this.edad = edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

}
