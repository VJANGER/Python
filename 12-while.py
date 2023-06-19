leng = ["Python", "Ruby", "PHP", "Javascript", "Java"]

i = 1 # "i" es el valor inicial. se utiliza "i" como nombre de la variable
while i <= 5:
    print(i)
    i = i + 1 # no olvidar poner condicion de salida. sino es un bucle infinito y consume toda la memoria del server. i = 1, si es menor a 5 pasa a la condicion y suma i = i(que vale 1) + 1, da como resultado 2 y vuelve a arrancar el bucle while. asi hasta llegar al 6 y ahi se corta el bucle

i = 1
while i <= 5:
    print(i * "El weta ") # funciona igual pero para agregar un str a otro str
    i = i + 1

# para ingresar a los elementos de un listado

i = 0 # el valor inicial de una lista es 0
while i < len(leng):
    print(leng[i])
    i = i + 1