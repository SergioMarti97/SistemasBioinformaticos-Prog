# APUNTES DIA: 08/11/2021

# Calcular la expresion de dna

# Esta función calcula el numero de apariciones de una subcadena en una cadena
import re


def countAppearancesSubSeqInSeq(bigSeq, seqToCount):
    count = 0
    end = len(bigSeq) - (len(seqToCount) - 1)
    for i in range(0, end):
        subSequence = bigSeq[i : i + len(seqToCount)]
        if subSequence == seqToCount:
            count += 1
        
    return count


# Esta función calcula el número de apariciones de una subcadena en una cadena y
# muestra los alineamientos
def showAlignment(bigSeq, seqToCount):
    count = 0
    end = len(bigSeq) - (len(seqToCount) - 1)
    
    for i in range(0, end):
        subSequence = bigSeq[i : i + len(seqToCount)]
        if subSequence == seqToCount:
            count += 1
            print(f"==== Alineamiento {count} posición: {i} ====")
            print(bigSeq)
            print("".join(' ' for x in range(i)) + seqToCount)
        
    return count


# Esta función cuenta el número de apariciones de una letra en una secuencia
def countBaseInSeq(seq, base):
    count = 0
    for i in range(len(seq)):
        if seq[i:i+1] == base:
            count += 1
    return count


# Esta función calcula el porcentage teorico de aparicion de una subsecuencia en una secuencia
def calTeoricalPercentageApearance(bigSeq, subSeq):
    apearancesA = countBaseInSeq(bigSeq, 'A') / float(len(bigSeq))
    apearancesT = countBaseInSeq(bigSeq, 'T') / float(len(bigSeq))
    apearancesG = countBaseInSeq(bigSeq, 'G') / float(len(bigSeq))
    apearancesC = countBaseInSeq(bigSeq, 'C') / float(len(bigSeq))

    countA, countT, countG, countC = 0, 0, 0, 0
    for i in range(len(subSeq)):
        if subSeq[i:i+1] == 'A':
            countA += 1
        elif subSeq[i:i+1] == 'T':
            countT += 1
        elif subSeq[i:i+1] == 'G':
            countG += 1
        else: #subSeq[i:i+1] == 'C'
            countC += 1
    
    val = 1
    if countA != 0:
        val *= (countA * apearancesA)
    if countT != 0:
        val *= (countT * apearancesT)
    if countG != 0:
        val *= (countG * apearancesG)
    if countC != 0:
        val *= (countC * apearancesC)
    
    return val


# Problema: palabras más frecuentes
def palabrasMasFrecuentes(seq, k):

    # Creamos el diccionario
    dic = {}

    # Calculamos el punto final para recorrer la secuencia y calcular las subsecuencias
    end = len(seq) - (k - 1)
    for i in range(0, end):
        subSequence = seq[i : i + k]
        if subSequence in dic.keys():
            dic[subSequence] += 1
        else:
            dic[subSequence] = 1

    # Sacamos el contador más grande
    maxApearances = 0
    for i in dic.values():
        if maxApearances < i:
            maxApearances = i

    # Sacamos las subsecuencias que tienen el máximo de apariciones 
    subSeqs = []
    for key in dic.keys():
        if dic[key] == maxApearances:
            subSeqs.append(key)

    return subSeqs


# =============== PROGRAMA =============== # 
rna = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"
seqToFind = "GT"
count = 0

print(f"Longitud de la cadena de RNA: {len(rna)}")
    
percentageApearances = showAlignment(rna, seqToFind) / float(len(rna))

print(f"Porcentage de aparicion de '{seqToFind}': {percentageApearances}")

countG = countBaseInSeq(rna, seqToFind[0:1]) / float(len(rna))
countT = countBaseInSeq(rna, seqToFind[1:2]) / float(len(rna))
percentageApearancesCalculated = countG * countT
percentageApearancesCalculated = calTeoricalPercentageApearance(rna, seqToFind)
print(f"Porcentage aparicion {seqToFind[0:1]}: {countG}\naparicion {seqToFind[1:2]}: {countT}\nAparicion calculada de {seqToFind}: {percentageApearancesCalculated}")

if percentageApearancesCalculated > percentageApearances:
    print(f"La secuencia {seqToFind} se encuentra sub-expresada")
else:
    print(f"La secuencia {seqToFind} se ecuentra sobre-expresada")

seqs = palabrasMasFrecuentes(rna, 4)

for s in seqs:
    print(f"{s}")

