from collections import Counter
from ctypes.wintypes import HLOCAL


cadena = input("Ingrese una palabra o frase para comprobar si es un heterograma: ")
cadena = cadena.lower()

contador = Counter(cadena)
print(contador.most_common(1))
if contador.most_common(1)[0][1] == 1:
    print("La palabra o frase ingresada es un heterograma.")
else:
    print("La palabra o frase ingresada no es un heterograma.")