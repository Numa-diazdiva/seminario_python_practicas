import string
from collections import Counter

numpy_readme_texto = """"NumPy is the fundamental package for scientific computing with Python.

    Website: https://www.numpy.org
    Documentation: https://numpy.org/doc
    Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion
    Source code: https://github.com/numpy/numpy
    Contributing: https://www.numpy.org/devdocs/dev/index.html
    Bug reports: https://github.com/numpy/numpy/issues
    Report a security vulnerability: https://tidelift.com/docs/security

It provides:

    a powerful N-dimensional array object
    sophisticated (broadcasting) functions
    tools for integrating C/C++ and Fortran code
    useful linear algebra, Fourier transform, and random number capabilities

Testing:

NumPy requires pytest and hypothesis. Tests can then be run after installation with:

python -c 'import numpy; numpy.test()'

Code of Conduct

NumPy is a community-driven open source project developed by a diverse group of contributors. The NumPy leadership has made a strong commitment to creating an open, inclusive, and positive community. Please read the NumPy Code of Conduct for guidance on how to interact with others in a way that makes our community thrive.
Call for Contributions

The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated; issues labeled as "good first issue" may be a good starting point. If you are considering larger contributions to the source code, please contact us through the mailing list first.

Writing code isn’t the only way to contribute to NumPy. You can also:

    review pull requests
    help us stay on top of new and old issues
    develop tutorials, presentations, and other educational materials
    maintain and improve our website
    develop graphic design for our brand assets and promotional materials
    translate website content
    help with outreach and onboard new contributors
    write grant proposals and help with other fundraising efforts

For more information about the ways you can contribute to NumPy, visit our website. If you’re unsure where to start or how your skills fit in, reach out! You can ask on the mailing list or here, on GitHub, by opening a new issue or leaving a comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to speak to us in private first, contact our community coordinators at numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for an invitation).

We also have a biweekly community call, details of which are announced on the mailing list. You are very welcome to join.

If you are new to contributing to open source, this guide helps explain why, what, and how to successfully get involved. """
# ----------------------------PUNTO1

# Separo el string en renglones y lo almaceno en una lista
readme_separado = numpy_readme_texto.split("\n")
print("Líneas que contienen direcciones con la cadena 'http' y 'https':")
# por cada línea busco la cadena
for linea in readme_separado:
    if (("https" in linea) or ("http" in linea)):
        print(linea)


# ----------------------------PUNTO2
#Indique la palabra que aparece mayor cantidad de veces en el texto del README.md de numpy.
print("---" * 20)
# reutilizo la variable para separar el texto original por palabras
readme_separado = numpy_readme_texto.lower().split()
contador = Counter(readme_separado)
palabra_mas_usada = contador.most_common(1)
print(f"La palabra que más veces aparece es: {palabra_mas_usada[0][0]}; con {palabra_mas_usada[0][1]} apariciones.")


#-----------------------------PUNTO3.
# Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha
#letra. En caso que no se haya ingresado una letra, indique el error. Ver: módulo string

texto = """Hacer nieve nunca había sido tan fácil, puedes preparar toda la receta una noche antes y disfrutarla al día siguiente
 para que la consistencia sea aún más firme. Y lo mejor de todo es que no solo puedes prepararla de un solo sabor, sino que hay 
 infinidad de sabores que puedes combinar, puedes optar por versiones naturales con fruta, u opciones más dulces como por ejemplo 
 dulce de leche, chocolate, leche condensada, entre otros. Destacamos que las calorías de la nieve de yogur son más bajas que las de un helado tradicional.
 Es por eso que en RecetasGratis te animamos a elaborar esta receta saludable y deliciosa."""

print("---" * 20)
print("Búsqueda de palabras que comienzan con la letra (ingrese la letra deseada): ")
l = input()
while (not l in string.ascii_letters):
    print("El caracter ingresado no es una letra. Por favor, ingrese una letra: ")
    l = input()

texto_procesado = texto.lower().split()
palabras_buscadas = list(filter(lambda x: x.startswith(l.lower()),texto_procesado))
print(palabras_buscadas)