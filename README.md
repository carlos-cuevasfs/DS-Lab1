# Práctica de Laboratorio - Resolución de Problemas en Python

## Introducción a Python

Python es un lenguaje de programación de alto nivel, interpretado y con tipado dinámico. Es ampliamente utilizado en desarrollo web, ciencia de datos, inteligencia artificial y muchas otras áreas. Sus principales características incluyen:

- **Tipos de variables**: Python soporta múltiples tipos de datos como:
  - `int`: Enteros
  - `float`: Números de punto flotante
  - `str`: Cadenas de texto
  - `bool`: Booleanos (`True` o `False`)
  - `list`, `tuple`, `dict`, `set`: Estructuras de datos para almacenar colecciones de valores

- **Estructuras de control**:
  - `for`: Se usa para iterar sobre una secuencia.
    ```python
    for i in range(5):
        print(i)  # Imprime los números del 0 al 4
    ```
  - `while`: Ejecuta un bloque de código mientras una condición sea verdadera.
    ```python
    x = 0
    while x < 5:
        print(x)
        x += 1  # Incrementa x en 1
    ```

- **Funciones**: Se definen con la palabra clave `def`.
  ```python
  def suma(a, b):
      return a + b

  print(suma(3, 5))  # Devuelve 8

---

## Programación Orientada a Objetos (POO) en Python

Python soporta la POO, la cual permite modelar objetos con atributos y comportamientos. Sus principales componentes son:

- **Clases**: Plantillas para crear objetos.
- **Objetos**: Instancias de una clase.
- **Atributos**: Variables dentro de una clase.
- **Métodos**: Funciones definidas dentro de una clase.
- **Encapsulamiento**: Restricción del acceso a ciertos datos.
- **Herencia**: Permite crear una nueva clase basada en otra.
- **Polimorfismo**: Diferentes clases pueden compartir métodos con el mismo nombre, pero con diferente comportamiento.

Ejemplo:
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Carlos", 25)
persona1.saludar()
```

---

## Problemas a Resolver

Se presentan diferentes problemas que deben resolverse utilizando Python:

### 1. Suma de números hasta `n`
**Descripción**: Escribir un programa que lea un número entero `n` e imprima la suma de todos los enteros desde 1 hasta `n`.  
**Solución**: Se solicitó un número n y se utilizó la fórmula de la suma de los primeros n enteros positivos para calcular el resultado de manera eficiente en O(1).  
**Código:**
```python
# Solicitar al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Verificar que el número sea positivo
if n > 0:
    # Calcular la suma de los primeros n enteros positivos
    suma = (n * (n + 1)) // 2  # Se usa // para asegurar que el resultado sea un entero
    print(f"La suma de los primeros {n} enteros positivos es: {suma}")
else:
    print("Por favor, ingrese un número entero positivo.")

```

### 2. Cálculo de sueldo de empleados
**Descripción**: Solicitar al usuario el número de horas trabajadas y el costo por hora, calcular la paga y gestionar una lista de empleados.  
**Solución**: Se pidió al usuario el número de horas trabajadas y la tarifa por hora, se multiplicaron estos valores y se imprimió el sueldo correspondiente.  
**Código:**
```python
# Lista de operadores con nombre, sueldo por hora y horas trabajadas
operadores = [
    ("Carlos", 10, 40),
    ("Ana", 12, 35),
    ("Luis", 15, 30),
    ("María", 11, 38),
    ("Pedro", 13, 42),
    ("Elena", 14, 36)
]

# Preguntar al usuario por sus datos
nombre_usuario = input("Ingrese su nombre: ")
horas_usuario = float(input("Ingrese el número de horas trabajadas: "))
sueldo_usuario = float(input("Ingrese su sueldo por hora: "))

# Calcular y mostrar el sueldo del usuario
pago_usuario = horas_usuario * sueldo_usuario
print(f"{nombre_usuario}, tu sueldo es: ${pago_usuario:.2f}")

# Imprimir la lista de operadores con sus sueldos
print("\n--- Sueldos de los operadores ---")
for nombre, sueldo_hora, horas in operadores:
    sueldo_total = sueldo_hora * horas
    print(f"{nombre}: ${sueldo_total:.2f}")

```

### 3. Promedio de pares y producto de impares
**Descripción**: Se debe calcular el promedio de los números pares y el producto de los impares de una lista de 10 números.  
**Solución**: Se utilizó una lista de números, se filtraron los pares y se calculó su promedio, mientras que los impares se multiplicaron entre sí.  
**Código:**  
```python
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

```

### 4. Adivina el número secreto
**Descripción**: El usuario debe adivinar un número aleatorio entre 1 y 10.  
**Solución**: Se generó un número aleatorio y se solicitó al usuario que intentara adivinarlo, proporcionando pistas hasta que acertara.  
**Código:**  
```python
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

```

### 5. Robot Explorador
**Descripción**: Se genera una matriz con obstáculos aleatorios. Un robot inicia en la esquina superior izquierda y debe encontrar su camino hasta la salida.  
**Solución**: Se generó una matriz con obstáculos aleatorios y se implementó una lógica para que el robot intentara encontrar un camino hacia la meta.  
**Código**: Esta disponible en el repositorio.


### 6. Gestión de Inventario
**Descripción**: Este programa permite gestionar productos en una tienda mediante un menú interactivo. Se implementa en POO con la clase Producto y la clase Inventario para almacenar y manipular productos.  
**Solución**: Se creó un sistema en Python utilizando POO, permitiendo agregar productos, venderlos, verificar disponibilidad e imprimir el inventario.  
**Código**: Esta disponible en el repositorio.

