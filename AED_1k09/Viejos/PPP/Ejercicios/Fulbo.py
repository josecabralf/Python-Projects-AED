from Funciones import *
import random
from Funciones_vec import *


def carga_manual(n):
    equipos = [] * n
    puntos = [0] * n
    goles = [0] * n
    for i in range(n):
        equipos[i] = input('Ingrese nombre del equipo: ')
        puntos[i] = validar_entre(0, 20, 'Ingrese puntos: ')
        goles[i] = validar_mayor_igual_que(0,'Ingrese goles: ')
    return equipos, puntos, goles


def carga_automatica(n):
    equipos = [''] * n
    puntos = [0] * n
    goles = [0] * n
    for i in range(n):
        equipos[i] = 'Equipo' + str(i)
        puntos[i] = random.randint(0,20)
        goles[i] = random.randint(0,100)
    return equipos, puntos, goles


def ordenar(equipos, puntos, goles):
    n = len(puntos)
    for i in range(n-1):
        for j in range(i+1, n):

            # Ordenar según puntos
            if puntos[i] < puntos[j]:
                equipos[i], equipos[j] = equipos[j], equipos[i]
                puntos[i], puntos[j] = puntos[j], puntos[i]
                goles[i], goles[j] = goles[j], goles[i]

            # Empate de puntos: se define x goles
            elif puntos[i] == puntos[j]:
                if goles[i] < goles[j]:
                    equipos[i], equipos[j] = equipos[j], equipos[i]
                    puntos[i], puntos[j] = puntos[j], puntos[i]
                    goles[i], goles[j] = goles[j], goles[i]


def mostrar(equipos, puntos, goles):
    print('Equipos','Puntos', 'Goles', sep='\t')
    for i in range(len(equipos)):
        print(equipos[i], puntos[i], goles[i], sep='\t\t')


# Buscar Mayores
def buscar_mayores(equipos, puntos):
    punteros = [equipos[0]]
    for i in range(1,len(puntos)):
        if puntos[i] == puntos[0]:
            punteros.append(equipos[i])
        else:
            break
    return punteros


def buscar_ultimos(v, cantidad):
    desde = len(v) - cantidad
    hasta = len(v)
    return v[desde:hasta]


def buscar_desde_goles(equipos, goles, minimo):
    buenos = list()
    for i in range(len(equipos)):
        if goles[i] > minimo:
            buenos.append(equipos[i])
    return buenos


def contar_ceros(goles, puntos):
    n = len(goles)
    contador = 0
    for i in range(n):
        if goles[i] == 0 and puntos[i] == 0:
            contador += 1
    return contador


def contar_goles_max(punteros, equipos, goles):
    ac = 0
    for team in punteros:
        for i in range(len(equipos)):
            if team == equipos[i]:
                ac += goles[i]
    return ac


def test():
    print("TORNEO DE FUTBOL")
    print("="*60)

    # Nro. de Equipos
    n = validar_mayor_que(5, "Ingrese la cantidad de equipos: ")

    # La carga debe implementarse tanto en forma manual como automática.
    carga = validar_entre(1, 2, 'Elija tipo de carga: 1) Manual - 2) Automatica: ')
    if carga == 1:
        equipos, puntos, goles = carga_manual(n)
    else:
        equipos, puntos, goles = carga_automatica(n)

    # Tabla de Posiciones
    print("\n TABLA DE POSICIONES \n")
    ordenar(equipos, puntos, goles)
    mostrar(equipos, puntos, goles)

    # Punteros
    print("\nPUNTEROS")
    punteros = buscar_mayores(equipos, puntos)
    print(punteros)

    # Descenso
    print("\nDESCENSO")
    print(buscar_ultimos(equipos,5))

    # Mejor desempeño
    print('\nMEJOR DESEMPEÑO')
    x = int(input('Ingrese cantidad minima de goles: '))
    buenos = buscar_desde_goles(equipos, goles, x)
    direct_insertion(buenos)
    print(buenos)

    # print('\nCOMPARATIVO DE GOLES')
    mostrar(equipos, puntos, goles)

    print()
    goles_punteros = contar_goles_max(punteros, equipos, goles)
    print("Total de goles para los equipos que tuvieron el máximo puntaje:", str(goles_punteros))
    print("Cantidad de equipos que no obtuvieron puntos ni marcaron goles:", str(contar_ceros(goles, puntos)))


if __name__ == "__main__":
    test()
