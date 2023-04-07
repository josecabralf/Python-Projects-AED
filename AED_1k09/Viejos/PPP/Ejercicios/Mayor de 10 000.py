# Generación de Números
import random
cant_nros = 0
mayor = 0
while cant_nros <= 10000:
    gen_nro = random.randint(0, 100000)
    cant_nros += 1
    if mayor < gen_nro:
        mayor = gen_nro
print("El mayor número es: ", mayor)
