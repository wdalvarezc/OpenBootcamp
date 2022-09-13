public class Tarea2 {
    public static void main(String[] args) {

        // Parte 1 sentencia if

        int numeroIf = -10;

        if (numeroIf < 0) {
            System.out.println("el numero es negativo");
        } else if (numeroIf == 0) {
            System.out.println("el numero es 0");
        } else if (numeroIf > 0) {
            System.out.println("el numero es positivo");
        }

        // Parte 2 sentencia while
        int numeroWhile = -5;

        while (numeroWhile < 3) {
            System.out.println(numeroWhile);
            numeroWhile++;
        }
        // Parte 3 sentencia do while
        do {
            System.out.println(numeroWhile);
            numeroWhile++;
        } while (numeroWhile < 3);

        // Parte 4 sentencia For
        int numeroFor = 0;
        for (; numeroFor <= 3; numeroFor++) {
            System.out.println(numeroFor);
        }

        // Parte 5 Sentencia Switch

        String estacion = "Verano";

        switch (estacion) {
            case "Invierno":
                System.out.println("la estacion actual es Invierno");
                break;
            case "Verano":
                System.out.println("la estacion actual es Verano");
                break;
            case "Primavera":
                System.out.println("la estacion actual es Primavera");
                break;
            case "Otoño":
                System.out.println("la estacion actual es Otoño");
                break;
            default:
            System.out.println("la estacion no existe");
                break;
        }
    }
}
