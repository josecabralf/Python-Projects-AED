"""
Una franquicia veterinaria quiere llevar un control de las prácticas realizadas en las distintas sucursales de la
cadena. Para lo cual solicita un programa que:

1- Ingrese por teclado los datos de las prácticas realizadas. De cada práctica se conoce: tipo de práctica (0-9),
sucursal (0-5), importe cobrado.

2- Determine el monto recaudado por cada sucursal

3- Determine cual fue la práctica que mas frecuentemente se realiza

4- Determinar la cantidad de veces que se realizó cada práctica en cada sucursal.
"""
import random


def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    valor = int(input(mensaje))
    while valor < inf:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


def validar_entre(inf, sup, mensaje):
    valor = int(input(mensaje))
    while valor < inf or valor > sup:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor


def cargar_practica_manual(n):
    tipo = sucursal = importe = [] * n
    for i in range(n):
        tipo[i] = validar_mayor_que(0, "Ingrese el tipo de práctica: ")
        sucursal[i] = validar_mayor_que(0, "Ingrese el nro de sucursal: ")
        importe[i] = validar_mayor_que(0, "Ingrese el importe cobrado")
    return tipo, sucursal, importe


def carga_automatica(n):
    tipo = [0] * n
    sucursal = [0] * n
    importe = [0] * n
    for i in range(n):
        tipo[i] = random.randint(0, 9)
        sucursal[i] = random.randint(0, 5)
        importe[i] = random.randint(0, 100)
    return tipo, sucursal, importe


def monto_sucursal(sucursal, importe):
    acu = [0] * 6
    for i in range(len(acu)):
        for j in range(len(sucursal)):
            if i == sucursal[j]:
                acu[i] += importe[j]
    return acu


def cont_practica(tipo):
    contador = [0] * 10
    for i in range(len(contador)):
        for j in range(len(tipo)):
            if i == tipo[j]:
                contador[i] += 1
    return contador


def mayor(contador):
    may = contador[0]
    pos = 0
    for i in range(1, len(contador)):
        if may < contador[i]:
            may = contador[i]
            pos = i
    return pos


def conteo_suc_practicas(n, practicas, sucursales):
    mat = [[0] * 10 for _ in range(6)]
    for i in range(n):
        fila = sucursales[i]
        columna = practicas[i]
        mat[fila][columna] += 1
    return mat


def test():
    n = validar_mayor_que(0, "Ingrese la cantidad de prácticas realizadas: ")

    op = validar_entre(1, 2, "Elija tipo de carga: 1) Manual - 2) Automatica: ")
    if op == 1:
        tipo, sucursal, importe = cargar_practica_manual(n)
    else:
        tipo, sucursal, importe = carga_automatica(n)

    # Monto por sucursal
    acumulador = monto_sucursal(sucursal, importe)
    print("\nMONTO RECAUDADO POR SUCURSAL:")
    print(acumulador)

    # Practica más realizada
    contador = cont_practica(tipo)
    practica_may = mayor(contador)
    print("\nPRACTICA MÁS REALIZADA:")
    print(practica_may)

    # Cada practica en cada sucursal
    mat = conteo_suc_practicas(n, tipo, sucursal)
    print("\nPRACTICAS REALIZADAS POR SUCURSAL:")
    for i in range(6):
        print("Sucursal", str(i), ":", str(mat[i]))


if __name__ == "__main__":
    test()
