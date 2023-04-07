"""
Nos solicitaron un software para registrar los usuarios que acceden un determinado software.

Cada usuario registrado debe contener un código identificatorio, un nombre de usuario, un password (que debe ser igual
4 caracteres y no ser mayor de 10 caracteres), el departamento al que pertenece el usuario (número entre 0 y 19)
Se pide:

1 -Generar las estructuras correspondientes para se registren los usuarios en un array de Registros.

Controlar que el password cumpla con los requerimientos antes mencionados al igual que el departamento.

2 - Listar los usuarios, omitiendo el password.

3 - Contar y mostrar cuantos usuarios hay por departamento.

4 - Modificar el password de un usuario.
"""
import random


class Usuario:
    def __init__(self, codigo, nombre, password, departamento):
        self.cod = codigo
        self.nom = nombre
        self.pas = password
        self.dpto = departamento


def validar_entre(inf, sup, mensaje):
    valor = int(input(mensaje))
    while valor < inf or valor > sup:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor


def menu():
    cad = "\nMENÚ DE OPCIONES:\n" \
          "1. Registrar usuarios\n" \
          "2. Lista de Usuatrios \n" \
          "3. Usuarios por departamento\n" \
          "4. Cambiar contraseña\n" \
          "5. Salir\n" \
          "Opción: "
    return cad


def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    valor = int(input(mensaje))
    while valor <= inf:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


def cars():
    car = "0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    return car


def gen_password():
    dig = random.randint(4, 9)
    cad = ""
    for i in range(dig):
        cad += str(random.choice(cars()))
    return cad


def registrar_usuarios(usuarios):
    n = validar_mayor_que(0, "\nIngrese la cantidad de usuarios a registrar: ")
    usuarios *= n

    for i in range(n):
        cod = random.randint(0, 9999)
        nombre = "Usuario" + str(i)
        password = gen_password()
        dpto = random.randint(0, 19)
        usuarios[i] = Usuario(cod, nombre, password, dpto)


def write(usuarios):
    print()
    for i in range(len(usuarios)):
        r = ""
        r += "{:<15}".format("Código: " + str(usuarios[i].cod))
        r += "{:<25}".format("Nombre: " + usuarios[i].nom)
        r += "{:<15}".format("Departamento: " + str(usuarios[i].dpto))
        print(r)


def usuarios_dpto(usuarios):
    cont = [0] * 20
    for i in range(len(usuarios)):
        cont[usuarios[i].dpto] += 1
    for i in range(len(cont)):
        if cont[i] != 0:
            print("Departamento", str(i), ":", cont[i])


def linear_search_user(usuarios, user):
    r = -1
    for i in range(len(usuarios)):
        if user == usuarios[i].cod:
            r = i
            return r
    return r


def validar_password():
    password = ""
    validez = False

    while not validez:
        password = str(input("Ingrese la nueva contraseña: "))
        n = len(password)
        if not (4 <= n <= 10):
            print("Esa contraseña no es valida! Intente de nuevo...\n")
        else:
            validez = True
    return password


def cambiar_pass(usuarios):
    pos = -1
    while pos == -1:
        user = int(input("\nIngrese el código identificador del usuario: "))
        pos = linear_search_user(usuarios, user)
        if pos == -1:
            print("El usuario buscado no existe!")
        else:
            usuarios[pos].pas = validar_password()


def test():
    print("REGISTRO DE USUARIOS:")
    print("="*60)

    op = -1
    usuarios = [None]
    existe = False

    while op != 5:
        op = validar_entre(1, 5, menu())

        if op == 1:
            registrar_usuarios(usuarios)
            existe = True
        elif op == 2:
            if existe:
                write(usuarios)
            else:
                print("\nNo existen usuarios... Intente registrarlos con la opcion 1!")
        elif op == 3:
            if existe:
                usuarios_dpto(usuarios)
            else:
                print("\nNo existen usuarios... Intente registrarlos con la opcion 1!")
        elif op == 4:
            if existe:
                cambiar_pass(usuarios)
            else:
                print("\nNo existen usuarios... Intente registrarlos con la opcion 1!")

    print("Fin.")


if __name__ == "__main__":
    test()
