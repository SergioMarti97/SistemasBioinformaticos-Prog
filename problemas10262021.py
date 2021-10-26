# Clase 26/10/2021

# Funciones

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


def CountRecusivo(seq, i, count):
    if (i == len(seq) - 1) or (seq[i] == '\n'):
        print(f"Apariciones de A: {count[0]}\nApariciones de T: {count[1]}\nApariciones de C: {count[2]}\nApiriciones de G: {count[3]}\nErrores: {count[4]}")
        return

    base = seq[i]

    if base == 'A':
        count[0] += 1
    elif base == 'T':
        count[1] += 1
    elif base == 'C':
        count[2] += 1
    elif base == 'G':
        count[3] += 1
    else:
        count[4] += 1

    i += 1
    CountRecusivo(seq, i, count)


# Contar cada tipo de nucleotido en una secuencia de DNA

seqs = ReadFromFile("files/sequencias.txt")

countA, countT, countC, countG, errores = 0, 0, 0, 0, 0 

print(f"Cadena. Tamaño: {len(seqs[0])}\n{seqs[0]}")

for base in seqs[0]:
    if base == '\n':
        continue

    if base == 'A':
        countA += 1
    elif base == 'T':
        countT += 1
    elif base == 'C':
        countC += 1
    elif base == 'G':
        countG += 1
    else:
        errores += 1
    
print(f"Apariciones de A: {countA}\nApariciones de T: {countT}\nApariciones de C: {countC}\nApiriciones de G: {countG}\nErrores: {errores}")

count = [0, 0, 0, 0, 0]
CountRecusivo(seqs[0], 0, count)
