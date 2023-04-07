# Desarrollar un programa completo en Python, que a través de un menu de opciones, ejecute los siguientes puntos:

# 1) Ingresar el nombre de tres atletas, ademas ingrese también los tiempos que esos lograron en su actividad deportiva
# (expresados en segundos), informe cual fue el nombre del atleta que gano la competición, ademas indicar con un mensaje
# que si el tiempo del ganador es menor a 850 segundos batió el record de la actividad

# 2) Ingresar un texto, el mismo termina con punto, recorrer el texto caracter a caracter y determinar cuantas letras 'p'
# hay en el texto, cuantas letras 'j' hay en el texto. Ademas indique cual es el porcentaje que cada conteo representa
# sobre el total de caracteres del texto.

# 3) Terminar el Programa

menu = "\nSeleccione una opción:\n " \
       "1. Atleta ganador \n " \
       "2. Procesamiento de texto\n " \
       "3. Terminar"
# Forzar ¨(1,n)
opcion = 4

while opcion != 3:

    # Mecanismo de control
    while opcion > 3 or opcion < 1:
        print(menu)
        opcion = int(input("Opción elegida:"))
        if opcion > 3 or opcion < 1:
            print("Error... esa opción no es válida")

    if opcion == 1:
        nom = None
        tg = None
        record = False

        for i in range(1, 4):
            nom = input("Ingrese el nombre del atleta " + str(i) + ": ")
            tiempo = int(input("Ingrese el tiempo logrado por el atleta (en segundos): "))

            if i == 1:
                ganador = nom
                tg = tiempo

            if tiempo < tg:
                ganador = nom
                tg = tiempo

            if tg < 850:
                record = True

        print("El ganador fue:", nom)
        if record:
            print("El ganador batió el record!")

        # Reset
        opcion = 4

    elif opcion == 2:
        texto = input("Ingrese un texto (recuerde terminar con un punto): ")
        cont_car = 0
        cont_p = 0
        cont_j = 0

        if texto[-1] != ".":
            texto += "."

        for car in texto:
            cont_car += 1
            if car == "p" or car == "P":
                cont_p += 1
            elif car == "j" or car == "J":
                cont_j += 1

        porcentaje = round((cont_p/cont_car)*100, 2)
        print("El total de letras 'p' fue: ", cont_p)
        print("Representando un", porcentaje, "% del total de caracteres")

        porcentaje = round((cont_j/cont_car)*100, 2)
        print("El total de letras 'j' fue: ", cont_j)
        print("Representando un", porcentaje, "% del total de caracteres")
        # Reset
        opcion = 4
