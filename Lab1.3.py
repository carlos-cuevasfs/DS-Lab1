# Lista con al menos 10 números
numeros = [3, 8, 12, 7, 5, 10, 4, 15, 9, 6]

# Filtrar los números pares e impares
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

# Calcular el promedio de los números pares
if len(pares) > 0:
    promedio_pares = sum(pares) / len(pares)
else:
    promedio_pares = 0  # Si no hay pares, el promedio es 0

# Calcular el producto de los números impares
producto_impares = 1
for num in impares:
    producto_impares *= num

# Imprimir los resultados
print(f"Números en la lista: {numeros}")
print(f"Números pares: {pares}")
print(f"Promedio de los números pares: {promedio_pares:.2f}")
print(f"Números impares: {impares}")
print(f"Producto de los números impares: {producto_impares}")
