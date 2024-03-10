def evaluar(anno):
    if (anno<1582 and anno % 4==0):
        print (str(anno) +  " es bisiesto")
    elif (anno>1582 and anno%400==0):
        print (str(anno) + " es bisiesto")
    else:
        print (str(anno) + " no es bisiesto")
    
    return "";

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
