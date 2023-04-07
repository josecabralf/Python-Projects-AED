import math
import os
import pickle


class Point:
    def __init__(self, cx, cy, desc='p'):
        self.x = cx
        self.y = cy
        self.descripcion = desc


def to_string(point):
    r = str(point.descripcion) + '(' + str(point.x) + ', ' + str(point.y) + ')'
    return r


def distance_between(p1, p2):
    # calcular "delta y" y "delta x"
    dy = p2.y - p1.y
    dx = p2.x - p1.x

    # Distancia entre ellos... Pitágoras...
    return math.sqrt(pow(dx, 2) + pow(dy, 2))


def read_fd(fd):
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    v = []

    while m.tell() < t:
        p = pickle.load(m)
        v.append(p)
    m.close()

    return v


def buscar_d(v):
    d_max = 0
    d_min = 9999
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            d = distance_between(v[i], v[j])
            if d < d_min:
                d_min = d
            if d > d_max:
                d_max = d

    d_min = round(d_min, 0)
    d_max = round(d_max, 0)

    return d_min, d_max


def test():
    fd = "puntos.df4"
    v = read_fd(fd)
    d_min, d_max = buscar_d(v)
    print("Dist Minima: ", str(d_min))
    print("Dist Máxima: ", str(d_max))


if __name__ == "__main__":
    test()
