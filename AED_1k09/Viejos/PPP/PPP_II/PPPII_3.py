""""
Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:

1 - Determinar la cantidad de palabras que presentan digitos en la palabra. Por ejemplo, en el texto: “El 1K09 y el
1K15 son cursos espejos a partir del año 2020.” Tiene 3 palabras que cumplen con la condición: “1K09”, “1K15” y “2020”.

2 - Determinar el promedio de letras de la palabras del texto que presentan la combinacion “pe” a partir de la tercer
letra de la palabra. Por ejemplo, en el texto: “El acampe del año apenas tuvo un ágape.” Tiene 2 palabras que cumplen
con la condición “acampe” y “ágape” que suman 11 letras, por lo que el promedio seria 11/2 = 5.5 letras.

3 - Determinar la cantidad de palabras que finalizan con la letra “n” y que empiecen con una vocal. Por ejemplo, en el
texto: “Los jovenes acamparon y asaron unos choripanes.” Tiene 2 palabras que cumplen con la condición “acamparon” y
“asaron”.

4 - Determinar la cantidad de palabras que finalizan con la primera letra de esa palabra. Por ejemplo, en el texto:
“Las simples vidas son solitarias.” Tiene 2 palabras que cumplen con la condición “simples” y “solitarias”.
"""

def ingreso():
    texto = input("Ingrese su texto (finalice con un punto): ")

    if texto[-1] != ".":
        texto = texto + "."

    return texto


def es_digito(car):
    return car in "0123456789"


def es_vocal(car):
    return car in "aeiouAEIOUáéíóúÁÉÍÓÚ"


def promedio(letras, palabras):
    prom = 0
    if palabras > 0:
        prom = round(letras / palabras, 2)

    return prom


def principal():
    texto = ingreso()

    cont_let = 0
    cont_pal = 0

    # Palabras con dígitos
    pal_dig = 0
    flag_dig = False

    # Promedio de Letras en Palabras con "pe"
    pal_pe = 0
    acu_pe = 0
    flag_p = False
    flag_pe = False

    # Palabras que empiezan en vocal y terminan en n
    flag_vocal = False
    ult_car = None
    cont_vn = 0

    # Primera letra == Ultima letra
    cont_igual = 0
    prim_car = None

    for car in texto:

        if car != " " and car != ".":
            cont_let += 1

            if es_digito(car):
                flag_dig = True

            if cont_let == 1:
                if es_vocal(car):
                    flag_vocal = True
                prim_car = car
            elif cont_let > 3:
                if car == "p":
                    flag_p = True
                elif car == "e" and flag_p:
                    flag_pe = True
                else:
                    flag_p = False

            ult_car = car

        else:
            if cont_let >= 1:
                cont_pal += 1

                if flag_dig:
                    pal_dig += 1

                if flag_pe:
                    acu_pe += cont_let
                    pal_pe += 1

                if flag_vocal and ult_car == "n":
                    cont_vn += 1
                elif prim_car == ult_car:
                    cont_igual += 1

            cont_let = 0
            flag_dig = False
            flag_pe = False
            flag_vocal = False

    prom_pe = promedio(acu_pe, pal_pe)

    print("La cantidad de palabras con dígitos fue:", pal_dig)
    print("El promedio de letras en palabras que presentan 'pe':", prom_pe)
    print("La cantidad de palabras que comienzan en vocal y terminan con 'n' fue:", cont_vn)
    print("La cantidad de palabras que comienzan con la misma letra con la que terminan fue:", cont_igual)


if __name__ == "__main__":
    principal()
