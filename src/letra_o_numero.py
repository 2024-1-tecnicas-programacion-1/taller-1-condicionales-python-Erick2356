def evaluar(caracter):
    if caracter.isalpha() and caracter.isupper():
        print (" Es letra mayuscula")
    elif (caracter.isalpha()):
        print (" Es letra minúscula")
    elif (caracter.isdigit()):
        print (" Es número")
    else:
        print (" No es letra ni número")
    return "";

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
