import random

def patrullaje():
    ruta = ["A", "B", "C", "D", "E"]
    posicion = 0
    direccion = 1  # 1 para adelante, -1 para atrás
    
    for _ in range(10):
        print(f"Agente en {ruta[posicion]}")
        if random.random() < 0.2:  # 20% de probabilidad de obstáculo
            direccion = random.choice([-1, 1])
            print("¡Obstáculo encontrado! Cambio de dirección.")
        
        posicion = (posicion + direccion) % len(ruta)

if __name__ == "__main__":
    patrullaje()