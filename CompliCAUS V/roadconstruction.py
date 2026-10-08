# https://vjudge.net/contest/786741#problem/G

import sys

input = sys.stdin.readline()

read = lambda: input().strip()
read_ints = lambda: list(map(int, read().split()))


def g(n, m):
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = read_ints()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

def solve():
    pass



if __name__ == "__main__":
    solve()
