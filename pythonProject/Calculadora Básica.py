Command = 1
while Command == 1:
    nro1 = int(input("Ingrese su primer nro:"))
    nro2 = int(input("Ingrese su segundo nro:"))
    Op = int(input("Seleccione la operación deseada: \n1.Suma \n2.Resta \n3.Multiplicación \n4.División \n"))
    result = 0
    if Op == 1:
        result = nro1 + nro2
    elif Op == 2:
        result = nro1 - nro2
    elif Op == 3:
        result = nro1 * nro2
    else:
        result = nro1 / nro2
    print("El resultado es: ", result)
    Command = int(input("Desea continuar operando sobre el resultado: \n1.Si \n2.No \n"))
    if Command == 1:
        while Command == 1:
            nro1 = result
            nro2 = int(input("Ingrese su segundo nro:"))
            Op = int(input("Seleccione la operación deseada: \n1.Suma \n2.Resta \n3.Multiplicación \n4.División"))
            if Op == 1:
                result = nro1 + nro2
            elif Op == 2:
                result = nro1 - nro2
            elif Op == 3:
                result = nro1 * nro2
            else:
                result = nro1 / nro2
            print("El resultado es: ", result)
            Command = int(input("Desea continuar operando sobre el resultado: \n1.Si \n2.No \n"))
            if Command == 2:
                print("Programa terminado!")
    else:
        print("Programa terminado!")
