import pickle
import os


def generar_archivo(vector, archivo):
    arch = open(archivo, 'wb')
    for c in vector:
        pickle.dump(c, arch)
    arch.flush()
    arch.close()


def leer_archivo(archivo):
    # Conseguir tamaño del archivo
    size = os.path.getsize(archivo)

    # Controlar que existe el archivo
    if size < 0:
        return None

    arch = open(archivo, 'rb')
    vc = [0] * 10
    while arch.tell() < size:
        # Cargamos una de las cabañas a una variable
        cabana = pickle.load(arch)
        vc[cabana.tipo] += cabana.monto
    arch.close()
    return vc
