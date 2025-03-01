import random
import heapq

def seleccionar_ruta():
    tamaño = 5
    mapa = [[random.randint(1, 10) for _ in range(tamaño)] for _ in range(tamaño)]
    inicio = (0, 0)
    meta = (4, 4)
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    heap = [(-mapa[0][0], inicio)]  # Negativo para max heap
    visitados = {}
    visitados[inicio] = None
    
    while heap:
        utilidad, actual = heapq.heappop(heap)
        if actual == meta:
            break
        for dx, dy in movimientos:
            nueva_pos = (actual[0] + dx, actual[1] + dy)
            if 0 <= nueva_pos[0] < tamaño and 0 <= nueva_pos[1] < tamaño:
                if nueva_pos not in visitados:
                    visitados[nueva_pos] = actual
                    heapq.heappush(heap, (-mapa[nueva_pos[0]][nueva_pos[1]], nueva_pos))
    
    ruta = []
    actual = meta
    while actual:
        ruta.append(actual)
        actual = visitados[actual]
    ruta.reverse()
    print("Ruta óptima encontrada:", ruta)

if __name__ == "__main__":
    seleccionar_ruta()
