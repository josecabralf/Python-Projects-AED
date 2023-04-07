# Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes opciones:

# 1.)    Ingrese por teclado las temperaturas de tres cámaras frigoríficas, tomadas durante el día, y el identificador
# o nombre de cada cámara (tres cadenas de caracteres). Informe el nombre de la cámara con la temperatura mayor, el
# nombre de la cámara con la temperatura menor, y la diferencia entre la mayor y la menor.

# 2.)    Ingrese por teclado una cadena de caracteres. Procese esa cadena a razón de un caracter por vuelta de ciclo, y
# determine cuántos de los caracteres eran letras mayúsculas. Informe también si apareció algún dígito (algún valor
# entre el '0' y el '9') en la cadena.  Y finalmente muestre cuál es el porcentaje de dígitos encontrados respecto del
# total de caracteres de la cadena.

# 3.)    Terminar el programa.

# Menu de opciones
menu = "Seleccione una opción: \n" \
       "1. Temperatura de Cámaras Frigoríficas \n" \
       "2. Mayúsculas y Dígitos (Procesamiento de texto)\n" \
       "3. Salir \n" \
       "Seleccione la opción deseada: "

# Forzar [1,N]
opcion = 4

while opcion != 3:

    # Vuelta al menu si previamente se eligió una opción != 3 (ej: opción == 1)
    opcion = 4

    # Mecanismo de control
    while opcion > 3 or opcion < 1:
        opcion = int(input(menu))
        if opcion > 3 or opcion < 1:
            print("ERROR: Esa opción no es válida.. \n")

    # Opción 1:
    if opcion == 1:
        # DATOS: Nombres y Temperaturas en tupla
        camara1 = input("\nIngrese el nombre de la camara 1: "), float(input("Ingrese la temperatura de la cámara 1: "))
        camara2 = input("Ingrese el nombre de la camara 2: "), float(input("Ingrese la temperatura de la cámara 2: "))
        camara3 = input("Ingrese el nombre de la camara 3: "), float(input("Ingrese la temperatura de la cámara 3: "))

        # PROCESO: sin usar max() y min()
        # Mayor?
        if camara1[1] > camara2[1] and camara1[1] > camara3[1]:
            mayor = camara1
        elif camara2[1] > camara3[1]:
            mayor = camara2
        else:
            mayor = camara3
        # Menor?
        if camara1[1] < camara2[1] and camara1[1] < camara3[1]:
            menor = camara1
        elif camara2[1] < camara3[1]:
            menor = camara2
        else:
            menor = camara3

        # RESULTADOS
        print("El nombre de la cámara con mayor temperatura es: ", mayor[0])
        print("El nombre de la cámara con menor temperatura es: ", menor[0])
        # Diferencia?
        print("La diferencia de temperatura fue de ", mayor[1] - menor[1], "°\n")

    # Opción 2:
    if opcion == 2:

        # DATOS

        # Cadena: DEBE TENER AL MENOS UN CARACTER
        # Forzar [1,N]
        cadena = ""
        # Ciclo de Control
        while len(cadena) < 1:
            cadena = input("\nIngrese una cadena de caracteres: ")
            if len(cadena) < 1:
                print("La cadena debe tener al menos un caracter!")

        # Inicio contador de Mayúsculas
        cont_may = 0

        # Hay dígitos?: contador, cant. de caracteres
        cont_dig = 0

        # Inicio contador caracteres
        cont_car = 0

        # PROCESO
        for car in cadena:
            cont_car += 1

            # Mayusculas?
            if "A" <= car <= "Z":
                cont_may += 1

            # Dígitos?
            if str(0) <= car <= str(9):
                cont_dig += 1

        # RESULTADOS
        print("Caracteres que fueron letras mayúsculas: ", cont_may)

        # Dígitos
        if cont_dig > 0:
            porcentaje = round((cont_dig / cont_car) * 100, 2)
            print("Hubo dígitos en la cadena y representaron un ", porcentaje, "% de los caracteres\n")
        else:
            print("No hubo dígitos en la cadena, por lo que representaron un 0% de los caracteres\n")

# Opción 3
print("\nPrograma terminado!")
