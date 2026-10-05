# https://vjudge.net/problem/CSES-1083

n = map(int, input())

nums = list(map(int, input().split()))

rango = [i + 1 for i in range(*n)]

for i in rango:
    if i not in nums:
        print(i)