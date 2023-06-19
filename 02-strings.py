texto = "Hola Mundo"
print(texto.upper()) #metodos: menu contextual luego de tipear ".". upper es un metodo
print(texto.lower())
print(texto.find("Mun")) #find devuelve el indice. python es case sensitive
print(texto.find("mun")) #python es case sensitive
nuevoTexto = texto.replace("Mun", "chanchito feliz")
print(texto, nuevoTexto)
print("Mundo" in texto) #in devuelve un booleano (bool) true/false