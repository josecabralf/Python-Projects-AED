import random

# Variables
cant_nros = 0
menor = 100000
sumatoria = 0
menores10k = 0

while cant_nros <= 5000:
    gen_nro = random.randint(0, 100000)
    cant_nros += 1
    if gen_nro < menor:
        menor = gen_nro
    if gen_nro < 10000:
        menores10k += 1
        sumatoria += gen_nro

promedio = sumatoria / menores10k
print("El menor de los números es: ", menor)
print("El valor promedio de los números menores a 10.000 es: ", promedio)
