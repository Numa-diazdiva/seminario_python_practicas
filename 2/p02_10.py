"""
• Generar una estructura con los nombres de los estudiantes y la suma de ambas notas.
• Calcular el promedio de las notas totales e informar que alumnos obtuvieron menos que el
promedio.
"""

# Genero un diccionario para guardar las notas para poder usarlas en el programa
suma_notas = {}

archivo_nombres = open("./archivos/nombres_1.txt","r")
archivo_nota1 = open("./archivos/eval1.txt","r")
archivo_nota2 = open("./archivos/eval2.txt", "r")


lista_nombres = archivo_nombres.read().replace("'","").replace(",","").split()
lista_notas_1 = archivo_nota1.read().replace(",","").split()
lista_notas_2 = archivo_nota2.read().replace(",","").split()


#suma_notas[lista_nombres[1]] = int(lista_notas_1[1]) + int(lista_notas_2[1])

suma_total = 0
for i in range(len(lista_nombres)):
    suma_notas[lista_nombres[i]] = int(lista_notas_1[i]) + int(lista_notas_2[i])
    suma_total += suma_notas[lista_nombres[i]]

promedio_total = suma_total / len(lista_nombres)
print(f"El promedio de todas las notas es de: {round(promedio_total,2)}")
for alumn in suma_notas:
    if suma_notas[alumn] < promedio_total:
        print(f"El alumn {alumn} obtuvo menor nota que el promedio ({suma_notas[alumn]})")


#print(lista[0][1:-2])
