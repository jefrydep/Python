# crear un lista vacia 

lista = list([])
#devuel la cantidad de eleemnetos

cantidad_elementos = len(lista);

#agregar un elemento a la lista
lista.append('jajajaj')
# agregar un elemnto a una lista en un indice dado

lista.insert(2,'fuckyou')
#agregando varios elementos a la lista
lista.extend(['1','roky'])
#elimina el elemnto de una lista pasandole un parametro
# -1 elimina el ultimo elemento de la lista
lista.pop(2)
# remueve un elemento de lal lista por su valor

lista.remove('roky')

# ordena los numeros o elemntos de forma accendent
# si pasamos el parametro reverse= true los cambia la orden
lista.sort()
# invierte los elementos de l lista 
lista.reverse()

 # te la direcion del indice 
lista.index()




# elimina todos los elementos de la lista
lista.clear()
print(lista)


