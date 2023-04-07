# Desarrollar un programa completo en Python, que a traves de un menú de opciones, ejecute los siguientes puntos:

# 1) Ingresar una secuencia de números, la carga termina cuando el usuario ingrese el numero 0, determinar el acumulado
# total de todos los números que estén entre los valores 15 y 25, ademas determine cual es la cantidad de números pares
# que se ingresaron. Por ultimo muestre y determine el promedio que se obtiene entre los valores acumulados entre 15 y
# 25 y la cantidad total de números procesados para ese rango

# 2) Ingrese  cantidad de toneladas de granos que tres provincias produjeron, calcule el promedio de granos producidos.
# Luego determine cuantos de esas cantidades superan al promedio.

# 3) Terminar el Programa
menu = "Seleccione la Opción Deseada: \n " \
       "1. Secuencia de Números \n " \
       "2. Producción de Granos \n " \
       "3. Fin \n " \
       "Opción deseada: "
opcion = 4

while opcion != 3:
    while opcion > 3 or opcion < 1:
        opcion = int(input(menu))
        if opcion > 3 or opcion < 1:
            print("Error... esa opción no es válida!")

    if opcion == 1:
        # Datos
        num = int(input("Ingrese su primer número (para finalizar ingrese 0): "))
        acu_15_25 = 0
        con_15_25 = 0
        pares = 0

        # Proceso
        while num != 0:
            if 14 < num < 26:
                acu_15_25 += num
                con_15_25 += 1
            if num % 2 == 0:
                pares += 1
            num = int(input("Ingrese su primer número (para finalizar ingrese 0): "))
        promedio = 0
        if con_15_25 > 0:
            promedio = round(acu_15_25/con_15_25, 2)

        # Resultados
        print("El acumulado total de todos los números 15 y 25 fue: ", acu_15_25)
        print("El promedio de estos fue: ", promedio)
        print("La cantidad de números pares fue: ", pares)

        # Reset
        opcion = 4

    elif opcion == 2:
        prov1 = float(input("Ingrese la cantidad de toneladas de granos producidos de la provincia 1: "))
        prov2 = float(input("Ingrese la cantidad de toneladas de granos producidos de la provincia 2: "))
        prov3 = float(input("Ingrese la cantidad de toneladas de granos producidos de la provincia 3: "))
        sup_prom = 0

        promedio = round((prov1+prov2+prov3)/3, 2)
        if prov1 > promedio:
            sup_prom += 1
        if prov2 > promedio:
            sup_prom += 1
        if prov3 > promedio:
            sup_prom += 1

        print("El promedio fue de: ", promedio)
        print("La cantidad de provincias con producción mayor al promedio fue de: ", sup_prom)

        # Reset
        opcion = 4

print("Programa Terminado!")
