# DATOS
nro = int(input("Ingrese un número: "))
sumatoria = 0
pares = 0
impares = 0
cero = False
alternado = True

# PROCESO
while nro >= 0:
    nro_ant = nro
    if 50 <= nro <= 100:
        sumatoria += nro
    if nro % 2 == 0:
        pares += 1
    else:
        impares += 1
    if nro == 0:
        cero = True
    nro = int(input("Ingrese un número: "))
    if (nro_ant + nro) % 2 == 0 and nro >= 0:
        alternado = False

# Resultados
print("La sumatoria es igual a ", sumatoria)
print("La cantidad de valores pares es: ", pares)
print("La cantidad de valores impares es: ", impares)
if cero:
    print("Se ingreso al menos un cero")
if alternado:
    print("La serie contiene solo números pares e impares alternados")
