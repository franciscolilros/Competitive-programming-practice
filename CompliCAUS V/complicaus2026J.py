# https://open.kattis.com/contests/nwerc15open/problems/communication

from collections import defaultdict

n = map(int, input())

nums = list(map(int, input().split()))


expos = [2**7, 2**6, 2**5, 2**4, 2**3, 2**2, 2, 1]
mem = defaultdict()

for i in range(256):
    res = 0
    k = i
    temp = []
    for j in expos:
        if k>=j:
            k -= j
            temp.append(1)
        else:
            temp.append(0)
    
    temp2 = temp.copy()
    temp2.remove(temp2[0])
    temp2.append(0)

    for j, bit in enumerate(temp2):
        if temp[j] == bit:
            temp[j] = 0
        else:
            temp[j] = 1
    
    for j, e in enumerate(expos):
        if temp[j] == 1:
            res += e
        
    mem[res] = i


resultados = []
for i in nums:
    print(mem[i],end=" ")

#print(resultados.replace(",", " ").remove("[").remove("]"))