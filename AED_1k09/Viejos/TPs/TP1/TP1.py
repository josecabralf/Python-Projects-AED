import random

# Presentar Juego y Jugadores
print("Juego de Dados: El Juego de Dos o Tres")

jugador1 = input("\nNombre del jugador 1:")
jugador2 = input("\nNombre del jugador 2:")
puntaje_j1 = 0
puntaje_j2 = 0

# Ronda 1
print("\nComienza Ronda 1")
# DATOS
dados_j1 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
dados_j2 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

# RONDA 1 JUGADOR 1
dado1, dado2, dado3 = dados_j1
print("Los dados de", jugador1, "son: ", dados_j1)

# 3 DADOS IGUALES J1
if dado1 == dado2 == dado3:
    print("Sus dados son todos iguales")
    puntaje_j1 += 6

# 2 DADOS IGUALES J1
elif dado1 == dado2 != dado3:
    dado3 = random.randint(1, 6)
    print("Uno de sus dados es distinto")
    print("Segunda tirada del dado distinto: ", dado3)
    if dado1 == dado2 == dado3:
        print("Ahora todos son iguales")
        puntaje_j1 += 6
    else:
        print("Sigue habiendo un dado distinto")
        puntaje_j1 += 3

elif dado1 != dado2 == dado3:
    dado1 = random.randint(1, 6)
    print("Uno de sus dados es distinto")
    print("Segunda tirada del dado distinto: ", dado1)
    if dado1 == dado2 == dado3:
        print("Ahora todos son iguales")
        puntaje_j1 += 6
    else:
        print("Sigue habiendo un dado distinto")
        puntaje_j1 += 3

elif dado2 != dado1 == dado3:
    dado2 = random.randint(1, 6)
    print("Uno de sus dados es distinto")
    print("Segunda tirada del dado distinto: ", dado2)
    if dado1 == dado2 == dado3:
        print("Ahora todos son iguales")
        puntaje_j1 += 6
    else:
        print("Sigue habiendo un dado distinto")
        puntaje_j1 += 3

# 3 DADOS DIFERENTES J1
else:
    print("Todos sus dados son distintos")

print("El puntaje de", jugador1, "es: ", puntaje_j1)

# RONDA 1 JUGADOR 2
dado1, dado2, dado3 = dados_j2
print("\nLos dados de", jugador2, "son: ", dados_j2)

# 3 DADOS IGUALES J2
if dado1 == dado2 == dado3:
    print("Sus dados son todos iguales")
    puntaje_j2 += 6

# 2 DADOS IGUALES J2
elif dado1 == dado2 != dado3:
    dado3 = random.randint(1, 6)
    print("Uno de sus dados es distinto")
    print("Segunda tirada del dado distinto: ", dado3)
    if dado1 == dado2 == dado3:
        print("Ahora todos son iguales")
        puntaje_j2 += 6
    else:
        print("Sigue habiendo un dado distinto")
        puntaje_j2 += 3

elif dado1 != dado2 == dado3:
    dado1 = random.randint(1, 6)
    print("Uno de sus dados es distinto")
    print("Segunda tirada del dado distinto: ", dado1)
    if dado1 == dado2 == dado3:
        print("Ahora todos son iguales")
        puntaje_j2 += 6
    else:
        print("Sigue habiendo un dado distinto")
        puntaje_j2 += 3

elif dado2 != dado1 == dado3:
    dado2 = random.randint(1, 6)
    print("Uno de sus dados es distinto")
    print("Segunda tirada del dado distinto: ", dado2)
    if dado1 == dado2 == dado3:
        print("Ahora todos son iguales")
        puntaje_j2 += 6
    else:
        print("Sigue habiendo un dado distinto")
        puntaje_j2 += 3
        
# 3 DADOS DIFERENTES J2
else:
    print("Todos sus dados son distintos")

print("El puntaje de", jugador2, "es: ", puntaje_j2)

print("Fin de Ronda 1")

# Ronda 2
print("\nComienza Ronda 2")

# Dados Ronda 2
dados_j1 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
dados_j2 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

# Jugador 1
print("Para elegir, ingrese el número apropiado:")
print(jugador1, "elija: \n1.Par \n2.Impar")
eleccion_j1 = int(input("Elección:"))

print("\nDados de", jugador1, ":", dados_j1)
sumatoria_j1 = sum(dados_j1)

if eleccion_j1 == 1:
    if sumatoria_j1 % 2 == 0:
        print("La suma es par y usted ha acertado")
        puntaje_j1 += max(dados_j1)
        if dados_j1[0] % 2 == 0 and dados_j1[1] % 2 == 0 and dados_j1[2] % 2 == 0:
            print("Además, todos los dados son pares, por lo que se duplica su puntaje")
            puntaje_j1 *= 2
    else:
        print("Usted no ha acertado y pierde puntos")
        puntaje_j1 -= min(dados_j1)
else:
    if sumatoria_j1 % 2 == 1:
        print("La suma es impar y usted ha acertado")
        puntaje_j1 += max(dados_j1)
        if dados_j1[0] % 2 == 1 and dados_j1[1] % 2 == 1 and dados_j1[2] % 2 == 1:
            print("Además, todos los dados son impares, por lo que se duplica su puntaje")
            puntaje_j1 *= 2
    else:
        print("Usted no ha acertado y pierde puntos")
        puntaje_j1 -= min(dados_j1)

print("El puntaje de", jugador1, "es: ", puntaje_j1)

# Jugador 2
print("\nPara elegir, ingrese el número apropiado:")
print(jugador2, "elija: \n1.Par \n2.Impar")
eleccion_j2 = int(input("Elección:"))
print("\nDados de", jugador2, ":", dados_j2)
sumatoria_j2 = sum(dados_j2)

if eleccion_j2 == 1:
    if sumatoria_j2 % 2 == 0:
        print("La suma es par y usted ha acertado")
        puntaje_j2 += max(dados_j2)
        if dados_j2[0] % 2 == 0 and dados_j2[1] % 2 == 0 and dados_j2[2] % 2 == 0:
            print("Además, todos los dados son pares, por lo que se duplica su puntaje")
            puntaje_j2 *= 2
    else:
        print("Usted no ha acertado y pierde puntos")
        puntaje_j2 -= min(dados_j2)
else:
    if sumatoria_j2 % 2 == 1:
        print("La suma es impar y usted ha acertado")
        puntaje_j2 += max(dados_j2)
        if dados_j2[0] % 2 == 1 and dados_j2[1] % 2 == 1 and dados_j2[2] % 2 == 1:
            print("Además, todos los dados son impares, por lo que se duplica su puntaje")
            puntaje_j2 *= 2
    else:
        print("Usted no ha acertado y pierde puntos")
        puntaje_j2 -= min(dados_j2)

print("El puntaje de", jugador2, "es: ", puntaje_j2)

print("Fin de Ronda 2")
# Fin Ronda 2

# Comparación de puntajes
if puntaje_j1 > puntaje_j2:
    ganador = jugador1
elif puntaje_j2 > puntaje_j1:
    ganador = jugador2
else:
    ganador = "ninguno, hubo empate"

print("\nLos puntajes finales fueron:")
print(jugador1, ":", puntaje_j1)
print(jugador2, ":", puntaje_j2)
print("El ganador fue", ganador)

print("\nFin del juego")
# Fin del Juego
