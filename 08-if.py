puntaje = 97
if puntaje >= 95:
    print("Aprobado con honores") # indentation: "indentacion" o "sangrado". codigo anidado, se imprime en terminal si se cumple

print("---------------") # sin indentacion se imprime en terminal siempre

puntaje = 93
if puntaje >= 95:
    print("Aprobado con honores") #si condicion 1 se cumple no ejecuta ni cond2 o cond3
elif puntaje >= 50: #cond1 no se cumple entonces ejecuta cond2. si con2 se cumple no ejecuta cond3
    print("Alumno aprobado")
else: #cond3 se ejecuta cuando no se cumplen ni cond1 ni cond2
    print("Reprobado")