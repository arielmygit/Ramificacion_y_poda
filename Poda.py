# O(1)
laberinto = [
    # 0    1    2    3    4    5    6    7
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], #0
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], #1
    ['P', 'P', 'P', 'P', 'C', 'P', 'P', 'P'], #2
    ['P', 'C', 'C', 'C', 'C', 'C', 'C', 'P'], #3
    ['P', 'C', 'P', 'C', 'P', 'P', 'C', 'P'], #4
    ['P', 'C', 'P', 'C', 'P', 'P', 'C', 'P'], #5
    ['P', 'C', 'P', 'C', 'C', 'C', 'C', 'P'], #6
    ['P', 'C', 'P', 'C', 'P', 'P', 'C', 'P'], #7
    ['P', 'C', 'C', 'C', 'C', 'P', 'C', 'P'], #8
    ['P', 'P', 'P', 'P', 'C', 'P', 'C', 'S'], #9
    ['P', 'P', 'C', 'P', 'C', 'P', 'P', 'P'], #10
    ['P', 'C', 'C', 'C', 'C', 'C', 'P', 'P'], #11
    ['P', 'P', 'C', 'P', 'P', 'C', 'P', 'P'], #12
    ['P', 'P', 'E', 'P', 'P', 'P', 'P', 'S'], #13
]

def encontrar_posiciones(laberinto, simbolo):
    for i, fila in enumerate(laberinto): # O(n)
        for j, celda in enumerate(fila): # O(m)
            if celda == simbolo:         # O(1)
                return i, j
    return None

# Cálculo de la distancia Manhattan
def distancia_manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) # O(1)


def resolver_laberinto(laberinto):
    entrada = encontrar_posiciones(laberinto, 'E') # O(n*m)
    salida = encontrar_posiciones(laberinto, 'S')  # O(n*m)

    if not entrada or not salida: # O(1)
        return None

    visitados = set() # O(1)
    mejor_camino = [] # O(1)
    mejor_distancia = float('inf') # O(1)

    def busqueda_profunda(pos, camino, pasos):
        nonlocal mejor_camino, mejor_distancia

        if pos == salida: # O(1)
            if pasos < mejor_distancia: # O(1)
                mejor_distancia = pasos # O(1)
                mejor_camino = camino[:] # O(1)
            return

        if pasos + distancia_manhattan(pos, salida) >= mejor_distancia: # O(1)
            return
        visitados.add(pos) # O(1)

        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] # O(1)
        for dx, dy in movimientos: # O(n)
            nueva_pos = (pos[0] + dx, pos[1] + dy)
            if (0 <= nueva_pos[0] < len(laberinto) and # O(1)
                    0 <= nueva_pos[1] < len(laberinto[0]) and
                    nueva_pos not in visitados and
                    laberinto[nueva_pos[0]][nueva_pos[1]] in ('C', 'S')):

                camino.append(nueva_pos) # O(1)
                busqueda_profunda(nueva_pos, camino, pasos + 1) # O(K) recursivo
                camino.pop()# O(1)
        visitados.remove(pos) # O(1)

    busqueda_profunda(entrada, [entrada], 0)
    return mejor_camino

# Complejidad Big O = O(16+K+(n*m)) = O(n+m)

camino = resolver_laberinto(laberinto)
if camino:
    print("Camino encontrado:")
    for paso in camino:
        print(paso)
else:
    print("No se encontró un camino.")
