# Clase 25/10/2021

import random
import re

# Problema: Cálculo del número medio de genes por cormosoma encontrado en el genoma
# hummano. El número de genes de cada corosoma se introduce como una secunecia de enteros
# por teclado, con marca de fin -1.
def AverageGenesInCromosome():
    sumaGenes, numCromo = 0, 0
    numGenes = int(input(f"Introduce el número de genes del cromsoma {numCromo + 1}: "))

    while numGenes != -1:
        sumaGenes += numGenes
        numCromo += 1
        numGenes = int(input(f"Introduce el número de genes del cromosoma {numCromo + 1}: "))

    if numCromo > 0:
        print(f"Número de cromosomas {numCromo}\nNúmero promedio de genes por cromosoma: {sumaGenes / numCromo}")
    else:
        print("Secunecia vacia")



# Leer de fichero
def ReadFromFile(fileName):
    lines = []
    
    try:
        data = open(fileName, 'r')
        line = data.readline()
        
        while line:
            lines.append(line)
            line = data.readline()
        
        data.close()
    except IOError as e:
        print(str(e))
        print(f"No se puede abrir el fichero {fileName}")
    
    return lines



# Read from file, with resources
def ReadFromFileWithResources(fileName):
    lines = []
    
    try:
        with open(fileName, 'r') as data:
            for line in data:
                lines.append(line)
    except IOError as e:
        print(str(e))
        print(f"No se puede abrir el fichero {fileName}")

    return lines
        

# Esto escribe en un fichero
def WriteInFile(fileName, lines):
    try:
        file = open(fileName, 'w')

        for line in lines:
            file.write(line + '\n')
        
        file.close()
    except IOError as e:
        print(str(e))
        print(f"No se ha podido escribir el fichero {fileName}")



# Genera una cadena aleatoria de DNA
def RndDNA(size):
    bases = ['A', 'T', 'G', 'C']
    return "".join((random.choice(bases)) for x in range(size))



# Genera una lista de secuencias de DNA aleatorias
def RndDNAs(numSeq, sizeSeq):
    seq = []
    
    for x in range(0, numSeq):
        seq.append(RndDNA(sizeSeq))
    
    return seq



# Encuentra un motivo en una secuencia de DNA
def FindMotif(seq, motif):
    count = 0
    motif = motif.rstrip()
    pos = seq.find(motif)
        
    while pos >= 0:
        count += 1
        print(f"¡Lo he encontrado! posición: {pos}")
        print(seq + "".join(' ' for x in range(pos)) + '*' + "".join('-' for x in range(len(motif) - 2)) + '*')
        pos = seq.find(motif, pos + len(motif) + 1)
    
    print(f"He encontrado \'{motif}\' un total de {count}")    

                


# Encuentra un motivo en muchas secuencias de DNA
def FindMotifInSequences(seqs, motif):
    for i in range(0, len(seqs)):
        print(f"=== Secuencia {i} ===")
        FindMotif(seqs[i], motif)



# Programa
#AverageGenesInCromosome()

fileName = "files/sequencias.txt"

#numSeq = int(input("Introduce el número de secuencias que quieres generar: "))
#sizeSeq = int(input("Introcue el tamaño de las secuencias que quieres generar: "))
#seqs = RndDNAs(numSeq, sizeSeq)
#WriteInFile(fileName, seqs)
#print(f"Se han guardado las {len(seqs)} secuencias")

seqs = ReadFromFile(fileName)
print(f"Se han cargado las secuencias del fichero \'{fileName}\'")

motif = input("Introcue el motivo que quieres buscar: ")

while True:
    FindMotifInSequences(seqs, motif)
    motif = input("Introduce el motivo que quieres buscar: ")

    if re.match("^\s*$", motif):
        break

