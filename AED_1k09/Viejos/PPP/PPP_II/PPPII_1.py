"""
Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:

  1 - Determinar la cantidad de palabras que terminan con la tercer letra de la primera palabra del texto. Por ejemplo,
  en el texto: “Las casas se terminaron antes de lo previsto.” Tiene 2 palabras que cumplen con la condición: “casas”
  y “antes”.

  2 - Determinar la cantidad palabras que tienen vocales en la segunda mitad de la palabra y cuya longitud sea mayor o
  igual a 5 letras. Por ejemplo, en el texto “Las materias de la facultad en cuarentena se rinden en aula virtual.”
  Tiene 5 palabras que cumplen con la condición: “materias”, “facultad”, “rinden”, ”cuarentena” y “virtual”.

  3 - Determinar la cantidad de palabras de longitud impar que se encuentran en el texto y que comienzan con una
  consonante. Por ejemplo, en el texto: “En el aula virtual los alumnos realizan tareas.” Tiene 2 palabras que cumplen
  con la condición: “virtual” y “realizan”.

  4 - Determinar el porcentaje que representan las palabras del punto 3 en base al total de palabras que se encuentran
  en el texto. Por ejemplo, en el texto: “En el aula virtual los alumnos realizan tareas.” La cantidad de palabras son
  8, 2 palabras cumplen con el punto 3, el porcentaje seria 2/8 = 25%.
"""


def es_vocal(car):
    return car in "aeiouAEIOUáéíóúÁÉÍÓÚ"


def test():

    texto = input("Ingrese un texto (Finalice con punto): ")
    texto = texto.lower()

    cont_let = cont_pal = cont_voc = 0

    # Tercera
    tercera = ult_car = None
    cont_pal_ter = 0

    # Vocal 2da Mitad
    cont_pal_voc = 0
    pos_voc = 0

    # Empieza consonante y len impar
    primera = None
    cont_pal_con_im = 0

    for car in texto:

        if car != " " and car != ".":
            cont_let += 1
            ult_car = car

            if cont_let == 1:
                primera = car

            if cont_let == 3 and cont_pal == 0:
                tercera = car
            
            if es_vocal(car):
                pos_voc = cont_let
                cont_voc += 1

        else:
            if cont_let > 0:
                cont_pal += 1

                medio_pal = cont_let // 2

                if ult_car == tercera and cont_pal != 1:
                    cont_pal_ter += 1

                if cont_let >= 5 and cont_voc > 0 and pos_voc > medio_pal:
                    cont_pal_voc += 1

                if not es_vocal(primera) and (cont_let % 2 == 1):
                    cont_pal_con_im += 1
                    primera = None

            cont_let = cont_voc = pos_voc = 0

    porcentaje = round((cont_pal_con_im / cont_pal) * 100, 2)

    print("La cantidad de palabras que terminan con la tercer letra de la primera palabra del texto fue:", cont_pal_ter)
    print("La cantidad palabras que tienen vocales en la segunda mitad de la palabra y cuya longitud sea mayor o igual a"
          " 5 letras fue:", cont_pal_voc)
    print("La cantidad de palabras de longitud impar que se encuentran en el texto y que comienzan con una consonante "
          "fue:", cont_pal_con_im)
    print("Representando un:", str(porcentaje), "%")


test()
