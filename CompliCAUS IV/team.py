# https://vjudge.net/contest/755576#problem/D

import sys

input = sys.stdin.readline

read = lambda:input().strip()
read_ints = lambda:list(map(int, read().split()))

n = int(read())

cont = 0
for i in range(n):
    a, b, c = read_ints()
    if a + b + c >=2:
        cont+=1

print(cont)