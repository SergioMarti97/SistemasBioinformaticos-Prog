# Problema 1
#numGenes = int(input("Introduce el número de genes: "))
#numBases = int(input("Introduce el número de bases: "))

#print(numBases / numGenes)

# Problema 2
DNA = 'ATAGTTGCCGT'
revcom = DNA[::-1]
print(revcom)

Transformacion = str.maketrans("ATCG", "TAGC")
print(revcom.translate(Transformacion))