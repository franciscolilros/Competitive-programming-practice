import sys
input = sys.stdin.readline
read_ints = lambda: list(map(int, input().split()))

n, m, k = read_ints()
apps = sorted(read_ints())
apar = sorted(read_ints())

i = j = cont = 0
while i < n and j < m:
    if apar[j] < apps[i] - k:
        j += 1
    elif apar[j] > apps[i] + k:
        i += 1
    else:
        cont += 1
        i += 1
        j += 1

print(cont)