import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Inicializar el contador de intentos
intentos = 0
adivinado = False

print(" ¡Adivina el número secreto entre 1 y 10!")

# Bucle while hasta que el usuario adivine
while not adivinado:
    try:
        # Pedir al usuario un número
        numero_usuario = int(input("Ingresa tu número: "))
        intentos += 1  # Contar intentos

        # Verificar si el número es correcto
        if numero_usuario < numero_secreto:
            print(" Muy bajo, intenta de nuevo.")
        elif numero_usuario > numero_secreto:
            print(" Muy alto, intenta de nuevo.")
        else:
            print(f" ¡Felicidades! Adivinaste el número en {intentos} intentos.")
            adivinado = True  # Salir del bucle

    except ValueError:
        print(" Ingresa un número válido.")
