"""
Se tiene un conjunto de números de forma que cada número puede venir repetido varias veces, y se desea un
programa que cuente cuántas veces apareció cada número (en este desafío, el conjunto de entrada estará dado por un
arreglo de números que los alumnos deberán crear con funciones provistas por la Cátedra). Aunque no se sabe cuántos
números diferentes vendrán, es posible que se conozca la cantidad total de números n que entrarán, y en algunas
ocasiones se sabe también si esos números están en algún rango conocido.

En esta primera consigna, suponga que sabemos la cantidad total n de números que tiene el arreglo de entrada, pero no
sabemos en qué rango vienen esos números (por ejemplo, podemos saber que vendrán n = 1000 números, pero no sabemos si
esos números están entre 1 y 1000 o entre 1 y 100000... o en ningún intervalo conocido de antemano). Para esta primera
consigna, el problema consiste en determinar cuántos números diferentes entraron (aunque saber cuántas veces entró cada
uno también será necesario para las consignas 2 y 3).

En general, es obvio que para llevar esa cuenta necesitamos un contador por cada número diferente que se detecte
(no sabemos cuántos números diferentes vendrán, pero sí que cada uno que venga puede entrar varias veces)  ¿Cuántos
contadores necesitaremos, si no sabemos la cantidad de números distintos? Un rápido análisis sugiere que podrían usarse
dos arreglos unidimensionales paralelos num y cont, de forma que en cada componente num[i] se guarde el número que nos
interesa controlar y en el componente cont[i] se proceda a contar cuántas veces fue visto el número guardado en num[i].
El algoritmo general podría ser el siguiente:

0.)  Cree los dos arreglos num y cont inicialmente vacíos (sin casilleros).
1.)  Para cada número x del arreglo de entrada:
      1.1) Buscar x en el arreglo num y determinar el índice i de la casilla donde está almacenado.
      1.2) ¿Existe x en el arreglo num (o sea: el valor de i es diferente de -1)?
          Sí:  Sumar l al casillero cont[i].
          No:  Agregar al final del arreglo num el número x, y agregar un 1 al final del arreglo cont.
2.)  Mostrar el tamaño final del arreglo num (para saber cuántos numeros diferentes aparecieron).

Para cumplir con esta primera consigna, se provee un módulo Aaaaa.py (que puede descargar haciendo click en el nombre
del módulo o también haciendo click aquí) ya programado por los docentes de la Cátedra, conteniendo un par de funciones
que los estudiantes obligatoriamente deberán usar para generar los arreglos que servirán como datos para las consignas
de este desafío.

Su tarea:
a.) Cree un proyecto nuevo en PyCharm para desarrollar los programas que necesitará en este desafío.
b.) Descargue y descomprima el archivo Aaaaa.py provisto por la Cátedra, e inclúyalo en el proyecto que acaba de
crear.
c.) Cree un programa dentro del proyecto, e importe el módulo Aaaaa.py en ese programa.
d.) Su programa debe usar la función soporte.vector_unknown_range() para crear y obtener el arreglo que debe procesar.
El arreglo debe generarse con n = 300000 (trescientos mil) elementos, y la instrucción que le permitiría hacerlo es
simplemente la siguiente: v = soporte.vector_unknown_range(300000)
e.) La instrucción anterior, asignará en v una referencia a un arreglo con n = 300000 números mayores o iguales a 0,
que pueden venir repetidos, pero de forma que se desconoce en qué intervalo o rango están. La invocación
v = soporte.vector_unknown_range(300000) creará exactamente el mismo arreglo cada vez que la ejecute, por lo que no debe
preocuparse: sus datos serán siempre los mismos, siempre y cuando el parámetro sea 300000. Con otros valores de ese
parámetro, el arreglo generado será diferente: asegúrese de invocar a la función pasando el valor 300000 como parámetro.
f.) En el mismo programa, implemente el algoritmo de conteo descripto en el pseudocódigo de más arriba, usando un
arreglo de registros de conteo, y obtenga como primera medida, la cantidad de números diferentes que detecte en el
arreglo v de entrada.
"""
import soporte


def linear_search(v, x):
    r = -1
    for i in range(len(v)):
        if x == v[i]:
            r = i

    return r


def creacion(v, num, cont):
    for i in range(len(v)):
        if v[i] not in num:
            num.append(v[i])
            cont.append(1)
        else:
            n = linear_search(num, v[i])
            cont[n] += 1


def buscar_mayor(v):
    mayor = v[0]
    pos = 0
    for i in range(1, len(v)):
        if v[i] > mayor:
            mayor = v[i]
            pos = i
    return pos


def test():
    v = soporte.vector_unknown_range(300000)
    num = []
    cont = []
    creacion(v, num, cont)

    tam = len(num)
    print("El tamaño es:", tam)
    print(num)

    pos = buscar_mayor(cont)
    print("Moda:", str(num[pos]))
    print("Frecuencia:", str(cont[pos]))


if __name__ == "__main__":
    test()
