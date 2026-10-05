#https://codeforces.com/gym/106733/problem/B

import sys


# sys.stdin.readline acelera la lectura de datos para evitar TLE por entrada
read = lambda: sys.stdin.readline().strip()
tests = int(read())

res = []
for i in range(tests):
    temp, n = list(map(int, read().split()))
    nums = list(map(int, read().split()))
    nums.sort()

    total = 0
    cont = 0
    
    while total < temp:
        # Comprobamos que hay elementos en la lista y si son rentables
        if nums and nums[-1] - cont >= 2:
            total += nums[-1] - cont
            nums.pop()
            cont += 1
        else:
            # Salto matemático O(1): calculamos lo que falta de golpe
            faltantes = temp - total
            cont += faltantes
            break  # Como ya habríamos sumado los faltantes al total, terminamos el bucle

    res.append(cont)

for i in res:
    print(i)