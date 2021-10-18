# APUNTES DÍA: 18/10/2021

# Importar módulos en python

# from mis_subrutinas import *

#a = int(input("Introduce el valor de a: "))
#b = int(input("Introduce el valor de b: "))
#c = int(input("Introduce el valor de c: "))

#print(Max3(a, b, c))
#print(Max2(a, b))



# LISTAS
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

# la función "len()" devuelve el tamaño de la lista
print(f"La lista tiene un tamaño de: {len(bases)}")

# Además las listas tienen otros metodos con los que se puede jugar

# Elimiar el último elemento --> pop() devuelve el elemento eliminado
base = bases.pop()
print(f"- Prueba \"pop()\": {bases}. Elemento eliminado: {base}")

# Añadir un nuevo elemento al final
bases.append('U')
print(f"- Prueba \"append()\": {bases}")

# Eliminar un elemento de la lista
base = 'A'
bases.remove(base)
print(f"- Prueba \"remove()\": {bases}. Se ha eliminado: {base}")

# Insertar en cualquier indice un elemento
index = 2
bases.insert(index, 'T')
print(f"- Prueba \"insert()\": {bases}. Insertado el elemento {bases[index]} en la posicion {index + 1}")

# Poner del revés la lista
bases.reverse()
print(f"- La lista del revés: {bases}")

# Ejemplo: Diseñar un algoritmo que dada una fecha en formato: "dia del mes, mes", obtenga el día del año
# que le corresponde.

def fecha_to_dia(day, month):
    # Si todos los meses tuviesen 30 dias:
    # day + 30 * (month - 1)
    # 
    # Se le puede añadir una corrección
    # day + 30 * (month - 1) + correction of month

    correct = [0, 1, -1, 0, 0, 1, 1, 2, 3, 3, 4, 4]
    return day + 30 * (month - 1) + correct[month]


day = int(input("Introduce un día (0 - 31): "))
month = int(input("Introduce un mes (1 - 12): "))
print(fecha_to_dia(day, month))



# DICCIONARIOS
# Los diccionarios son contenedores donde se almacenan entradas que contienen dos elementos: la clave y el valor
# La clave puede ser de cualquier tipo y el valor también

# Definir un diccionario:
dicNotasAlumnos = {
    "Juan Martinez" : 9.5,
    "Federico Pelaez" : 7.0,
    "Sergio Martí" : 6.5, 
    "Rubén Martí" : 8.9,
    "Anastasia Kalafnikove" : 10.0 
}

print(dicNotasAlumnos)

# Los valores del diccionario
notas = list(dicNotasAlumnos.values())
print(notas)

# Los diccionarios son muy útiles porque permiten acceder a los valores por su clave

nombreAlumno = "Juan Martinez"
if nombreAlumno in dicNotasAlumnos:
    print(f"El alumno {nombreAlumno} tiene una nota de {dicNotasAlumnos.get(nombreAlumno)}" + 
    f"\nAhora eliminamos a {nombreAlumno} del diccionario")
    del dicNotasAlumnos[nombreAlumno]
