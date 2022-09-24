public class tarea4 {

    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.setNombre("primercliente");
        cliente.setEdad(20);
        cliente.setTelefono(176542);
        cliente.setCredito(5.000);

        System.out.println("Nombre:  " + cliente.getNombre() + " Edad:  " + cliente.getEdad() + " Telefono:  "+ cliente.getTelefono() + " Credito: " + cliente.getCredito());

        Trabajador trabajador = new Trabajador();
        trabajador.setNombre("primerTrabajador");
        trabajador.setEdad(25);
        trabajador.setTelefono(123456);
        trabajador.setSalario(2.000);

        System.out.println("Nombre:  " + trabajador.getNombre() + " Edad:  " + trabajador.getEdad() + " Telefono:  "+ trabajador.getTelefono() + " Credito: " + trabajador.getSalario());

    }
       
}

class Persona {
    private int edad;
    private String nombre;
    private int telefono;

    public int getEdad() {
        return this.edad;
    }

    public String getNombre() {
        return this.nombre;
    }

    public int getTelefono() {
        return this.telefono;
    }

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

class Cliente extends Persona {
    private double credito;

    public double getCredito() {
        return this.credito;
    }

    public void setCredito(double credito) {
        this.credito = credito;
    }
}

class Trabajador extends Persona {
    private double salario;

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public double getSalario() {
        return this.salario;
    }
}
