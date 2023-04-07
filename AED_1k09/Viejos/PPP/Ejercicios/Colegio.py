"""
En un colegio secundario se maneja la información de las notas de una materia con tres vectores de longitud n, llamados
trim1, trim2 y trim3. Esos vectores almacenan las notas correspondientes a cada trimestre para cada alumno. Asimismo se
mantienen los nombres de los alumnos en otro vector paralelo a los de las notas.

Se necesita un programa que permita ingresar todos esos datos y que luego de la carga genere un cuarto vector que
contenga el promedio de cada alumno. Finalmente el programa debe mostrar todos los datos de los tres alumnos con mejor
promedio de la materia.
"""
import random


def ordenar_descendente(nombres, trim1, trim2, trim3, promedios):
    n = len(nombres)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if promedios[i] < promedios[j]:
                nombres[i], nombres[j] = nombres[j], nombres[i]
                trim1[i], trim1[j] = trim1[j], trim1[i]
                trim2[i], trim2[j] = trim2[j], trim2[i]
                trim3[i], trim3[j] = trim3[j], trim3[i]
                promedios[i], promedios[j] = promedios[j], promedios[i]


def cargar_datos_automatico(alumnos, trim1, trim2, trim3):
    n = len(alumnos)
    for i in range(n):
        alumnos[i] = "Alumno" + str(i)
        trim1[i] = random.randint(1, 10)
        trim2[i] = random.randint(1, 10)
        trim3[i] = random.randint(1, 10)


def calc_promedio(prom, trim1, trim2, trim3):
    n = len(prom)
    for i in range(n):
        prom[i] = round((trim1[i] + trim2[i] + trim3[i]) / 3, 2)


def mostrar(alumnos, promedio, cantidad):
    print("MEJORES ALUMNOS:")
    for i in range(cantidad):
        print(alumnos[i], promedio[i], sep='\t\t')


def test():
    # Una nota por alumno
    n = int(input("Ingrese el número de alumnos: "))

    # Crear Vectores
    alumnos = [""] * n
    trim1 = [0] * n
    trim2 = [0] * n
    trim3 = [0] * n

    # Cargar Datos
    cargar_datos_automatico(alumnos, trim1, trim2, trim3)

    # Generar promedio
    promedio = [0] * n
    calc_promedio(promedio, trim1, trim2, trim3)
    ordenar_descendente(alumnos, trim1, trim2, trim3, promedio)

    # Mostrar Datos
    mostrar(alumnos, promedio, 3)


if __name__ == "__main__":
    test()
