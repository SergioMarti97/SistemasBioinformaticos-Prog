# Problemas día 02/11/2021

# Capitales del mundo
hCaptiales = {
    "Reino Unido" : "Londres",
    "Peru" : "Lima",
    "Francia" : "Paris",
    "Portugal" : "Lisboa",
    "España" : "Madrid"
}

print("=== metodo 1 ===")
for pais, capital in hCaptiales.items():
    print("País: " + pais + ", captial: " + capital)

print("=== metodo 2 ===")
for pais in hCaptiales:
    capital = hCaptiales[pais]
    print("País: " + pais + ", capital: " + capital)


# Problema: Contar el número de cada tipo de nucléotido en una secuencia de DNA.
# Se leerá el fichero de entrada carácter a carácter
print("=== Contar las bases nitrogenadas de un archivo con secuencias de DNA ===")

# protFileName = input("Escriba el nombre del fichero que contiene la secuencia de DNA: ") # <- para evitar que me pida meter por teclado todo el rato el archivo
protFileName = "files/sequencias.txt"
protFileName = protFileName.rstrip()

try:
    protInFile = open(protFileName)
    
    contar = {
        'A' : 0,
        'T' : 0,
        'G' : 0,
        'C' : 0,
    }
    bases = ('A', 'T', 'G', 'C')
    errores = 0
    
    base = protInFile.read(1)
    
    # Contadura
    while base:
        if base in bases:
            contar[base] += 1
        else:
            print("No se reconoce esta base: ", base)
            errores += 1
        base = protInFile.read(1)
    
    protInFile.close()

    # Escritura
    for base in bases:
        print(f"{base} = {contar[base]}")
    
    print(f"Errors = {errores}")

except IOError as e :
    print(e)

# Traducir una secuencia de DNA
# Una función que con ayuda de un diccionario devuelva el aminoácido correspondiente a un codon
print("=== Traducción de RNA ===")

dicDNATranslate = {
        "UUU" : "F",   # 1
        "UUC" : "F",   # 1
        
        "UUA" : "L",  # 2
        "UUG" : "L",  # 2
        "CUU" : "L",  # 2
        "CUC" : "L",  # 2
        "CUA" : "L",  # 2
        "CUG" : "L",  # 2

        "UCU" : "S",   # 3
        "UCC" : "S",   # 3
        "UCA" : "S",   # 3
        "UCG" : "S",   # 3
        "AGU" : "S",   # 3
        "AGC" : "S",   # 3

        "UAU" : "Y",     # 4
        "UAC" : "Y",     # 4

        "UAA" : ".",     # 5 <- Stop
        "UAG" : ".",     # 5 <- Stop
        "UGA" : ".",     # 5 <- Stop

        "UGU" : "C",     # 6
        "UGC" : "C",     # 6

        "UGG" : "W",      # 7

        "CCU" : "P",         # 8
        "CCC" : "P",         # 8
        "CCA" : "P",         # 8
        "CCG" : "P",         # 8

        "CAU" : "H",    # 9
        "CAC" : "H",    # 9

        "CAA" : "Q",    # 10
        "CAG" : "Q",    # 10

        "CGU" : "R", # 11
        "CGC" : "R", # 11
        "CGA" : "R", # 11
        "CGG" : "R", # 11
        "AGA" : "R", # 11
        "AGG" : "R", # 11

        "AUU" : "I",  # 12
        "AUC" : "I",  # 12
        "AUA" : "I",  # 12

        "AUG" : "*",          # 13 <- Start
        
        "ACU" : "T",        # 14
        "ACC" : "T",        # 14
        "ACA" : "T",        # 14
        "ACG" : "T",        # 14
        
        "AAU" : "N",   # 15
        "AAC" : "N",   # 15
        
        "AAA" : "K",       # 16
        "AAG" : "K",       # 16

        "GUU" : "V",          # 17
        "GUC" : "V",          # 17
        "GUA" : "V",          # 17
        "GUG" : "V",          # 17
        
        "GCU" : "A",         # 18
        "GCC" : "A",         # 18
        "GCA" : "A",         # 18
        "GCG" : "A",         # 18
        
        "GAU" : "D",   # 19
        "GAC" : "D",   # 19
        
        "GAA" : "E",   # 20
        "GAG" : "E",   # 20
        
        "GGU" : "G",          # 21
        "GGC" : "G",          # 21
        "GGA" : "G",          # 21
        "GGG" : "G"         # 21
}

def CodonTranslateAA(codon):
    if codon in dicDNATranslate:
        return dicDNATranslate.get(codon)


rna = "CGACGUCUUCGUACGGGACUAGCUCGUGUCGGUCGC"
prot = ""

# algoritmo
for i in range(0, len(rna) // 3):
    codon = rna[3 * i : 3 * i + 3]
    prot += CodonTranslateAA(codon)

print(f"RNA:\n{rna}\nProteina:\n{prot}")