# Realizar un programa completo de Python, que a través de un menu de opciones, desarrolle los siguientes items:
# 1)  Ingresar 3 temperaturas, informar la mayor y la menor temperatura. Ademas mostrar la diferencia ente la
#     mayor temperatura y la menor y por ultimo indicar el promedio de las temperaturas ingresadas
# 2)  Ingresar un cadena de caracteres, informar la cantidad de vocales que se encuentran en el texto. Ademas
#     informar el porcentajes que representan sobre el total de letras de texto
# 3)  Salir del Programa

menu = "Seleccione una opción: \n" \
       "1. Temperatura mayor y menor \n" \
       "2. Vocales en un texto \n" \
       "3. Salir \n" \
       "Seleccione la opción deseada: "

opcion = 4

while opcion != 3:
    while opcion > 3 or opcion < 1:
        opcion = int(input(menu))
        if opcion > 3 or opcion < 1:
            print("Error... esa opción no es válida! \n")

    if opcion == 1:
        t1 = float(input("\nIngrese la temperatura 1: "))
        t2 = float(input("Ingrese la temperatura 2: "))
        t3 = float(input("Ingrese la temperatura 3: "))

        if t1 > t2 and t1 > t3:
            mayor = t1
        elif t2 > t3:
            mayor = t2
        else:
            mayor = t3

        if t1 < t2 and t1 < t3:
            menor = t1
        elif t2 < t3:
            menor = t2
        else:
            menor = t3

        promedio = round((t1 + t2 + t3)/3, 2)

        print("La mayor temperatura fue: ", mayor, "°")
        print("La menor temperatura fue: ", menor, "°")
        print("La diferencia fue de: ", mayor - menor, "°")
        print("La temperatura promedio fue: ", promedio, "° \n")

        opcion = 4

    elif opcion == 2:
        texto = input("\nIngrese una frase: ")
        cont_letras = 0
        cont_vocal = 0
        porcentaje = 0

        for car in texto:
            cont_letras += 1
            if car in "aeiouAEIOU":
                cont_vocal += 1

        if cont_letras > 0:
            porcentaje = round((cont_vocal / cont_letras) * 100, 2)

        print("La cantidad de vocales fue: ", cont_vocal)
        print("Esto representa un ", porcentaje, "% del total de letras del texto\n")

        opcion = 4

print("\nPrograma terminado!")
