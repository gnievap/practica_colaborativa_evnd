# Programa básico en Python

# Solicitar datos al usuario
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))

# Mostrar un mensaje
print("Hola,", nombre, "tienes", edad, "años.")

# Condicional simple
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")