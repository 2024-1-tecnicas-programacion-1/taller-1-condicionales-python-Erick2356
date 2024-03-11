def evaluar(num_victorias_a, num_victorias_b):
    if num_victorias_a < 0 or num_victorias_a > 7 or num_victorias_b < 0 or num_victorias_b > 7:
        return "El valor es inválido"
    elif num_victorias_a >= 6 and num_victorias_a - num_victorias_b >= 2:
        return "Ganó A"
    elif num_victorias_b >= 6 and num_victorias_b - num_victorias_a >= 2:
        return "Ganó B"
    else:
        return "El juego aún no ha terminado"
    
if __name__ == '__main__':
    print("Los juegos ganados por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganados por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
