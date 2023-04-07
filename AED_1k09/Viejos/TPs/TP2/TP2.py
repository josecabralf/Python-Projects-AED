import random


# Validar mayor que inf
def mayor_que(inf):
    n = inf
    while n <= inf:
        n = int(input("Ingrese un número mayor a " + str(inf) + ": "))
        if n <= inf:
            print("No es válido, debe ser mayor a " + str(inf))
    return n


# Eleeción del Jugador: Par o Impar?
def choice():
    n = 0
    while n < 1 or n > 2:
        n = int(input("La suma de dados será: \n1)Par  \n2)Impar \nIngrese su apuesta: "))
        if n < 1 or n > 2:
            print("\nValor no válido\n")
    return n


# Tirada de dados
def roll():
    dados = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
    return dados


# Definir paridad de dados o su suma
def paridad(x):
    if x % 2 == 0:
        return True
    else:
        return False


# Realizar un Turno
def turno(eleccion):

    # Tirada de Dados
    dados = roll()
    print("El valor de sus dados fue: ", dados)

    # Acumulador de puntos de turno
    pt_parcial = 0

    # Eleccion de Jugador == Par
    if eleccion == 1:

        # Sumatoria Par?
        if paridad(dados[0]+dados[1]+dados[2]):
            pt_parcial += max(dados)

            # Todos los dados Pares?
            if paridad(dados[0]) and paridad(dados[1]) and paridad(dados[2]):
                pt_parcial *= 2
        # No
        else:
            pt_parcial -= min(dados)

    # Eleccion de Jugador == Impar
    else:
        # Sumatoria Impar?
        if not paridad(dados[0]+dados[1]+dados[2]):
            pt_parcial += max(dados)

            # Todos los dados Impares?
            if not paridad(dados[0]) and not paridad(dados[1]) and not paridad(dados[2]):
                pt_parcial *= 2

        # No
        else:
            pt_parcial -= min(dados)

    print("Usted ha obtenido:", pt_parcial, "puntos esta ronda")

    # Devolver el puntaje obtenido en el Turno
    return pt_parcial


# Definir el mayor entre puntaje/aciertos
def ganador(n1, n2):
    # Ganador J1
    if n1 > n2:
        res = 1
    # Ganador J2
    elif n2 > n1:
        res = 2
    # Empate
    else:
        res = 3

    return res


# Promedio
def promedio(suma, cantidad):
    prom = round(suma / cantidad, 2)
    return prom


# Función del Programa
def test():
    print("Bienvenidos al Juego de Dados 2.0 \n")

    # Nombres
    j1 = input("Ingrese el Nombre de Jugador 1: ")
    j2 = input("Ingrese el Nombre de Jugador 2: ")

    # Puntaje Ganador
    print("\nSeleccione un puntaje Ganador")
    pt_win = mayor_que(10)

    # Iniciador de Puntajes
    pt_j1 = 0
    pt_j2 = 0

    # Iniciador de Ronda
    ronda = 0

    # Flag: Empate?
    empate = False

    # Rondas consecutivas: Flag, contador y ganador anterior
    consec = False
    rond_consec = 0
    winner_ant = None

    # Contadores de Aciertos y de Rondas Ganadas
    aciertos_j1 = 0
    aciertos_j2 = 0
    ganadas_j1 = 0
    ganadas_j2 = 0

    # Ciclo de Rondas
    while pt_j1 < pt_win and pt_j2 < pt_win:

        # Cuento Ronda
        ronda += 1

        # Turno J1:
        print("\nTurno de", j1)
        eleccion = choice()
        pt_parcial_j1 = turno(eleccion)

        # Si obtiene más de 0 pts significa que acertó
        if pt_parcial_j1 > 0:
            aciertos_j1 += 1

        # Turno J2
        print("\nTurno de", j2)
        eleccion = choice()
        pt_parcial_j2 = turno(eleccion)

        # Si obtiene más de 0 pts significa que acertó
        if pt_parcial_j2 > 0:
            aciertos_j2 += 1

        # Definir ganador de ronda
        winner = ganador(pt_parcial_j1, pt_parcial_j2)

        if winner == 1:
            ganadas_j1 += 1

        elif winner == 2:
            ganadas_j2 += 1

        #  Hubo Empates?
        else:
            empate = True

        # Rondas consecutivas: winner != 3 para que no cuente empates
        if winner == winner_ant and winner != 3:
            rond_consec += 1
            if rond_consec >= 3:
                consec = True
        else:
            # rond_consec = 1 porque ganó esta ronda
            rond_consec = 1

        # Ganador de Ronda Anterior
        winner_ant = winner

        # Acumular puntos de Ronda en los Puntos Totales
        pt_j1 += pt_parcial_j1
        pt_j2 += pt_parcial_j2

        print("\nPuntajes Totales:")
        print(j1 + ":" + str(pt_j1))
        print(j2 + ":" + str(pt_j2))

    # Fin del Juego
    print("Fin del Juego")

    # Definir Ganador del Juego
    winner = ganador(pt_j1, pt_j2)
    # Ganador J1
    if winner == 1:
        print("El ganador fue:", j1)
    # Ganador J2
    elif winner == 2:
        print("El ganador fue:", j2)
    else:
        # Empate = Gana el que más rondas ganó
        winner = ganador(ganadas_j1, ganadas_j2)
        if winner == 1:
            print("El ganador fue:", j1)
        elif winner == 2:
            print("El ganador fue:", j2)
        # Empate de rondas ganadas = Empate
        else:
            print("No hubo ganador: Fue un Empate")

    # Estadisticas
    print("\nEstadiscas:")

    # Cantidad de Rondas
    print("\nRondas jugadas:", ronda)

    # Empates?
    if empate:
        print("\nHubo al menos una ronda empatada")

    # Puntajes promedio por Ronda
    print("\nPuntajes promedios por Ronda:")
    print(j1 + ":" + str(promedio(pt_j1, ronda)))
    print(j2 + ":" + str(promedio(pt_j2, ronda)))

    # Porcentajes de Aciertos
    print("\nPorcentajes de Acierto:")
    print(j1 + ":" + str(promedio(aciertos_j1, ronda) * 100) + "%")
    print(j2 + ":" + str(promedio(aciertos_j2, ronda) * 100) + "%")

    aciertos = ganador(aciertos_j1, aciertos_j2)

    if aciertos == winner:
        print("\nEl Jugador ganador fue el que tuvo más aciertos")

    # 3 Consecutivas?
    if consec:
        print("\nUn jugador ganó al menos 3 rondas consecutivas")


# Ejecución del Programa
test()
