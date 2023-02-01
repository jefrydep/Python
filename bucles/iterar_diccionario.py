diccionario = {
    'name':'jefry',
    'last_name':'palomino',
    'age':23,
    'status':'married'
}
for datos in diccionario.items():
    key = datos[0]
    value= datos[1]
    print(value)