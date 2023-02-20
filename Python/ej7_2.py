import time
import calcSalida

def main():
    segundos = time.time();
    dat = time.localtime(segundos);
    print(calcSalida.horaSalida(dat.tm_hour,dat.tm_min))

if __name__ == '__main__':
    main();