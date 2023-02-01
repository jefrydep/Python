lista = ['banana','pera','cacahate','limonse','pera']
#filtramos todo lo que sea pera
for frutas in lista:
    if(frutas != 'pera'):
        continue
        
    print(frutas)
    
    
# filtramos todo lo que no sea pera 
for frutas in lista:
    if(frutas != 'pera'):
        continue
        
    print(frutas) 
    
# for en una sola linia de codigo

numero = [1,2,3,4,5]
numeros_multiplicados = [num * 2 for num in numero]
print(numeros_multiplicados)