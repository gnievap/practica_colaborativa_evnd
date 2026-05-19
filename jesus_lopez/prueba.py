# Programa básico en Python con menú

def saludar():
    nombre = input("¿Cuál es tu nombre? ")
    print("¡Hola,", nombre, "! Bienvenido al programa.")

def calcular_area_rectangulo():
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))
    area = base * altura
    print("El área del rectángulo es:", area)

def contar_hasta_n():
    n = int(input("¿Hasta qué número quieres contar? "))
    for i in range(1, n + 1):
        print(i)

def verificar_edad():
    edad = int(input("¿Cuántos años tienes? "))
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

# Menú principal
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saludar")
    print("2. Calcular área de rectángulo")
    print("3. Contar hasta N")
    print("4. Verificar edad")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        saludar()
    elif opcion == "2":
        calcular_area_rectangulo()
    elif opcion == "3":
        contar_hasta_n()
    elif opcion == "4":
        verificar_edad()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida, intenta de nuevo.")