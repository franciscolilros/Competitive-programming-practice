# https://vjudge.net/contest/755576#problem/F

import sys

input = sys.stdin.readline

read = lambda:input().strip()
read_ints = lambda:list(map(int, read().split()))

n, k = read_ints()
ing = read_ints()
tot = read_ints()

temp = []
for i in range(len(tot)):
    temp.append(tot[i]//ing[i])

while k > 0:
    a = min(temp)
    b = temp.index(a)
    tot[b]+=1
    temp[b] = tot[b]//ing[b]
    k-=1
    
a = min(temp)

print(a)