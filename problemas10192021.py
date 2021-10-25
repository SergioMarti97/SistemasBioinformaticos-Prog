# Clase 19/10/2021

# FUNCIONES

# Dadas dos duraciones expresadas como: hora, minutos y segundos, escribir un algorithmo que obtenga
# la suma expresdas de igual modo

def DurationToSeconds(dur):
    return dur['h'] * 3600 + dur['m'] * 60 + dur['s']


def SecondsToDuration(seconds):
    dur = {}
    dur['h'] = int(seconds // 3600)
    dur['m'] = int((seconds % 3600) // 60)
    dur['s'] = int((seconds % 3600) % 60)
    return dur 

# Algoritmo de sumar
def SumarD(dur1, dur2):
    segDur1 = DurationToSeconds(dur1)
    segDur2 = DurationToSeconds(dur2)
    totSeg = segDur1 + segDur2
    return SecondsToDuration(totSeg)


def SumarDTres(dur1, dur2, dur3):
    return SumarD(SumarD(dur1, dur2), dur3)


def ShowDur(dur):
    print("%dh %dmin %dseg".format(dur['h'], dur['m'], dur['s']))


def CompareD(dur1, dur2):
    return DurationToSeconds(dur1) > DurationToSeconds(dur2)


# Crea una función que devuelva el día siguiente de esa fecha
# La fecha se almacena como un diccionario donde se guarda el dia 
# 'd', el mes 'M' y el año 'A'

#  1 Enero 31
#  2 Febrero 28
#  3 Marzo 31
#  4 Abril 30
#  5 Mayo 31
#  6 Junio 30
#  7 Julio 31
#  8 Agosto 31
#  9 Septiembre 30
# 10 Octubre 31
# 11 Noviembre 30
# 12 Diciembre 31

# meses con 31: (1, 3, 5, 7, 8, 10, 12)
# meses con 30: (4, 6, 9, 11)
# meses con 28/29: 2
def SigFecha(date):
    date['d'] += 1
    if date['M'] == 2:
        if date['d'] > 28:
            date['d'] = 0
            date['M'] += 1
    elif date['M'] in (1, 3, 5, 7, 8, 10, 12):
        if date['d'] > 31:
            date['d'] = 0
            date['M'] += 1
    else:
        if date['d'] > 30:
            date['d'] = 0
            date['M'] += 1
    
    if date['M'] > 12:
        date['M'] = 1
        date['A'] += 1

    return date


# Esta clase representa un aminoácido, está representado por su nombre, su nombre reducido y su letra
class Aminoacid():

    def __init__(self, nameComplete, nameRedux, letter) -> None:
        self.nameComplete = nameComplete
        self.nameRedux = nameRedux
        self.letter = letter


# Una función que con ayuda de un diccionario devuelva el aminoácido correspondiente a un codon
dicDNATranslate = {
        "UUU" : Aminoacid("Fenilanina", "Phe", "F"),   # 1
        "UUC" : Aminoacid("Fenilanina", "Phe", "F"),   # 1
        
        "UUA" : Aminoacid("Leucina", "Leu", "L"),  # 2
        "UUG" : Aminoacid("Leucina", "Leu", "L"),  # 2
        "CUU" : Aminoacid("Leucina", "Leu", "L"),  # 2
        "CUC" : Aminoacid("Leucina", "Leu", "L"),  # 2
        "CUA" : Aminoacid("Leucina", "Leu", "L"),  # 2
        "CUG" : Aminoacid("Leucina", "Leu", "L"),  # 2

        "UCU" : Aminoacid("Serina", "Ser", "S"),   # 3
        "UCC" : Aminoacid("Serina", "Ser", "S"),   # 3
        "UCA" : Aminoacid("Serina", "Ser", "S"),   # 3
        "UCG" : Aminoacid("Serina", "Ser", "S"),   # 3
        "AGU" : Aminoacid("Serina", "Ser", "S"),   # 3
        "AGC" : Aminoacid("Serina", "Ser", "S"),   # 3

        "UAU" : Aminoacid("Tirosina", "Tyr", "Y"),     # 4
        "UAC" : Aminoacid("Tirosina", "Tyr", "Y"),     # 4

        "UAA" : Aminoacid("Stop", "[.]", "."),     # 5 <- Stop
        "UAG" : Aminoacid("Stop", "[.]", "."),     # 5 <- Stop
        "UGA" : Aminoacid("Stop", "[.]", "."),     # 5 <- Stop

        "UGU" : Aminoacid("Cisteína", "Cys", "C"),     # 6
        "UGC" : Aminoacid("Cisteína", "Cys", "C"),     # 6

        "UGG" : Aminoacid("Triptofano", "Trp", "W"),      # 7

        "CCU" : Aminoacid("Prolina", "Pro", "P"),         # 8
        "CCC" : Aminoacid("Prolina", "Pro", "P"),         # 8
        "CCA" : Aminoacid("Prolina", "Pro", "P"),         # 8
        "CCG" : Aminoacid("Prolina", "Pro", "P"),         # 8

        "CAU" : Aminoacid("Histidina", "His", "H"),    # 9
        "CAC" : Aminoacid("Histidina", "His", "H"),    # 9

        "CAA" : Aminoacid("Glutamina", "Gln", "Q"),    # 10
        "CAG" : Aminoacid("Glutamina", "Gln", "Q"),    # 10

        "CGU" : Aminoacid("Arginina", "Arg", "R"), # 11
        "CGC" : Aminoacid("Arginina", "Arg", "R"), # 11
        "CGA" : Aminoacid("Arginina", "Arg", "R"), # 11
        "CGG" : Aminoacid("Arginina", "Arg", "R"), # 11
        "AGA" : Aminoacid("Arginina", "Arg", "R"), # 11
        "AGG" : Aminoacid("Arginina", "Arg", "R"), # 11

        "AUU" : Aminoacid("Isoleucina", "Ile", "I"),  # 12
        "AUC" : Aminoacid("Isoleucina", "Ile", "I"),  # 12
        "AUA" : Aminoacid("Isoleucina", "Ile", "I"),  # 12

        "AUG" : Aminoacid("Start", "[*]", "*"),          # 13 <- Start
        
        "ACU" : Aminoacid("Treonina", "Thr", "T"),        # 14
        "ACC" : Aminoacid("Treonina", "Thr", "T"),        # 14
        "ACA" : Aminoacid("Treonina", "Thr", "T"),        # 14
        "ACG" : Aminoacid("Treonina", "Thr", "T"),        # 14
        
        "AAU" : Aminoacid("Asparagina", "Asn", "N"),   # 15
        "AAC" : Aminoacid("Asparagina", "Asn", "N"),   # 15
        
        "AAA" : Aminoacid("Lisina", "Lys", "K"),       # 16
        "AAG" : Aminoacid("Lisina", "Lys", "K"),       # 16

        "GUU" : Aminoacid("Valina", "Val", "V"),          # 17
        "GUC" : Aminoacid("Valina", "Val", "V"),          # 17
        "GUA" : Aminoacid("Valina", "Val", "V"),          # 17
        "GUG" : Aminoacid("Valina", "Val", "V"),          # 17
        
        "GCU" : Aminoacid("Alanina", "Ala", "A"),         # 18
        "GCC" : Aminoacid("Alanina", "Ala", "A"),         # 18
        "GCA" : Aminoacid("Alanina", "Ala", "A"),         # 18
        "GCG" : Aminoacid("Alanina", "Ala", "A"),         # 18
        
        "GAU" : Aminoacid("Ác. aspártico", "Asp", "D"),   # 19
        "GAC" : Aminoacid("Ác. aspártico", "Asp", "D"),   # 19
        
        "GAA" : Aminoacid("Ác. glutámico", "Glu", "E"),   # 20
        "GAG" : Aminoacid("Ác. glutámico", "Glu", "E"),   # 20
        
        "GGU" : Aminoacid("Glicina", "Gly", "G"),          # 21
        "GGC" : Aminoacid("Glicina", "Gly", "G"),          # 21
        "GGA" : Aminoacid("Glicina", "Gly", "G"),          # 21
        "GGG" : Aminoacid("Glicina", "Gly", "G")          # 21
}


def CodonTranslateAA(codon):
    if codon in dicDNATranslate:
        return dicDNATranslate.get(codon)
    else:
        return "No se ha encontrado el aminoácido correspondiente a ese codon"


# En python el asterisco índica que es una lista
def IndeterminadosPosicion(*args):
    for args in args:
        print(args)


# La misma forma de hacer lo de antes pero recursivomente. La función se llama a si misma
def IndeterminadosPosicionRecursivo(count, args):
    if count >= len(args):
        return
    else:
        print(args[count])
        count += 1 
        IndeterminadosPosicionRecursivo(count, args)


# de forma recursiva xq estoy loco @.@
def RecursivoContarA(car, count):
    if car == '#':
        return count
    else:

        if car == 'A':
            count += 1
        
        car = input("Introduce un carácter: ")
        
        RecursivoContarA(car, count)
    

# Programa

# Sumar dos duraciones distintas, guardadas como un diccionario
print("========= Ejercicio de sumar dos duraciones distintas =========")

dur1 = {}
dur2 = {}

dur1['h'] = 1 #int(input("Hora duración 1: "))
dur1['m'] = 20 #int(input("Minuto duración 1: "))
dur1['s'] = 34 #int(input("Segundo duración 1: "))

dur2['h'] = 2 #int(input("Hora duración 2: "))
dur2['m'] = 30 #int(input("Minuto duración 2: "))
dur2['s'] = 12 #int(input("Segundo duración 2: "))

print("Las dos duraciones: ")
ShowDur(dur1)
ShowDur(dur1)

print("La duracion total: ")
durTot = SumarD(dur1, dur2)
ShowDur(durTot)

print("Sumar las dos duraciones iniciales más la suma de las dos duraciones: ")
durTot = SumarDTres(dur1, dur2, durTot)
print(durTot)

# Algoritmo para obtener el dia de después, dada una fecha
print("========= Ejercicio del algoritmo para obtener el dia siguiente a una fecha dada =========")

date = {
    'A' : 2021,
    'M' : 2,
    'd' : 28
}

print(f"El día después de {date} es {SigFecha(date)}")

# Obtener un aminoácido a partir de un codon, tres bases nitrogenadas
print("========= Ejercicio para obtener un aminacido a partir de un triplete =========")

codon = 'AAA'
print(f"El codon {codon} codifica el aminoácido: {CodonTranslateAA('AAA').nameComplete}")

# Función recursiva
print("========= Función recursiva para mostrar una lista de valores =========")

indeterminados = [1, 2, 3, 4, 5]
print(indeterminados)
IndeterminadosPosicionRecursivo(0, indeterminados)

# Determinar el número de alaninas ('A') en una secuencia de aminoácidos representada
# mediante un texto introducido por el telcado, uno por linea, con marca de fin #
print("========= Ejercicios de Iteración =========")

carToCount = 'A'
carToStop = '#'

car = input("Introduce un carácter: ")
count = 0

while car != carToStop:
    if car == carToCount:
        count += 1
        
    car = input("Introduce un carácter: ")

print(f"El número total de '{carToCount}' es: {count}.")

# El mismo bucle pero de forma recursiva
print("========= El mismo ejercicio pero recursivo =========")

count = RecursivoContarA(input("Introduce un carácter: "), 1)

print(f"El número total de '{carToCount}' es: {count}.")


# Contar las demás letras letras
print("========= El primer ejercicio pero contando más letras =========")

car = input("Introduce un carácter: ")
countA = 0
countT = 0
countG = 0
countC = 0

while car != carToStop:
    
    if car == 'A':
        countA += 1
    elif car == 'T':
        countT += 1
    elif car == 'G':
        countG += 1
    elif car == 'C':
        countC += 1
    else:
        print("Esa letra no está permitida. Solo se permite: A, T, G, C")

    car = input("Introduce un carácter: ")

print(f"El número total de 'A' es: {countA}.\nEl número total de 'T' es: {countT}\nEl número total de 'G' es: {countG}\nEl número total de 'C' es: {countC}")


