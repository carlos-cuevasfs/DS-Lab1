# Solicitar al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Verificar que el número sea positivo
if n > 0:
    # Calcular la suma de los primeros n enteros positivos
    suma = (n * (n + 1)) // 2  # Se usa // para asegurar que el resultado sea un entero
    print(f"La suma de los primeros {n} enteros positivos es: {suma}")
else:
    print("Por favor, ingrese un número entero positivo.")
