temp = float(input("Ingrese la temperatura:"))
esc =input("Es Fahrenheit (F) o es Celsius (C)?:").lower()

if esc == "f":
    celsius = (temp - 32) * 5/9
    print(celsius)
elif esc == "c":
    farenheit = temp * 1.8 + 32
    print(farenheit)
else:
    print("Escala incorrecta")