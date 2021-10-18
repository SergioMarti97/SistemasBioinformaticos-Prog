import re
# Ejercicios de problemas python - Sistemas Bioinformaticos

# Ejercicio 1: estructura condicional if-else
#x = int(input("Introduce un número: "))
#y = int(input("Introduce un número: "))

#if x >= y:
#    z = x
#    print("El valor de \"x\" es %d, el valor de \"y\" es %d y el mayor es %d" % (x, y, z))
#else:
#    z = y
#    print(f"El valor de \"x\" es {x}, el valor de \"y\" es {y} y el mayor es {z}")
#
#print("El programa ha finalizado su ejecución")

# Problema 1 - Tema 1: Dados tres enteros diferentes, ordenese de mayor a menor:

x, y, z = 1, 2, 3

  # Ordenar a la antiguita
if x > y:
    temp = x
    x = y
    y = temp

if x > z:
    temp = x
    x = z
    z = temp

if y > z:
    temp = y
    y = z
    z = temp

print(f"Ordenados son: {x}, {y}, {z}")

  # Ordenar a la modernita
nums = [x, y, z]
nums.sort(reverse=False)
print(f"Ordenados son: {nums}")

  # La solución del profe según el análisis de casos (usando elif)
a, b, c = x, y, z
p, s, t = 0, 0, 0

if a < b < c: # Python permite condensar comparaciones, esto es igual que: "a < b and b < c"
    p, s, t = a, b, c
elif a < c < b:
    p, s, t = a, c, b
elif b < a < c:
    p, s, t = b, a, c
elif b < c < a:
    p, s, t = b, c, a
elif c < b < a:
    p, s, t = c, b, a
else:
    p, s, t = c, a, b

print(f"Ordenados son: {p}, {s}, {t}")

# Problema 2 - Tema 1: traductor de codones:
mapDNATranslate = {
    "UU[UC]" : "Fenilanina",   # 1
    "UU[AG]|CU." : "Leucina",  # 2
    "UC.|AG[UC]" : "Serina",   # 3
    "UA[UC]" : "Tirosina",     # 4
    "UA[AG]|UGA" : "Stop",     # 5 <- Stop
    "UG[UC]" : "Cisteina",     # 6
    "UGG" : "Triptofano",      # 7

    "CC." : "Prolina",         # 8
    "CA[UC]" : "Histidina",    # 9
    "CA[AG]" : "Glutamina",    # 10
    "CG.|AG[AG]" : "Arginina", # 11
    
    "AU[UCA]" : "Isoleucina",  # 12
    "AUG" : "Start",           # 13 <- Start
    "AC." : "Treonina",        # 14
    "AA[UC]" : "Asparagina",   # 15
    "AA[AG]" : "Lisina",       # 16
    
    "GU." : "valina",          # 17
    "GC." : "Alanina",         # 18
    "GA[UC]" : "Ác. aspártico",# 19
    "GA[AG]" : "Ác. glutámico",# 20
    "GG." : "Glicina"          # 21
}


# Esta función traduce un codon, usando un hash map (diccionario)
def translate_with_map(codon):
    for key in mapDNATranslate.keys():
        if re.match(key, codon):
            return mapDNATranslate.get(key)


codon = "UAA"
print(f"Codon: {codon}, Aminoácido: {translate_with_map(codon)}")


# Problema 1 - Tema 2: Crear una funciónpara sacar el valor máximo de 3 valores:

def Max3(x, y, z):
    if x > y > z or x > z > y:
        return x
    if y > x > z or y > z > x:
        return y
    if z > x > y or z > y > x:
        return z
    

str = "Introduce el valor de "
a, b, c = int(input(f"{str} a: ")), int(input(f"{str} b: ")), int(input(f"{str} c: ")) 

t = a + b + c - Max3(a, b, c)

if Max3(a, b, c) == a:
    a = a + 1

print(f"a: {a}, b: {b}, c: {c}\nValor máximo: {Max3(a, b, c)}\nValor de t: {t}")

