datos = ('carlos','manuel')
nombre,apellido = datos

# print(nombre)


conjunto = set(['name','lastname'])

print(conjunto)
#mantiene unconjunto dentro de otro conjunto

conjunto = frozenset()
conjunto1 = {1,2,3,4}
conjunto2 = {1,2,3,4,5,6,7}
#verificando que es un subconjunto
resultado = conjunto1.issubset(conjunto2)
#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint()

print(resultado)
