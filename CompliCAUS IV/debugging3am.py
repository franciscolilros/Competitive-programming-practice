# https://vjudge.net/contest/755576#problem/H

import sys

input = sys.stdin.readline

read = lambda:input().strip()
read_ints = lambda:list(map(int, read().split()))

def solve():
    n = read()
    cadena = read()
    res=0
    cont = 0
    L = False
    R = False
    for i in range(len(cadena)):
        if cadena[i] == ".":
            cont+=1
        elif cadena[i] == "L":
            if R:
                if cont %2 == 1:
                    res+=1
            cont = 0
            L = True
            R = False
        elif cadena[i] == "R":
            res += cont
            cont = 0
            R = True
            L = False


    if not R:
        res += cont


    print(res)

if __name__ == "__main__":
    solve()