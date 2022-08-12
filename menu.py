
sw = 1

while sw == 1:
    print("BIENVENIDOS A SISTEMA DE ENTRADAS")
    print("1. COMPRAR ENTRADAS")
    print("2. OPCION SIN CONSTRUIR")
    print("3. SALIR")
    try:
            op = int(input("Seleccion una opción\n"))
            if op == 1:
                print("COMPRAR ENTRADAS")
               
                
               
            if op == 2:
                print("opcion2")
            if op == 3:
                print("Muchas gracias por visitarnos")
                sw = 0

    except :
            print("Oops!  Este sistema acepta solo numeros...")