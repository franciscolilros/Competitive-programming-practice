# https://codeforces.com/problemset/problem/344/B

a, b, c = map(int, input().split())

suma = a + b + c
enlaces = suma/2
temp = [a, b, c]
res = [0, 0, 0]

if suma % 2 == 1:
    print("Impossible")

while enlaces > 0:
    if min(temp) == temp[0]:
        res[1] +=1
        temp[1] -=1
        temp[2] -=1
    elif min(temp) == temp[1]:
        res[2] +=1
        temp[0] -=1
        temp[2] -=1
    else:
        res[0] +=1
        temp[0] -=1
        temp[1] -=1
    enlaces -=1

if temp[0] == 0 & temp[1] == 0 & temp[2] ==0:
    print(res)
else:
    print("Impossible")