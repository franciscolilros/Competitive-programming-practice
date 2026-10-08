import sys
from bisect import bisect_left, bisect_right

def solve():
    # Optimización de lectura para Codeforces
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    T = int(input_data[2])
    
    # Leer y ordenar los eventos
    events_input = []
    idx = 3
    for _ in range(n):
        events_input.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2
        
    events_input.sort()
    
    # 1. Fusionar eventos que compartan extremos (ej: [0, 10] y [10, 20] -> [0, 20])
    events = []
    for l, r in events_input:
        if not events:
            events.append([l, r])
        elif l <= events[-1][1]:
            events[-1][1] = max(events[-1][1], r)
        else:
            events.append([l, r])
            
    n = len(events)
    L = [e[0] for e in events]
    R = [e[1] for e in events]
    
    # 2. Prefix Sums: precalcular la suma de longitudes de los eventos
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + (R[i] - L[i])
        
    # Matriz DP: dp[i][j] -> max solape desde el evento i usando j comandos
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Llenamos el DP de atrás hacia adelante (Bottom-Up)
    for i in range(n - 1, -1, -1):
        for j in range(1, k + 1):
            
            # Opción 1: No hacer nada en este evento
            res = dp[i+1][j]
            
            # Opción 2: Usar 'c' comandos seguidos empezando en L[i]
            for c in range(1, j + 1):
                X = L[i] + c * T # El momento exacto en que se apagará el PC
                
                # Encontrar 'm', el último evento que empezó antes o a la vez que X
                m = bisect_right(L, X) - 1
                
                # El solape es la suma completa de los eventos intermedios + la parte cubierta del evento 'm'
                overlap = pref[m] - pref[i] + max(0, min(X, R[m]) - L[m])
                
                # Encontrar el siguiente evento al que saltar (el primero que empieza en X o después)
                next_idx = bisect_left(L, X)
                
                # Actualizar el máximo
                current = overlap + dp[next_idx][j - c]
                if current > res:
                    res = current
                    
                # Si nuestra cadena de comandos ya cubre hasta el final del último evento,
                # no tiene sentido gastar más comandos desde aquí (c más grandes no darán más solape)
                if X >= R[-1]:
                    break
                    
            dp[i][j] = res
            
    # La respuesta es el máximo solape considerando todos los eventos y 'k' comandos
    print(dp[0][k])

if __name__ == '__main__':
    solve()