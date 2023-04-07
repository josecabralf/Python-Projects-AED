"""
Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe incluir al
menos una función simple con parámetros y retorno de resultado, debe procesar el texto caracter a caracter (a razón de
uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

Determinar la cantidad de palabras que tienen dos dígitos seguidos y no tienen "n" (mayúscula o minúscula).
Por ejemplo, el texto: "El curso 1k06 rinde a la tarde." tiene una sola palabra que cumple la condición ("1k06").

Determinar el porcentaje de palabras (respecto del total de palabras del texto) que comienzan y terminan con vocal.
Por ejemplo, en el texto: "Una oca es casi igual a un ganso." hay 3 palabras que cumplen la condición: "Una", "oca"
y "a". Como el texto completo tiene 8 palabras, el porcentaje pedido es 37.5%.

Determinar la cantidad de palabras que comienzan con el primer caracter del texto (en mayúscula o en minúscula).
Por ejemplo, en el texto: "En Córdoba este verano será eterno." Hay tres palabras que cumplen la condición (incluida la
primera palabra del texto): "En", "este" y "eterno".

Determinar el promedio de caracteres por palabra de aquellas que tienen la expresión "pe" (con cualquiera de sus
letras en minúscula o en mayúscula). Por ejemplo, en el texto: "Pedro es genial pero no va a venir." hay 2 palabras
que cumplen la condición ("Pedro" y "pero"). Entre la dos suman 9 caracteres y por lo tanto es el promedio pedido es
4.5 letras por palabra. Por "caracteres", se entiende "cualquier tipo de símbolo, sea este un dígito, una letra, o
cualquier otro que pueda aparecer".
"""


# Ingresar Texto --- Pasarlo a minusculas --- Corroborar final con "."
def ingreso_texto():
    texto = input("Ingrese su texto (finalice con un punto): ")
    texto = texto.lower()

    if texto[-1] != ".":
        texto = texto + "."

    return texto


# Determinar si un caracter es dígito
def es_digito(car):
    return car in "0123456789"


# Determinar si un caracter es vocal
def es_vocal(car):
    return car in "aeiouáéíóú"


# Calcular porcentaje
def porcentaje(subtotal, total):
    porc = 0

    # Evitar n/0
    if total > 0:
        porc = round((subtotal / total) * 100, 2)

    return porc


# Calcular Promedio de Letras por Palabras
def promedio(letras, palabras):
    prom = 0
    # Evitar n/0
    if palabras > 0:
        prom = round(letras / palabras, 2)

    return prom


# Programa Principal
def principal():
    print("="*60)
    print("Bienvenido al Programa del Parcial N°2")
    print("="*60, "\n")

    texto = ingreso_texto()
    cont_car = cont_pal = 0

    # Dos dígitos seguidos y no n
    flag_n = flag_dig = False
    ult_car = None
    cont_dig = 0

    # Palabras que comienzan y terminan en vocal
    flag_ini_voc = False
    cont_pal_voc = 0

    # Palabras que comienzan con el primer caracter del texto
    primer_car = None
    # Aunque se cuenta la primera palabra, existe la posibilidad de texto vacío y, por lo tanto, cont_pal_primer == 0
    cont_pal_primer = 0

    # Promedio de letras en palabras con "pe"
    flag_pe = False
    cont_pal_pe = acu_car_pe = 0

    # Ciclo for (caracter por caracter)
    for car in texto:

        if car != " " and car != ".":
            cont_car += 1

            if cont_car == 1:
                # Palabra inicia con vocal?
                if es_vocal(car):
                    flag_ini_voc = True

                # Guardar primer caracter del texto
                if cont_pal == 0:
                    primer_car = car
                    # Se cuenta la primera también
                    cont_pal_primer += 1
                # En caso que no sea la 1ra palabra, comparar y sumar en caso de que car == primer_car
                elif car == primer_car:
                    cont_pal_primer += 1

            # Las siguientes son todas mutuamente excluyentes. Por lo tanto elif
            # Contiene "n"?
            if car == "n":
                flag_n = True
            # Contiene 2 digitos seguidos?
            elif es_digito(car) and es_digito(ult_car):
                flag_dig = True
            # Contiene "pe"?
            elif car == "e" and ult_car == "p":
                flag_pe = True

            # Guardar ultimo caracter
            ult_car = car

        else:
            if cont_car > 0:
                cont_pal += 1

                # Las siguientes NO son mutuamente excluyentes. Por lo tanto if
                # Contar si 2 dígitos consecutivos y no "n"
                if flag_dig and not flag_n:
                    cont_dig += 1
                # Contar si comienza y termina en vocal
                if flag_ini_voc and es_vocal(ult_car):
                    cont_pal_voc += 1
                # Acumular caracteres y contar palabras con "pe"
                if flag_pe:
                    acu_car_pe += cont_car
                    cont_pal_pe += 1

            # Reset Variables
            flag_n = flag_dig = flag_ini_voc = flag_pe = False
            cont_car = 0

    print("\nLa cantidad de palabras que tienen dos dígitos seguidos y no tienen 'n' fue:", cont_dig)
    print("El porcentaje de palabras que comienzan y terminan con vocal fue:", porcentaje(cont_pal_voc, cont_pal))
    print("La cantidad de palabras que comienzan con el primer caracter del texto fue", cont_pal_primer)
    print("El promedio de caracteres por palabra de aquellas que tienen la expresión 'pe' fue:",
          promedio(acu_car_pe, cont_pal_pe))

    print("\nFin del Programa")


if __name__ == "__main__":
    principal()
