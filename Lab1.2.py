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
