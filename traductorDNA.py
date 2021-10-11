# Prueba de Python
from enum import Enum
import random as rnd
import re
import time

# Esta enumeración representa las formas de mostrar una proteína
class WaysShowProteins(Enum):
    EXTEND = 1 # Extendido
    CONDEN = 2 # Condensado o abreviado
    LETTER = 3 # Letras


# Esta clase representa un aminoácido, está representado por su nombre, su nombre reducido y su letra
class Aminoacid():

    def __init__(self, nameComplete, nameRedux, letter) -> None:
        self.nameComplete = nameComplete
        self.nameRedux = nameRedux
        self.letter = letter

# Esta clase cotiene los métodos para traducir una cadena de DNA     
class DNAtranslater():

    # Este diccionario contiene una expresión regex y un aminoácido
    mapDNATranslate = {
        "UU[UC]" : Aminoacid("Fenilanina", "Phe", "F"),   # 1
        "UU[AG]|CU." : Aminoacid("Leucina", "Leu", "L"),  # 2
        "UC.|AG[UC]" : Aminoacid("Serina", "Ser", "S"),   # 3
        "UA[UC]" : Aminoacid("Tirosina", "Tyr", "Y"),     # 4
        "UA[AG]|UGA" : Aminoacid("Stop", "[.]", "."),     # 5 <- Stop
        "UG[UC]" : Aminoacid("Cisteína", "Cys", "C"),     # 6
        "UGG" : Aminoacid("Triptofano", "Trp", "W"),      # 7

        "CC." : Aminoacid("Prolina", "Pro", "P"),         # 8
        "CA[UC]" : Aminoacid("Histidina", "His", "H"),    # 9
        "CA[AG]" : Aminoacid("Glutamina", "Gln", "Q"),    # 10
        "CG.|AG[AG]" : Aminoacid("Arginina", "Arg", "R"), # 11

        "AU[UCA]" : Aminoacid("Isoleucina", "Ile", "I"),  # 12
        "AUG" : Aminoacid("Start", "[*]", "*"),          # 13 <- Start
        "AC." : Aminoacid("Treonina", "Thr", "T"),        # 14
        "AA[UC]" : Aminoacid("Asparagina", "Asn", "N"),   # 15
        "AA[AG]" : Aminoacid("Lisina", "Lys", "K"),       # 16

        "GU." : Aminoacid("Valina", "Val", "V"),          # 17
        "GC." : Aminoacid("Alanina", "Ala", "A"),         # 18
        "GA[UC]" : Aminoacid("Ác. aspártico", "Asp", "D"),# 19
        "GA[AG]" : Aminoacid("Ác. glutámico", "Glu", "E"),# 20
        "GG." : Aminoacid("Glicina", "Gly", "G")          # 21
    }

    # Este método transcribe DNA -> RNA
    @staticmethod
    def transcript(dna):
        return dna.replace('T', 'U')
    

    # Este método traduce un codon
    @staticmethod
    def translate_codon_with_map(codon):
        for key in DNAtranslater.mapDNATranslate.keys():
            if re.match(key, codon):
                return DNAtranslater.mapDNATranslate.get(key)


    # Este método traduce una secuencia de DNA a una cadena de aminoácidos
    # Método del hashmap
    @staticmethod
    def translate_map(dna, read_guide = 1):
        seq = dna
        if seq.__contains__('T'):
            seq = DNAtranslater.transcript(dna)
        
        prot = []
        for i in range((read_guide - 1), len(seq) - 3, 3):
            prot.append(DNAtranslater.translate_codon_with_map(seq[i:(i + 3)]))
        
        return prot
    

    # Función para traducir un codon de RNA -> prot
    @staticmethod
    def translate_codon_with_elif(codon):
        if codon[0] == 'U':
            return DNAtranslater.translate_codon_firstU(codon)
        elif codon[0] == 'C':
            return DNAtranslater.translate_codon_firstC(codon)
        elif codon[0] == 'A':
            return DNAtranslater.translate_codon_firstA(codon)
        else:
            return DNAtranslater.translate_codon_firstG(codon)


    # Función para traducir un codon cuya primera letra sea U
    @staticmethod
    def translate_codon_firstU(codon):
        if codon[1] == 'U':
            if codon[2] == 'U':
                return Aminoacid("Fenilanina", "Phe", "F") # Fenilalanina
            elif codon[2] == 'C':
                return Aminoacid("Fenilanina", "Phe", "F") # Fenilalanina
            elif codon[2] == 'A':
                return Aminoacid("Leucina", "Leu", "L") # Leucina
            else: 
                return Aminoacid("Leucina", "Leu", "L") # Leucina
        elif codon[1] == 'C':
            if codon[2] == 'U':
                return Aminoacid("Serina", "Ser", "S") # Serina
            elif codon[2] == 'C':
                return Aminoacid("Serina", "Ser", "S") # Serina
            elif codon[2] == 'A':
                return Aminoacid("Serina", "Ser", "S") # Serina
            else: 
                return Aminoacid("Serina", "Ser", "S") # Serina
        elif codon[1] == 'A':
            if codon[2] == 'U':
                return Aminoacid("Tirosina", "Tyr", "Y") # Tirosina
            elif codon[2] == 'C':
                return Aminoacid("Tirosina", "Tyr", "Y") # Tirosina
            elif codon[2] == 'A':
                return Aminoacid("Stop", "[.]", ".") # Stop
            else: 
                return Aminoacid("Stop", "[.]", ".") # Stop
        else:
            if codon[2] == 'U':
                return Aminoacid("Cisteína", "Cys", "C") # Cisteina
            elif codon[2] == 'C':
                return Aminoacid("Cisteína", "Cys", "C") # Cisteina
            elif codon[2] == 'A':
                return Aminoacid("Stop", "[.]", ".") # Stop
            else: 
                return Aminoacid("Triptofano", "Trp", "W") # Triptofano
        

    # Función para traducir un codon cuya primera letra sea C
    @staticmethod
    def translate_codon_firstC(codon):
        if codon[1] == 'U':
            if codon[2] == 'U':
                return Aminoacid("Leucina", "Leu", "L") # Leucina
            elif codon[2] == 'C':
                return Aminoacid("Leucina", "Leu", "L") # Leucina
            elif codon[2] == 'A':
                return Aminoacid("Leucina", "Leu", "L") # Leucina
            else: 
                return Aminoacid("Leucina", "Leu", "L") # Leucina
        elif codon[1] == 'C':
            if codon[2] == 'U':
                return Aminoacid("Prolina", "Pro", "P") # Prolina
            elif codon[2] == 'C':
                return Aminoacid("Prolina", "Pro", "P") # Prolina
            elif codon[2] == 'A':
                return Aminoacid("Prolina", "Pro", "P") # Prolina
            else: 
                return Aminoacid("Prolina", "Pro", "P") # Prolina
        elif codon[1] == 'A':
            if codon[2] == 'U':
                return Aminoacid("Histidina", "His", "H") # Histidina
            elif codon[2] == 'C':
                return Aminoacid("Histidina", "His", "H") # Histidina
            elif codon[2] == 'A':
                return Aminoacid("Glutamina", "Gln", "Q") # Glutamina
            else: 
                return Aminoacid("Glutamina", "Gln", "Q") # Glutamina
        else:
            if codon[2] == 'U':
                return Aminoacid("Arginina", "Arg", "R") # Arginina
            elif codon[2] == 'C':
                return Aminoacid("Arginina", "Arg", "R") # Arginina
            elif codon[2] == 'A':
                return Aminoacid("Arginina", "Arg", "R") # Arginina
            else: 
                return Aminoacid("Arginina", "Arg", "R") # Arginina


    # Función para traducir un codon cuya primera letra sea A
    @staticmethod
    def translate_codon_firstA(codon):
        if codon[1] == 'U':
            if codon[2] == 'U':
                return Aminoacid("Isoleucina", "Ile", "I") # Isoleucina
            elif codon[2] == 'C':
                return Aminoacid("Isoleucina", "Ile", "I") # Isoleucina
            elif codon[2] == 'A':
                return Aminoacid("Isoleucina", "Ile", "I") # Isoleucina
            else: 
                return Aminoacid("Start", "[*]", "*") # Metionina
        elif codon[1] == 'C':
            if codon[2] == 'U':
                return Aminoacid("Treonina", "Thr", "T") # Treonina
            elif codon[2] == 'C':
                return Aminoacid("Treonina", "Thr", "T") # Treonina
            elif codon[2] == 'A':
                return Aminoacid("Treonina", "Thr", "T") # Treonina
            else: 
                return Aminoacid("Treonina", "Thr", "T") # Treonina
        elif codon[1] == 'A':
            if codon[2] == 'U':
                return Aminoacid("Asparagina", "Asn", "N") # Asparagina
            elif codon[2] == 'C':
                return Aminoacid("Asparagina", "Asn", "N") # Asparagina
            elif codon[2] == 'A':
                return Aminoacid("Lisina", "Lys", "K") # Lisina
            else: 
                return Aminoacid("Lisina", "Lys", "K") # Lisina
        else:
            if codon[2] == 'U':
                return Aminoacid("Serina", "Ser", "S") # Serina
            elif codon[2] == 'C':
                return Aminoacid("Serina", "Ser", "S") # Serina
            elif codon[2] == 'A':
                return Aminoacid("Arginina", "Arg", "R") # Arginina
            else: 
                return Aminoacid("Arginina", "Arg", "R") # Arginina


    # Función para traducir un codon cuya primera letra sea G
    @staticmethod
    def translate_codon_firstG(codon):
        if codon[1] == 'U':
            if codon[2] == 'U':
                return Aminoacid("Valina", "Val", "V") # Valina
            elif codon[2] == 'C':
                return Aminoacid("Valina", "Val", "V") # Valina
            elif codon[2] == 'A':
                return Aminoacid("Valina", "Val", "V") # Valina
            else: 
                return Aminoacid("Valina", "Val", "V") # Valina
        elif codon[1] == 'C':
            if codon[2] == 'U':
                return Aminoacid("Alanina", "Ala", "A") # Alanina
            elif codon[2] == 'C':
                return Aminoacid("Alanina", "Ala", "A") # Alanina
            elif codon[2] == 'A':
                return Aminoacid("Alanina", "Ala", "A") # Alanina
            else: 
                return Aminoacid("Alanina", "Ala", "A") # Alanina
        elif codon[1] == 'A':
            if codon[2] == 'U':
                return Aminoacid("Ác. aspártico", "Asp", "D") # Ac. aspartico
            elif codon[2] == 'C':
                return Aminoacid("Ác. aspártico", "Asp", "D") # Ac. aspartico
            elif codon[2] == 'A':
                return Aminoacid("Ác. glutámico", "Glu", "E") # Ac. glutamico
            else: 
                return Aminoacid("Ác. glutámico", "Glu", "E") # Ac. glutamico
        else:
            if codon[2] == 'U':
                return Aminoacid("Glicina", "Gly", "G") # Glicina
            elif codon[2] == 'C':
                return Aminoacid("Glicina", "Gly", "G") # Glicina
            elif codon[2] == 'A':
                return Aminoacid("Glicina", "Gly", "G") # Glicina
            else: 
                return Aminoacid("Glicina", "Gly", "G") # Glicina


    # Este método traduce una secuencia de DNA a una cadena de aminácidos
    # Método del elif
    @staticmethod
    def translate_elif(dna, read_guide = 1):
        seq = dna
        if seq.__contains__('T'):
            seq = DNAtranslater.transcript(dna)
        
        prot = []
        for i in range((read_guide - 1), len(seq) - 3, 3):
            prot.append(DNAtranslater.translate_codon_with_elif(seq[i:(i + 3)]))
        
        return prot


# Función para mostrar una proteína
def show_prot(prot, wayShowProt = 1):
    prot_seq = ""
    for index in range(0, len(prot)):
        if wayShowProt == WaysShowProteins.EXTEND:
            prot_seq += f"{index}: {prot[index].nameComplete}\n"
        elif wayShowProt == WaysShowProteins.CONDEN:
            prot_seq += prot[index].nameRedux + '-'
        elif wayShowProt == WaysShowProteins.LETTER:
            prot_seq += prot[index].letter
        else:
            prot = "."
    print(prot_seq)


# Funcion para crear una secuencia de ADN aleatoria
def rnd_seq(lenght):
    bases = ['A', 'C', 'T', 'G']
    seq = ""
    for i in range(0, lenght):
        seq = seq + bases[rnd.randint(0, 3)]
    return seq


# Función para calcular el % de GC de una secuencia
def count_percentageGC(seq):
    countA, countC, countT, countG, countExtra = 0, 0, 0, 0, 0
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
        return translate_codon_firstU(codon)
    elif codon[0] == 'C':
        return translate_codon_firstC(codon)
    elif codon[0] == 'A':
        return translate_codon_firstA(codon)
    else:
        return translate_codon_firstG(codon)


# Función para traducir un codon cuya primera letra sea U
def translate_codon_firstU(codon):
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
    

# Función para traducir un codon cuya primera letra sea C
def translate_codon_firstC(codon):
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


# Función para traducir un codon cuya primera letra sea A
def translate_codon_firstA(codon):
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


# Función para traducir un codon cuya primera letra sea G
def translate_codon_firstG(codon):
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
def translate_seq(seq):
    if seq.__contains__('T'):
        seq = seq.replace('T', 'U')
    
    prot = ""
    for i in range(0, len(seq) - 3, 3):
        prot += translate_codon(seq[i:(i + 3)])
    
    return prot


# Función para traducir una sequencia de DNA/RNA a prot
def obtain_proteins(seq):
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


# COMIENZO DEL PROGRAMA
lenght = 30
lenght_divisore_line = 15
print(f"Generando la cadena de DNA. Longitud: {lenght}pb")
seq = rnd_seq(lenght)
print(seq)
GCpercentage = count_percentageGC(rnd_seq(lenght))
ATpercetage = 1 - GCpercentage
print(f"{GCpercentage * 100}% GC | {ATpercetage * 100}% AT")
print(f"{'-' * lenght_divisore_line}")

num_reps = 1000

print(f"(1) Método del diccionario para traducir la secuencia de DNA\nRepeticiones de la traducción: {num_reps}")
sum = 0
seq_aa = []
for i in range(0, num_reps):
    start = time.time()
    seq_aa = DNAtranslater.translate_map(seq)
    end = time.time()
    sum += (end - start)
print(f"Tiempo medio: {(sum / num_reps) * 1000}ms\n{'-' * lenght_divisore_line}")
show_prot(seq_aa, WaysShowProteins.LETTER)
print(f"{'-' * lenght_divisore_line}")

print(f"(2) Método del elif para traducir una secuencia de DNA\nRepeticiones de la traducción: {num_reps}")
sum = 0
for i in range(0, num_reps):
    start = time.time()
    seq_aa = DNAtranslater.translate_codon_with_elif(seq)
    end = time.time()
    sum += (end - start)
print(f"Tiempo medio: {(sum / num_reps) * 1000}ms\n{'-' * lenght_divisore_line}")
show_prot(seq_aa, WaysShowProteins.LETTER)
print(f"{'-' * lenght_divisore_line}")

print("** PROTEÍNAS **")
prots = obtain_proteins(seq)
print(f"{prots}\nNúmero de proteínas: {len(prots)}")