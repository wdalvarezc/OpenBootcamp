public class tarea1Pt2 {
    public static void main(String[] args) {
        Coche miCoche = new Coche();
        miCoche.agregarPuertas();
        System.out.println(miCoche.puertas);

    }

}

/**
 * creamos la clase Coche
 */
class Coche {
    // le indicamos la propiedad puertas y le damos un valor inicial de 2
    int puertas = 2;

    // creamos la accion del objeto agregarPuertas, que nos va a agregar una puerta
    // a la cantidad exixtente
    public void agregarPuertas() {
        this.puertas++;
    }

}
