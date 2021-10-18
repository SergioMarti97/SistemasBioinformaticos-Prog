# Este fichero es para probar los módulos en python
# 
# Un modulo es un fichero con extensión .py (igual que un programa de python) que contiene todas las funciones
# y clases que queramos. Se hace para ordenar el código
#
# Para invocar las funciones contenidas en este fichero, se debe de utilizar la siguiente sintaxis:
# 
# import mis_subrutinas as ms <- donde ms es el acronimo
# from mis_subritinas import Max2 <- donde Max2 es una función en concreto que queremos importar. Si ponemos un '*' importamos todas las funciones
#   

# Crear una función para sacar el valor máximo de 3 valores:
def Max3(x, y, z):
    if x > y > z or x > z > y:
        return x
    if y > x > z or y > z > x:
        return y
    if z > x > y or z > y > x:
        return z

# Función maximo 2:
def Max2 (x, y):
    # Algoritmo
    return ((x + y + abs(x - y)) / 2)