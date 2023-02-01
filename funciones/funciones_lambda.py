# creando una funcion lambda para multiplicar por dos
# es como el return implicitoi de java script
multiplicar_por_dos = lambda x: x * 2

print(multiplicar_por_dos(5))
# el filter te itera cada valor
# filter()


def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input("ingrese el nombre del compañero")
        edad = int(input("ingrese su edad"))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros [-1][0]
    return asistente,profesor



asistente,profesor = obtener_compañeros(3)
