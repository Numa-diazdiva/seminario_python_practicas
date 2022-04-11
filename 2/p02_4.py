evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

limites_titulo1 = {"facil" : 12, "aceptable": 17, "dificil": 25}
limites_oraciones = dict(facil = range(0,13), aceptable = range(13,18), dificil = range(18,26))


dificultad_titulo = ""
dificultad_resumen = {"facil":0,"aceptable":0,"dificil":0,"muy_dificil":0}

# Primero separo el título del resúmen.
# Otra solución podría haber sido guardar los dos componentes de la lista que salen del split en variables por desestructuración
texto_separado = evaluar.split("resumen: ")
# Quito el string "título" que me queda de más, con un slicing.
texto_separado[0] = texto_separado[0][9:]
texto_separado[0].split()

long_tit = len(texto_separado[0].split())
if long_tit <= 10:
    dificultad_titulo = "aceptable"
else:
    dificultad_titulo = "no aceptable"

# Separo en oraciones el resumen
texto_separado[1] = texto_separado[1].split(".")
# Proceso las oraciones para saber qué dificultad tienen
for oracion in texto_separado[1]:
    long_or = len(oracion.split())
    match long_or:
        case long_or if long_or in limites_oraciones["facil"]:
            dificultad_resumen["facil"] += 1
        case long_or if long_or in limites_oraciones["aceptable"]:
            dificultad_resumen["aceptable"] += 1
        case lont_or if long_or in limites_oraciones["dificil"]:
            dificultad_resumen["dificil"] += 1
        case long_or if long_or > limites_oraciones["dificil"][-1]:
            dificultad_resumen["muy_dificil"] += 1


print(f"La cantidad de palabras del título es {dificultad_titulo}.")
print(f"La cantidad de oraciones fáciles de leer es {dificultad_resumen['facil']}, aceptables para leer: {dificultad_resumen['aceptable']}, difíciles de leer: {dificultad_resumen['dificil']}, muy difíciles de leer: {dificultad_resumen['muy_dificil']}")



