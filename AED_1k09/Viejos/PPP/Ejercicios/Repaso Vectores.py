from random import randint

__author__ = 'Algoritmos y Estructuras de Datos'
"""
Desarrollar un programa que permita procesar el puntaje obtenido por un participante en una prueba olimpica de gimnasia.
Para ellos generar un vector de 9 elementos, represeantando cada miembro del jurado. Por cada celda, generar un valor 
aleatorio entre 0 y 10 (inclusive) que indicará la puntuación recibida.
A continuacion informar:
1) Los tres mejores puntajes recibidos
2) Indicar cuantos jueces calificaron con mas de 6
3) Indicar el puntaje promedio que obtuvo la gimnasta
4) Indique cuantas veces se repitio la menor nota
5) Genere un nuevo vector, tal que no admita notas repetidas
"""


def menu():
    cadena = "\nMenu de Opciones\n" \
             "================================\n" \
             "1) Los tres mejores puntajes recibidos\n" \
             "2) Indicar cuantos jueces calificaron con mas de 6\n" \
             "3) Indicar el puntaje promedio que obtuvo la gimnasta\n" \
             "4) Indique cuantas veces se repitio la menor nota\n" \
             "5) Genere un nuevo vector, tal que no admita notas repetidas\n" \
             "6) Salir\n" \
             "Ingrese su opcion: "
    return cadena


def generar_arreglo(vector):
    for i in range(len(vector)):
        vector[i] = randint(1, 10)


def ordenar_arreglo(vector):
    tam = len(vector)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if vector[i] < vector[j]:
                vector[i], vector[j] = vector[j], vector[i]


def promedio(subtotal, total):
    prom = 0
    # Evitar n/0
    if total > 0:
        prom = round(subtotal / total, 2)

    return prom


def op_1(puntuaciones):
    for i in range(0, 3):
        print("La nota del juez" + str(i + 1) + "fue de " + str(puntuaciones[i]))


def op_2(puntuaciones):
    mas_6 = 0
    for i in range(len(puntuaciones)):
        if puntuaciones[i] > 6:
            mas_6 += 1
    print("\nLa cantidad de jueces que calificaron con mas de 6:", mas_6)


def op_3(puntuaciones):
    acu_puntuaciones = 0

    for i in range(len(puntuaciones)):
        acu_puntuaciones += puntuaciones[i]

    prom = promedio(acu_puntuaciones, len(puntuaciones))

    print("\nEl puntaje promedio que obtuvo la gimnasta fue:", prom)


def op_4(puntuaciones):
    menor = puntuaciones[-1]
    rep = 0

    for i in range(len(puntuaciones)):
        if puntuaciones[i] == menor:
            rep += 1

    print("\nLa menor nota se repitió:", rep, "veces")


def sin_repeticiones(puntuaciones):
    nuevo = [puntuaciones[0]]

    for i in range(1, len(puntuaciones)):
        if puntuaciones[i] != nuevo[-1]:
            nuevo.append(puntuaciones[i])

    return nuevo


def principal():
    print("Repaso Vectores")
    opcion = 0

    puntuaciones = [0] * 9
    generar_arreglo(puntuaciones)
    ordenar_arreglo(puntuaciones)
    print(puntuaciones)

    while opcion != 6:
        opcion = int(input(menu()))

        if opcion == 1:
            op_1(puntuaciones)

        elif opcion == 2:
            op_2(puntuaciones)

        elif opcion == 3:
            op_3(puntuaciones)

        elif opcion == 4:
            op_4(puntuaciones)

        elif opcion == 5:
            nuevo = sin_repeticiones(puntuaciones)
            print(nuevo)


if __name__ == '__main__':
    principal()
