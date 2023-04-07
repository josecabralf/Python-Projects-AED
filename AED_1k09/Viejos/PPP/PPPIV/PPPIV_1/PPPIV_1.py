"""
Desarrollar un programa que permita generar el extracto del sorteo del Quini 6.
El programa debe tener las siguientes opciones:

1) Cargar sorteo: cargar por teclado los 6 números sorteados. Los valores posibles van del 0 al 36,
ambos inclusive (validar). Grabarlos el archivo extracto.dat, ordenados de forma ascendente.

2) Consultar: mostrar el contenido del archivo extracto.dat.
"""
import os
import pickle
import random


def test():
    op = -1
    existe = False

    while op != 3:
        print("MENU DE OPCIONES:\n1- Cargar \n2- Consultar \n3- Salir")
        op = int(input("Seleccione Op:"))

        if op == 1:
            nros = [0] * 6
            for i in range(len(nros)):
                nros[i] = random.randint(0, 36)

            archivo = open("extracto.dat", "wb")
            existe = True
            for i in range(len(nros)):
                pickle.dump(nros[i], archivo)

            archivo.close()
            print("Archivo generado")

        elif op == 2:
            if existe:
                archivo = open("extracto.dat", "rb")
                for i in range(6):
                    print(pickle.load(archivo))


if __name__ == "__main__":
    test()
