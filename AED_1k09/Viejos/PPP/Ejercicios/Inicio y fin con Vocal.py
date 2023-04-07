# Se solicita crear un programa que permita ingresar un texto, las palabras se encontrarán separadas únicamente
# por espacios en blanco y el mismo debe finalizar con un punto. En base a ese texto determinar:

# a) La cantidad de palabras que comienzan y terminan en vocal
# b) La cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior
# c) El porcentaje que representa el punto a) sobre el total de palabras del texto

texto = input(str("Ingrese su texto (recuerde finalizar con un punto):"))

texto = texto + "."
# contador de letras
cl = 0

# contador total de palabras
ctp = 0

# comienzan y terminan en vocal
comienzo_vocal = False
vocal = 0

# final y comienzo con misma letra
car_ant = None
misma_letra = 0

for car in texto:

    cl += 1

    if cl == 1:
        # comienzo con vocal
        if car == "a" or car == "e" or car == "i" or car == "o" or car == "u" or car == "A" or car == "E" or car == "I" \
                or car == "O" or car == "U":
            comienzo_vocal = True
        # final y comienzo
        if car == car_ant:
            misma_letra += 1

    # final de palabra
    if car == " " or car == ".":
        if cl > 1:
            ctp += 1
            if (car_ant == "a" or car_ant == "e" or car_ant == "i" or car_ant == "o" or car_ant == "u") and \
                    comienzo_vocal:
                vocal += 1
                comienzo_vocal = False
        cl = 0
    else:
        car_ant = car

# Resultados
print("La cantidad de palabras que comienzan y terminan en vocal: ", vocal)
print("La cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior: ", misma_letra)

# Porcentaje
porcentaje = (vocal/ctp) * 100
print("Porcentaje de palabras que comienzan y terminan en vocal: ", porcentaje, "%")
