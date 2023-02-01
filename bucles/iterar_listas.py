animales = ['gato','perro','loro','gallina','cuervo','chancho']
for animal in animales:
    print(animal)
numeros = [1,2,3,4,5,6]
for numero in numeros:
    resultado = numero * 2
    print(resultado)


# iterar dos listas ambos deben tener la misma cantidad de parametros
for animale,numero in zip(animales,numeros):
    print(f'recorriedno lista 1: {numero}')
    print(f'recorriedno lista 1: {animale}')

for num in range(10,20):
    print(num)
    
    # forma corredcta de reorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
else:
    print('el bule ya termino')


# todo lo anterior sirve para iterar tuplas conjuntos
