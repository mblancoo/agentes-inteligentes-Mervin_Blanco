import heapq

def navegar_laberinto():
    laberinto = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    inicio = (0, 0)
    meta = (4, 4)
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    heap = [(0, inicio)]
    visitados = {}
    visitados[inicio] = None
    
    while heap:
        _, actual = heapq.heappop(heap)
        if actual == meta:
            break
        for dx, dy in movimientos:
            nueva_pos = (actual[0] + dx, actual[1] + dy)
            if 0 <= nueva_pos[0] < 5 and 0 <= nueva_pos[1] < 5 and laberinto[nueva_pos[0]][nueva_pos[1]] == 0:
                if nueva_pos not in visitados:
                    visitados[nueva_pos] = actual
                    heapq.heappush(heap, (abs(nueva_pos[0] - meta[0]) + abs(nueva_pos[1] - meta[1]), nueva_pos))
    
    ruta = []
    actual = meta
    while actual:
        ruta.append(actual)
        actual = visitados[actual]
    ruta.reverse()
    print("Ruta encontrada:", ruta)

if __name__ == "__main__":
    navegar_laberinto()
