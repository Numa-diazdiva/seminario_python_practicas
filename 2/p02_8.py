# Checar que se ingresó una palabra
# Procesar cada letra de la palabra
#   Por cada letra, evaluar a qué grupo pertenece y sumar el puntaje al puntajeTotal

import string
from collections import Counter

puntaje_total = 0
tabla_puntajes = {"aeioulnrst" : 1, "dg": 2, "bcmp" : 3, "fhvwy" : 4, "k": 5, "jx" : 8, "qz": 10} 



# Utilizo un set para evaluar 
palabra = input("Ingrese una palabra para saber el puntaje: ")
while(not set(palabra).issubset(string.ascii_letters)):
    palabra = input("La palabra contiene caracteres no permitidos. Ingrese una palabra con únicamente letras: ")
palabra = palabra.lower()
# Utilizo un counter para contar las letras y procesarlas una sola vez (la otra solución es iterar por cada caracter de la palabra y buscarlo en el diccionario)
contador = Counter(palabra)
comunes = contador.most_common()
# Me guardo las keys del diccionario para buscar con mayor facilidad
claves = list(tabla_puntajes.keys())

for letra_tupla in comunes:
    i = 0
    while (not letra_tupla[0] in claves[i]):
        i += 1
    puntaje_total += letra_tupla[1] * tabla_puntajes[claves[i]]

print(f"La palabra que ingresó suma un total de {puntaje_total} puntos, de acuerdor con la tabla de puntajes del Scrabble.")

