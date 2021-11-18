# Ejercicios y problemas de Python - día: 16/11/2021
from itertools import *

# Continuamos con el ejercicio de ayer, pero esta vez lo hacemos con diccionarios
# y como dice el profe
def puntacion_y_consenso_dic(motifs, k):
    # Definimos el profile
    profile = {
        'A' : [],
        'C' : [],
        'G' : [],
        'T' : []
    }

    # Inicializamos el profile
    for i in range(k):
        for key in profile.keys():
            profile[key].append(0)

    # Calculamos los valores de profile
    for motif in motifs:
        for i in range(k):
            profile[motif[i]][i] += 1
            
    # Calcular la puntuación y el la secuencia consenso
    score = 0
    consense = ""
    for col in range(k):
        max = 0
        for key, value in profile.items():
            if value[col] > max:
                max = value[col]
                base = key
        score += max
        consense += base
                
    # Calcular la puntuación y el consenso
    return (score, consense) 


# función powerset
def powerset(elementos):
    """
    Esta función obtiene todas las posibles combinaciones de los valores contenidos en elementos
    """
    s = list(elementos)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


# función suma_numeros
def suma_numeros(elements, score):
    """
    Esta función sirve para obtener las combinaciones de valores (que hay en elementos)
    cuya suma sea igual a la suma objetivo, llamada "score"
    Además, devuelve las combinaciones mejores, mejores en el sentido que son combinaciones que 
    suman la suma objetivo con una combinación de menos números
    """
    result = []
    len_result = len(values) + 1
    for c in powerset(elements):
        sum = 0
        for num in c:
            sum += num
        
        if sum == score:
            # Es posible que haya más de una solución con el mismo tamaño
            if len(c) < len_result:
                result = []
                len_result = len(c)
            
            if len(c) == len_result:
                result.append(c)

    return (result)


# ----------------------------------------------------------------
print("==== Ejercicio 4.2. \"Motif: profile y consenso\" ====")

# Definimos las variables de prueba (sacadas del power point)
motif = ["AGGTACTT", "CCATACGT", "ACGTTAGT", "ACGTCCAT", "CCGTACGG"]
k = len(motif[0])

# Mostrar los motivos 
for m in motif:
    print(f"{m}")

# Desempaquetar la información
score, consense = puntacion_y_consenso_dic(motif, k)

# Mostramos la información
print(f"\n{consense} --> consenso\nPuntuación: {score}\nPorcentage (score/max_escore * 100): "
      f"{score / float(k * len(motif)) * 100}%")

# ----------------------------------------------------------------
# TEMA 1: Algoritmos en python
# ----------------------------------------------------------------
print("\n==== TEMA 1: Algoritmos en python ====")

# --- En este tema vamos a dar la busqueda exaustiva ---
print("==== BUSQUEDA EXAHUSTIVA ====")

# Sea un conjunto de números, obtener un subconjunto cuya suma sea exactamente un valor.
# Por ejemplo, sea (13, 11, 7) y el valor a obtener 20, la solución es el subconjunto que
# suma ese valor es (13, 7)

# definimos el conjunto de valores
values = set()
values.add(13)
values.add(11)
values.add(7)

# lo mostramos
print(f"Los valores con los que trabajaremos:\n{values}")

# Ahora lo que hacemos es tratar de encontrar todos los candidatos
# Usaremos el paquete "itertools"
print("Todas las combinaciones posibles tomando solo 2 valores:")
for c in combinations(values, 2):
    print(c)

# ¿Y si queremos todas las combinaciones?
print("Todas las combinaciones posibles tomando cualquier número de valores:")
for cardi in range(len(values) + 1):
    for c in combinations(values, cardi):
        print(c)

# A esto se le llama "power set", el súper conjunto de combinaciones posibles

# Función powerset encapsula el código de arriba:
print("Todas las combinaciones posibles tomando cualquier número de valores, usando la función powerset:")
for c in powerset(values):
    print(c)

# Ahora, la busqueda exaustiva consiste en buscar en todo este conjunto, cuales
# combinaciones cumplen el requisito. Esto lo hace la función suma_numeros
score = 20
values.add(9)
values.add(3)
values.add(4)
values.add(2)
print(f"Combinación que cumple el requisito que sus valores sumen {score}:\n{suma_numeros(values, score)}")
