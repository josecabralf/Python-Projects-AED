z = int(input("Seleccione la Operación que quiere: 1. Segundos a H:M:S 2. H:M:S a Segundos "))

if z == 1:

    ts = int(input("Ingrese la Cantidad de Segundos:"))

    s = ts % 60
    m = (ts % 3600) // 60
    h = ts // 3600

    print("El tiempo transcurrido fue: ", h, "hora/s", m, "minuto/s", s, "segundo/s")

else:

    h = int(input("Ingrese la cantidad de Horas: "))
    m = int(input("Ingrese la cantidad de Minutos: "))
    s = int(input("Ingrese la cantidad de Segundos: "))

    ts = h * 3600 + m * 60 + s

    print("El tiempo transcurrido fue: ", ts, "segundos")
