# Ejercicios y problemas de Python - día: 16/11/2021

# ----------------------------------------------------------------
# TEMA 2: Motif, búsqueda exhaustiva
# ----------------------------------------------------------------

# Los genes son activados o desactivados por proteínas reguladoras
# Estas proteínas se unen a regiones reguladoras de los genes con el 
# fin de atraer o bloquear la RNA polimerasa
# El fragmento de DNA al que se unen estas proteínas reguladoras se
# denomina motif
# Encontrar el mismo motif en varios genes sugiere que existe una 
# relación de regulación entre ellos, como los genes relacionados con 
# los ciclos circadianos
# Habitualmente, se conoce el tamaño de los motif. Sin embargo, no 
# resulta fácil su localización ya que suelen presentarse con algunas
# mutaciones en cada gen
#
# El problema de la búsqueda de motif plantea las siguientes 
# dificultades:
# - El motif puede variar ligeramente en cada gen debido a mutaciones.
# - No se conoce el motif que buscamos, aunque sí su tamaño.
# - La ubicación en las regiones reguladoras tampoco es conocida y 
#   puede ser distinta en cada gen.
#
# El problema de la búsqueda de los motif requiere conocer la siguiente
# información:
# - t: número de secuencias de DNA (regiones reguladoras de los genes)
# - n: longitud de las secuencias (todas del mismo tamaño)
# - k: tamaño del motif que buscamos
# - secuencias: lista de secuencias de DNA
# Una solución s al problema sería una lista de t k-meros, cada uno 
# siguendo una secuencia distinta de DNA

from itertools import *

# Partimos de la base del problema del día anterior, la puntuación conseno
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


# obtener subsecuencia de una secuencia partiendo de una posicion y un tamaño
def obtain_subseq(seq, pos, size_subseq):
    return seq[pos:pos + size_subseq]


# Calcular subsecuencias
def cal_subseqs(seq, size_subseq):
    """
    (string, int) -> array(string)

    Encuentra todas las subsecuencias te tamaño "size_subseq" de
    la secuencia "seq"

    :param seq: la secuencia
    :param size_subseq: el tamaño de la subsecuencia
    """
    sub_seqs = []
    for pos in range(0, len(seq) - size_subseq + 1): 
        sub_seqs.append(obtain_subseq(seq, pos, size_subseq))
    
    return sub_seqs


# Calcular el número de diferencias entre dos cadenas
def num_differences_between_str(str1, str2):
    size_str1 = len(str1)
    size_str2 = len(str2)
    count_differences = 0    
    if size_str1 >= size_str2:
        for pos in range(size_str2):
            if str1[pos] != str2[pos]:
                count_differences += 1
            
        count_differences += size_str1 - size_str2
    else:
        for pos in range(size_str1):
            if str1[pos] != str2[pos]:
                count_differences += 1
        
        count_differences += size_str2 - size_str1
        
    

# el problema de hoy
def find_regulatory_motifs(num_seqs, len_seqs, len_motif, seqs):
    """
    (int, int, int, array(string)) -> array(int)

    Encuentra las posiciones iniciales de los motivos reguladores

    :param num_seqs: número de secuencias de DNA (t)
    :param len_seqs: longitud de las secuencias de DNA (n)
    :param len_motif: tamaño o longitud de los motivos (k)
    :param seqs: las secuencias de DNA con las que vamos a trabajar (secuencias)
    """
    solution = [] # la solución
    max_score = 0
    # todas las posibles combinaciones
    for combina in product(range(len_seqs - len_motif + 1), repeat=num_seqs):
        motifs_to_test = []

        # creamos los motifs canditatos        
        for i in range(num_seqs):
            motifs_to_test.append(seqs[i][combina[i]:combina[i] + len_motif])
        
        # Para cada conjunto de motivos a probar, calculamos su puntuación
        score, consense = puntacion_y_consenso_dic(motifs_to_test, len_motif)

        # Si la puntuación de estos motivos es mayor que la puntuación
        # máxima, la solución es este conjunto de motivos
        if max_score < score:
            max_score = score
            solution = motifs_to_test

    return (max_score, solution)


# ----------------------------------------------------------------

num_seqs = 4
len_seqs = 32
len_motif = 8
seqs = ("GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA")

max_score, regulatory_motifs = find_regulatory_motifs(num_seqs, len_seqs, len_motif, seqs)

for motifs in regulatory_motifs:
    print(motifs)