"""
Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:

1)      Determinar la cantidad de palabras que incluyen exactamente dos vocales. Por ejemplo, en el texto: “Los cursos
del turno tarde.” Respuesta: 3 palabras. Las palabras que cumplen con la condición son: “cursos”, “turno” y “tarde”.

2)      Determinar el porcentaje de palabras en todo el texto que tienen una cantidad impar de caracteres.
Por ejemplo, en el texto: “Hoy es un lindo día.” Respuesta: 60,00 % (palabras que cumplen la condición: 3
("Hoy", "lindo" y "día")
sobre un total de palabras de 5).

3)      Determinar cuántas palabras del texto inician con consonante y tienen más de 4 letras. Por ejemplo,
en el texto: “Confiamos que aprueben el parcial.” Respuesta: 2 palabras. Las palabras que cumplen la condición son:
“Confiamos” y “parcial”.

4)      Determinar cuántas palabras incluyen la expresión "sa" pero más de una vez. Por ejemplo, en el texto:
“La salsa es muy sabrosa.” Respuesta: 2 palabras. Las palabras que cumple con la condición son: “salsa” y "sabrosa".
"""


def ingreso():
    texto = input("Ingrese su texto (finalice con un punto):")

    if texto[-1] != ".":
        texto = texto + "."

    return texto


def es_vocal(car):
    return car in "aeiouAEIOUáéíóúÁÉÍÓÚ"


def porcentaje(monto, total):
    porc = round((monto/total) * 100, 2)
    return porc


def principal():
    print("Ejercicio 4: Procesamiento de Texto")
    texto = ingreso()

    cont_let = 0
    cont_pal = 0

    # A- Dos Vocales
    cont_voc = 0
    dos_voc = 0

    # B- Cant Impar de Letras
    impar = 0

    # C- Consonante y +4 letras
    flag_con = False
    con_cuatro = 0

    # D- Sa sa
    cont_pal_sa = 0
    cont_sa = 0
    car_ant = None

    for car in texto:

        if car != " " and car != ".":
            cont_let += 1

            if es_vocal(car):
                cont_voc += 1

            if not es_vocal(car) and cont_let == 1:
                flag_con = True

            if car_ant == "s" and car == "a":
                cont_sa += 1

            car_ant = car

        else:
            if cont_let > 0:
                cont_pal += 1

                if cont_voc == 2:
                    dos_voc += 1

                if cont_let % 2 == 1:
                    impar += 1

                if flag_con and cont_let > 4:
                    con_cuatro += 1

                if cont_sa >= 2:
                    cont_pal_sa += 1

                cont_sa = 0
                cont_voc = 0
                flag_con = False
                cont_let = 0
                car_ant = None

    print("La cantidad de palabras con 2 vocales exactamente fue:", dos_voc)
    print("El porcentaje de palabras con cantidad de letras impares:", porcentaje(impar, cont_pal))
    print("La cantidad de palabras que inician en consonante y tienen más de 4 letras fue:", con_cuatro)
    print("La cantidad de palabras que incluyen la expresión 'sa' más de una vez fue:", cont_pal_sa)


if __name__ == "__main__":
    principal()
