import random

# Dimensiones de la matriz (puedes cambiar el tamaño aquí)
N = 10

# Generar una matriz vacía con obstáculos aleatorios
matriz = [['o' for _ in range(N)] for _ in range(N)]

# Colocar obstáculos aleatoriamente (excepto en inicio y fin)
num_obstaculos = random.randint(5, 10)  # Número aleatorio de obstáculos
obstaculos = set()

while len(obstaculos) < num_obstaculos:
    x, y = random.randint(0, N-1), random.randint(0, N-1)
    if (x, y) not in [(0, 0), (N-1, N-1)]:  # Evitar inicio y fin
        matriz[x][y] = 'X'
        obstaculos.add((x, y))

# Posición inicial del robot
pos_x, pos_y = 0, 0

# Direcciones de movimiento (Derecha, Abajo, Izquierda, Arriba)
direcciones = [(0, 1, '→'), (1, 0, '↓'), (0, -1, '←'), (-1, 0, '↑')]
ruta = []
mapa_ruta = [[' ' for _ in range(N)] for _ in range(N)]

# Buscar camino usando una estrategia simple
def mover_robot(x, y):
    if (x, y) == (N-1, N-1):
        return True  # Llegamos al destino
    
    for dx, dy, simbolo in direcciones:
        nuevo_x, nuevo_y = x + dx, y + dy

        if 0 <= nuevo_x < N and 0 <= nuevo_y < N and matriz[nuevo_x][nuevo_y] == 'o':
            ruta.append((x, y, simbolo))
            matriz[x][y] = '.'  # Marcar como visitado
            if mover_robot(nuevo_x, nuevo_y):
                return True
            ruta.pop()  # Retroceder si es un callejón sin salida
    
    return False

# Ejecutar el movimiento del robot
exito = mover_robot(pos_x, pos_y)

# Imprimir el mapa inicial con obstáculos
print("\nMapa inicial:")
for fila in matriz:
    print(' '.join(fila))

if exito:
    print("\n ¡El robot llegó a su destino!\n")
    
    # Marcar la ruta en el mapa de flechas
    for x, y, simbolo in ruta:
        mapa_ruta[x][y] = simbolo

    # Imprimir el mapa con la ruta
    print("\nMapa con la ruta seguida:")
    for fila in mapa_ruta:
        print(' '.join(fila))

else:
    print("\n Imposible llegar al destino.")
