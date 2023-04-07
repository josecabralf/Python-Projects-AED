import soporte


def contador(v, c):
    for i in range(len(v)):
        c[v[i]] += 1


def no_cero(c):
    nc = 0
    for i in range(len(c)):
        if c[i] != 0:
            nc += 1
    return nc


def buscar_mayor(v):
    mayor = v[0]
    pos = 0
    for i in range(1, len(v)):
        if v[i] > mayor:
            mayor = v[i]
            pos = i
    return pos


def test():
    c = [0] * 300000
    v = soporte.vector_known_range(300000)
    contador(v, c)
    nc = no_cero(c)

    print("Cant de nros != 0: ", str(nc))

    pos = buscar_mayor(c)
    print("Moda:", pos)
    print("Frecuencia", str(c[pos]))


if __name__ == "__main__":
    test()
