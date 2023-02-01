
#maneras de trabajar con modulos

# import saludar as saludando
# si ponemos import* importamos todo pero es considerado una mala p ractica
 
# podemos redeclaras nuestras funciones con as poniendole un alias
from saludar import saludar

# saludart = saludando.saludar()
saludart = saludar()

print(saludart)
# accedemos al nombre de este modulo
print(__name__)

# para importar un modulo desde otra carpéta podenmos e combre dela carpetay punto
# import sys
import sys
# nos muestra todos los modulos
print(sys.builtin_module_names)
# modulos instalados
print(sys.path)