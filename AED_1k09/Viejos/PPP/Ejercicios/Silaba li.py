texto = input(str("Ingrese su texto (recuerde finalizar con un punto):"))

# Asegurarse que el texto tenga punto
texto = texto + "."

# Cant. de Palabras que comienzan con consonantes y terminan en vocales
flag_cons = False
cp_cv = 0
car_ant = None

# Cantidad de palabras que poseen la secuencia ‘li’ a partir de la tercera letra de la palabra
cp_li = 0
cl = 0
flag_l = False

# Cantidad de palabras con menos de 4 letras y porcentaje que dicha cantidad representa sobre el total del texto
cp_4 = 0
ctp = 0

for car in texto:

    # Contar letras
    if car != " " and car != ".":
        cl += 1
        car_ant = car
    # Fin de Palabra
    else:
        if cl >= 1:
            if cl < 4:
                cp_4 += 1
            if car_ant == "a" or car_ant == "e" or car_ant == "i" or car_ant == "o" or car_ant == "u" and flag_cons:
                cp_cv += 1
                flag_cons = False
            ctp += 1
        cl = 0

    # Empieza con consonante?
    if cl == 1 and (car != "a" and car != "e" and car != "i" and car != "o" and car != "u" and car != "A" and car != "E"
                    and car != "I" and car != "O" and car != "U"):
        flag_cons = True

    # "li"?
    if cl > 3:
        if car == "l":
            flag_l = True
        if flag_l and car == "i":
            cp_li += 1
            flag_l = False

# ... porcentaje que dicha cantidad representa sobre el total del texto
porcentaje = (cp_4 / ctp) * 100

# RESULTADOS
print("La cantidad de palabras que comienzan con consonantes y terminan en vocales: ", cp_cv)
print("La cantidad de palabras que poseen la secuencia ‘li’ a partir de la tercera letra de la palabra: ", cp_li)
print("La cantidad de palabras con menos de 4 letras: ", cp_4)
print("Porcentaje que estas ultimas representan: ", porcentaje, "%")
