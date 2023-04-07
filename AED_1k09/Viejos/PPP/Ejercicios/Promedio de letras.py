cl = 0
cant_l = 0
cp = 0
frase = None

while frase != ".":

    frase = input(str("Ingrese una frase de a un caracter por vez (use punto para finalizar): "))

    # Contar letras
    if frase != " " and frase != ".":
        cl += 1

    # Contar palabras y acumular las letras
    else:
        if cl >= 1:
            cant_l += cl
            cp += 1
        cl = 0

promedio = cant_l/cp

print("La cantidad de palabras fue: ", cp)
print("La cantidad promedio de letras por palabra es de: ", promedio)
