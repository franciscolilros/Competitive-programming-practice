#https://codeforces.com/gym/106733/problem/A

n = int(input())
letras = input()


cont=0
for i in range(n):
    if letras[i] == "C":
        cont+=1

res=0
for i in range(n):
    if (letras[i]=="C") and (i>=cont):
        res+=1


print(res)