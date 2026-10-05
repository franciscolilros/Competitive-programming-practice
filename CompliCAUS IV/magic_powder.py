# https://vjudge.net/problem/CodeForces-670D1

n, powder = map(int, input().split())

requirements = list(map(int, input().split()))

ingredients = list(map(int, input().split()))

while powder > 0:
    temp = []
    for i, ing in enumerate(ingredients):
        temp.append(ingredients[i]/requirements[i])
    
    ingredients[temp.index(min(temp))] += 1
    powder -= 1

for i, ing in enumerate(ingredients):
        temp.append(ingredients[i]/requirements[i])
print(int(min(temp)))