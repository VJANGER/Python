resultado = input("Ingresa tu edad:")
print(type(resultado)) #en consola muestra que el input espera un string 'str'
numero = int(resultado) #int transforma un str a un num
print(numero + 2)
# str(22) pasa de int a str
# float(22.23) pasa a decimales un int o str
# bool(" ") pasa a true/false lo que le pasemos (str, int o float). todos los valores son true menos bool false, 0, " "(str vacio) y objeto none
