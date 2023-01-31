saludo = 'welcome my friend'

print(dir(saludo))# muestra todo los metodos que se le pueden asignar
 
saludo_mayuscula = saludo.upper() 
saludo_minuscula = saludo.lower()
primer_letra_mayuscula = saludo.capitalize()
buscar_find  = saludo.find('e') # tes da la posicion en la que se encuentra
buscar_index = saludo.index('d') # si no la encuentra lanza una excepcion

#count()
#isnumeric()
#  isalpha
# len() # esto es una fncion tienes que pasarle el parametro

#startwith()
# endwith()
# replace()
# split( )


print(buscar_index)