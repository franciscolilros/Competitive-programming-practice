# https://codeforces.com/gym/106733/problem/C

import sys
from heapq import heappush, heappop
# Aumentar límite de recursión y activar Fast I/O
input = sys.stdin.readline
# Atajos para lectura rápida
read = lambda: input().strip()
read_ints = lambda: list(map(int, read().split()))

def solve():
    n, s = read_ints()

    grafo = leer_grafo_no_dirigido_ponderado(n,s)


    lista = dijsktra(grafo, 0, n-1)

    print(lista[-1])

def leer_grafo_no_dirigido_ponderado(V, E):

    AL = [[] for _ in range(V)]
    for _ in range(E):
        temp = read_ints()
        u, v, w = temp[0]-1, temp[1]-1, temp[2]
        AL[u].append((v, w)) # u -> v con peso w
        AL[v].append((u, w)) # v -> u con peso w
    return AL

def dijsktra(al, s, destino):
    dist = [float("inf")] * len(al)
    dist[s]=0
    pq = [(0,s)]
    while 0 < len(pq):
        d, u = heappop(pq)

        if u == destino:
            break

        if d > dist[u]:
            continue

        for v, w in al[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heappush(pq, (dist[v], v))
    return dist


if __name__ == "__main__":
    solve()
