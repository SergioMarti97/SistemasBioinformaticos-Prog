# Ejercicios y problemas de Python - día: 15/11/2021

# Ejercicio 4.2 - Tema 4. Motifs: profile y consenso
# Calcular el parecido entre varios fragmentos de DNA del mismo del
# tamaño (motif) y encontrar un motif consenso entre ellos
#
# 1) calcular los contadores de nucleótidos en cada posición de un grupo de motif a estos contadores los denominaremos profile
# 2) Utilizando los contadores, calcularemos la puntuación del grupo de motif
# 3) De nuevo, utilizando los contadores calcularemos el que sería el motif consenso
# 4) Finalmente, todos los cálculos se incluirán en una función

def puntacion_y_consenso(motifs, k):
    """
    (list, int) -> tupla(puntuacion, consenso)
    
    :param motifs: lista de motifs
    :param k: el tamaño de los motifs 
    """
    # Calcular el profile
    profile = []
    for i in range(0, k):
        # ACGT orden de las columnas
        #       A  C  G  T
        line = [0, 0, 0, 0]
        
        for motif in motifs:
            if motif[i] == 'A':
                line[0] += 1
            elif motif[i] == 'C':
                line[1] += 1
            elif motif[i] == 'G':
                line[2] += 1
            else: # motif[i] == 'T'
                line[3] += 1
        
        profile.append(line)

    # Calcular la puntuación y el consenso
    score = 0
    consense = ""
    for line in profile:
        max = 0
        indx = 0
        for i in range(0, len(line)):
            if max < line[i]:
                max = line[i]
                indx = i
        
        score += max

        if indx == 0:
            consense += 'A'
        elif indx == 1:
            consense += 'C'
        elif indx == 2:
            consense += 'G'
        else:
            consense += 'T'

    return (score, consense) 


# ----------------------------------------------------------------
print("==== Ejercicio 4.2. \"Motif: profile y consenso\" ====")

motif = ["AGGTACTT", "CCATACGT", "ACGTTAGT", "ACGTCCAT", "CCGTACGG"]
k = len(motif[0])

score, consense = puntacion_y_consenso(motif, k)

for m in motif:
    print(f"{m}")

print(f"\n{consense} --> consenso\nPuntuación: {score}\nPorcentage (score/max_escore * 100): {score / float(k * len(motif)) * 100}%")

