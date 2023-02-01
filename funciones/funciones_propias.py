
def saludar(name):
    return f'hola {name}'

myName = 'Jefry'

mysaludo = saludar(myName)

print(mysaludo)

def sumar (*numeros):
    sumados = sum(numeros)
    return sumados

resultado = sumar(1,2,3,4,5)
print(resultado)

#tambien podemos agregar prametros opcionaless