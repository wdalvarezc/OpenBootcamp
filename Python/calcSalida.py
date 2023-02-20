def horaSalida(hora, min):
    if hora < 19:
        return f'falta {18 - hora} horas y {60-min} minutos para ir a casa'
    else:
        return 'ya es hora de ir a casa'