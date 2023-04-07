"""
ENUNCIADO:
Un delivery de comidas necesita un programa para procesar los datos de sus pedidos. Por cada Pedido se tienen los
siguientes datos: número de pedido, código de repartidor (un valor entre 0 y 5), descripción del pedido, importe total
del pedido, categoría de comida (un valor entre 0  y 12 ambos incluidos, de la forma 0: comida vegetariana, 1: carnes
2: arepas, etc.). Se desea almacenar la información referida a los n pedidos en un arreglo de registros de tipo Pedido
(definir el tipo Pedido y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos, que
permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de los n pedidos. Valide que el importe total del pedido sea mayor a 0 y que
la categoría de cada comida sea un valor entre 0 y 12. Puede hacer la carga en forma manual, o puede generar los datos
en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe
programar.

2- Mostrar todos los datos de los pedidos con un importe menor a un valor x ingresado por teclado. Este listado debe
mostrar una línea por cada pedido y debe estar presentado en orden de menor a mayor según los importes de los pedidos.
Al final del listado, mostrar una línea adicional con el importe promedio de todos los resgistros mostrados.

3- Usando el arreglo creado en el punto 1, determinar y mostrar la sumatoria (aumulación) de importes de los pedidos
por cada categoría de comida (es decir, 13 acumuladores en un vector de acumulación). Muestre sólo los resultados
mayores a 0.

4- Determinar y mostrar la cantidad de pedidos y la suma de los importes de esos pedidos realizados por un repartidor
cuyo código x se ingresa por teclado. Si el repartidor no tiene ningún pedido registrado, informar con un mensaje esta
situación.

5- Determinar si existe algún pedido con número de pedido igual a x, siendo x un valor que se ingresa por teclado. Si
existe, actualizar en el registro su importe con un descuento del 2% sobre el importe final y mostrar todos los datos
de ese registro. Si no existe, informar con un mensaje.


"""
import random
import clase


def menu():
    cad = "\nMENÚ DE OPCIONES:\n" \
          "1. Cargar Pedidos\n" \
          "2. Datos de Pedidos con Importe Menor a X \n" \
          "3. Importes por Categoría de Comida\n" \
          "4. Pedidos e Importes por Repartidor\n" \
          "5. Existencia de Pedido con Código X\n" \
          "6. Salir\n" \
          "Opción: "
    return cad


def validar_entre(inf, sup, mensaje):
    valor = int(input(mensaje))
    while valor < inf or valor > sup:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor


def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    valor = int(input(mensaje))
    while valor <= inf:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


def carga_manual(pedidos):
    for i in range(len(pedidos)):
        nro = int(input("\nIngrese el número del pedido " + str(i+1) + ": "))
        cod = validar_entre(0, 5, "Ingrese el código de repartidor del pedido " + str(i+1) + ": ")
        desc = str(input("Ingrese la descripción del pedido " + str(i+1) + ": "))
        imp = validar_mayor_que(0, "Ingrese el importe del pedido " + str(i+1) + ": ")
        cat = validar_entre(0, 12, "Ingrese la categoría del pedido " + str(i+1) + ": ")
        pedidos[i] = clase.Pedido(nro, cod, desc, imp, cat)


def carga_automatica(pedidos):
    for i in range(len(pedidos)):
        nro = random.randint(0, 9999)
        cod = random.randint(0, 5)
        # Descripción desconocida
        desc = "-"
        imp = random.randint(100, 9999)
        cat = random.randint(0, 12)
        pedidos[i] = clase.Pedido(nro, cod, desc, imp, cat)


def opcion1():
    n = validar_mayor_que(0, "\nIngrese el número de pedidos a cargar: ")
    pedidos = [None] * n
    carga = validar_entre(1, 2, "Ingrese el tipo de carga a realizar:\n1. Manual\n2. Automática \nCarga: ")
    if carga == 1:
        carga_manual(pedidos)
    else:
        carga_automatica(pedidos)
    return pedidos


def opcion2(pedidos):
    imp = validar_mayor_que(0, "\nIngrese el valor del importe: ")
    clase.selection_sort_importes(pedidos)
    for i in range(len(pedidos)):
        if pedidos[i].importe < imp:
            print(clase.to_string(pedidos[i]))


def opcion3(pedidos):
    ac = [0] * 13
    for i in range(len(pedidos)):
        ac[pedidos[i].categoria] += pedidos[i].importe
    for i in range(len(ac)):
        if ac[i] > 0:
            print("Categoría " + str(i) + ": " + str(ac[i]))


def opcion4(pedidos):
    cod = validar_entre(0, 5, "\nIngrese el código del repartidor x: ")
    cont = 0
    acu = 0
    for i in range(len(pedidos)):
        if pedidos[i].codigo == cod:
            cont += 1
            acu += pedidos[i].importe
    if cont == 0:
        print("El repartidor no tiene ningún pedido registrado")
    else:
        print("Repartidor " + str(cod) + ":")
        print("Cantidad de Pedidos: " + str(cont))
        print("Importes Totales: " + str(acu))


def opcion5(pedidos):
    nro = int(input("\nIngrese el número de pedido búscado: "))
    pos = clase.linear_search_numero(pedidos, nro)

    if pos == -1:
        print("No existe el pedido buscado")
    else:
        print("Pedido: " + str(nro))
        pedidos[pos].importe *= 0.98
        print(clase.to_string(pedidos[pos]))


def test():
    print("DELIVERY: PEDIDOS")
    print("="*60)

    op = -1
    existe = False
    pedidos = []

    while op != 6:
        op = validar_entre(1, 6, menu())

        if op == 1:
            pedidos = opcion1()
            existe = True
        elif op == 2:
            if not existe:
                print("\nNo hay pedidos cargados... Carguelos con la opción 1!")
            else:
                opcion2(pedidos)
        elif op == 3:
            if not existe:
                print("\nNo hay pedidos cargados... Carguelos con la opción 1!")
            else:
                opcion3(pedidos)
        elif op == 4:
            if not existe:
                print("\nNo hay pedidos cargados... Carguelos con la opción 1!")
            else:
                opcion4(pedidos)
        elif op == 5:
            if not existe:
                print("\nNo hay pedidos cargados... Carguelos con la opción 1!")
            else:
                opcion5(pedidos)

    print("\nFin del Programa!")


if __name__ == "__main__":
    test()
