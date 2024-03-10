def evaluar(num_victorias_a, num_victorias_b):
    if num_victorias_a> num_victorias_b+2 | num_victorias_b> num_victorias_a+2 & num_victorias_a>= 6 | num_victorias_b>=6:
        print ("El juego ha terminado")
    elif num_victorias_a<6 | num_victorias_b<6:
        print ("El juego aún no ha termiado")
    elif num_victorias_a<0 | num_victorias_a>7 | num_victorias_b<0 | num_victorias_b<7:
        print ("El valor es invalido")
    
    return ""

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
