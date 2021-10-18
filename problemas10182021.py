# APUNTES DÍA: 18/10/2021

from mis_subrutinas import *

#a = int(input("Introduce el valor de a: "))
#b = int(input("Introduce el valor de b: "))
#c = int(input("Introduce el valor de c: "))

#a = 10
#b = 12
#c = 4

#print(Max3(a, b, c))
#print(Max2(a, b))

# Listas

# Las listas son contenedores de elementos, ordenados por un indice.
# En python, las listas comienzan con índice 0

# definir la lista
bases = ['A', 'C', 'G', 'T']

# mostrar todas las bases
print(bases)

# mostrar el elemento con índice 2
print(bases[2])

# mostrar una sublista de la lista
# Para definir los intervalos, el último número no se tiene en cuenta
print(bases[1:4])

# Las listas son mutables, se pueden añadir y quitar elementos de la lista, y se pueden modificar
print("El último elemento de la lista es: " + bases[3])
bases[3] = 'U'
print("El último elemento de la lista ahora es: " + bases[3] + "\nAhora son las bases del RNA")

# El método de ordenación "sort" pertence a todas las listas
bases.sort()
print(f"La lista ordenada: {bases}")