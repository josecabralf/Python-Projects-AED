def sucesion(n):
    if n % 2 == 0:
        n = n/2
    else:
        n = 3 * n + 1
    return n


def promedio(v, longitud):
    ac = 0
    for i in v:
        ac += i
    prom = round(ac / longitud, 1)
    return prom


def test():
    n = int(input("Ingrese el primer valor de n: "))
    v = [n]

    while n != 1:
        n = sucesion(n)
        v.append(n)

    print("Orbita: ", v)
    print("Longitud de Orbita: ", str(len(v)))
    print("Promedio: ", str(promedio(v, len(v))))
    print("Mayor: ", max(v))


test()
