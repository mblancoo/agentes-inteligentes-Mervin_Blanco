import random

def exploracion():
    tamaño = 5
    visitados = set()
    posicion = (0, 0)
    
    for _ in range(15):
        print(f"Agente en {posicion}")
        visitados.add(posicion)
        
        posibles_movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(posibles_movimientos)
        
        for dx, dy in posibles_movimientos:
            nueva_pos = (posicion[0] + dx, posicion[1] + dy)
            if 0 <= nueva_pos[0] < tamaño and 0 <= nueva_pos[1] < tamaño and nueva_pos not in visitados:
                posicion = nueva_pos
                break

if __name__ == "__main__":
    exploracion()
