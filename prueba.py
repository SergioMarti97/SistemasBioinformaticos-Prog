# Prueba de Python
import random as rnd

# Funcion para crear una secuencia de ADN aleatoria
def rnd_seq(lenght):
    bases = ['A', 'C', 'T', 'G']
    seq = ""
    for i in range(0, lenght):
        seq = seq + bases[rnd.randint(0, 3)]
    return seq


# Función para calcular el % de GC de una secuencia
def count_percentageGC(seq):
    countA = 0 
    countC = 0 
    countT = 0
    countG = 0 
    countExtra = 0
    for i in range(0, len(seq)):
        if seq[i] == 'A':
            countA = countA + 1
        elif seq[i] == 'C':
            countC = countC + 1
        elif seq[i] == 'T':
            countT = countT + 1
        elif seq[i] == 'G':
            countG = countG + 1
        else:
            countExtra = countExtra + 1
    return (countG + countC) / len(seq)


# Función para traducir un codon de RNA -> prot
def translate_codon(codon):
    if codon[0] == 'U':
        if codon[1] == 'U':
            if codon[2] == 'U':
                return 'F' # Leucina
            elif codon[2] == 'C':
                return 'F' # Leucina
            elif codon[2] == 'A':
                return 'L' # Leucina
            else: 
                return 'L' # Leucina
        elif codon[1] == 'C':
            if codon[2] == 'U':
                return 'S' # Serina
            elif codon[2] == 'C':
                return 'S' # Serina
            elif codon[2] == 'A':
                return 'S' # Serina
            else: 
                return 'S' # Serina
        elif codon[1] == 'A':
            if codon[2] == 'U':
                return 'Y' # Tirosina
            elif codon[2] == 'C':
                return 'Y' # Tirosina
            elif codon[2] == 'A':
                return '.' # Stop
            else: 
                return '.' # Stop
        else:
            if codon[2] == 'U':
                return 'C' # Cisteina
            elif codon[2] == 'C':
                return 'C' # Cisteina
            elif codon[2] == 'A':
                return '.' # Stop
            else: 
                return 'W' # Triptofano
    elif codon[0] == 'C':
        if codon[1] == 'U':
            if codon[2] == 'U':
                return 'L' # Leucina
            elif codon[2] == 'C':
                return 'L' # Leucina
            elif codon[2] == 'A':
                return 'L' # Leucina
            else: 
                return 'L' # Leucina
        elif codon[1] == 'C':
            if codon[2] == 'U':
                return 'P' # Prolina
            elif codon[2] == 'C':
                return 'P' # Prolina
            elif codon[2] == 'A':
                return 'P' # Prolina
            else: 
                return 'P' # Prolina
        elif codon[1] == 'A':
            if codon[2] == 'U':
                return 'H' # Histidina
            elif codon[2] == 'C':
                return 'H' # Histidina
            elif codon[2] == 'A':
                return 'Q' # Glutamina
            else: 
                return 'Q' # Glutamina
        else:
            if codon[2] == 'U':
                return 'R' # Arginina
            elif codon[2] == 'C':
                return 'R' # Arginina
            elif codon[2] == 'A':
                return 'R' # Arginina
            else: 
                return 'R' # Arginina
    elif codon[0] == 'A':
        if codon[1] == 'U':
            if codon[2] == 'U':
                return 'I' # Isoleucina
            elif codon[2] == 'C':
                return 'I' # Isoleucina
            elif codon[2] == 'A':
                return 'I' # Isoleucina
            else: 
                return '*' # Metionina
        elif codon[1] == 'C':
            if codon[2] == 'U':
                return 'T' # Treonina
            elif codon[2] == 'C':
                return 'T' # Treonina
            elif codon[2] == 'A':
                return 'T' # Treonina
            else: 
                return 'T' # Treonina
        elif codon[1] == 'A':
            if codon[2] == 'U':
                return 'N' # Asparagina
            elif codon[2] == 'C':
                return 'N' # Asparagina
            elif codon[2] == 'A':
                return 'K' # Lisina
            else: 
                return 'K' # Lisina
        else:
            if codon[2] == 'U':
                return 'S' # Serina
            elif codon[2] == 'C':
                return 'S' # Serina
            elif codon[2] == 'A':
                return 'R' # Arginina
            else: 
                return 'R' # Arginina
    else:
        if codon[1] == 'U':
            if codon[2] == 'U':
                return 'V' # Valina
            elif codon[2] == 'C':
                return 'V' # Valina
            elif codon[2] == 'A':
                return 'V' # Valina
            else: 
                return 'V' # Valina
        elif codon[1] == 'C':
            if codon[2] == 'U':
                return 'A' # Alanina
            elif codon[2] == 'C':
                return 'A' # Alanina
            elif codon[2] == 'A':
                return 'A' # Alanina
            else: 
                return 'A' # Alanina
        elif codon[1] == 'A':
            if codon[2] == 'U':
                return 'D' # Ac. aspartico
            elif codon[2] == 'C':
                return 'D' # Ac. aspartico
            elif codon[2] == 'A':
                return 'E' # Ac. glutamico
            else: 
                return 'E' # Ac. glutamico
        else:
            if codon[2] == 'U':
                return 'G' # Glicina
            elif codon[2] == 'C':
                return 'G' # Glicina
            elif codon[2] == 'A':
                return 'G' # Glicina
            else: 
                return 'G' # Glicina 


# Función para traducir una secuencia de DNA/RNA a prot
def translate_seq2(seq):
    if seq.__contains__('T'):
        seq = seq.replace('T', 'U')
    
    prot = ""
    for i in range(0, len(seq) - 3, 3):
        prot += translate_codon(seq[i:(i + 3)])
    
    return prot


# Función para traducir una sequencia de DNA/RNA a prot
def translate_seq(seq):
    if seq.__contains__('T'):
        seq = seq.replace('T', 'U')
    
    prot = ""
    prots = []
    isReading = False

    for i in range(0, len(seq) - 3, 3):
        a = translate_codon(seq[i:(i + 3)])
        
        if a == '.':
            if isReading:
                prots.append(prot)
            isReading = False
        
        if a == "*":
            isReading = True
            prot = ""
        
        if isReading:
            prot = prot + a

    return prots


lenght = 1024
seq = rnd_seq(lenght)
print(seq)
GCpercentage = count_percentageGC(rnd_seq(lenght))
ATpercetage = 1 - GCpercentage
print(f"{GCpercentage * 100}% GC | {ATpercetage * 100}% AT")
prot_seq = translate_seq2(seq)
prots = translate_seq(seq)
print(f"{prot_seq}\n{prots}\nLongitud DNA: {len(seq)}\nLongitud prot: {len(prots)}")