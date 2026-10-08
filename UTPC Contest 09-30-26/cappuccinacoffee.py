import sys

read = lambda: sys.stdin.readline().strip()
read_ints = lambda: list(map(int, read().split()))




n = int(read())
nums = read_ints()


nums.sort()

pairs = []
for i in range(0, n-1):
    pairs.append(nums[i+1]-nums[i])


oddpairs = [0] 
for i in range(0, len(pairs), 2):
    oddpairs.append(oddpairs[-1] + pairs[i])

evenpairs = [0]
for i in range(len(pairs)-1, -1, -2):
    evenpairs.append(evenpairs[-1] + pairs[i])

evenpairs.reverse()

temp = []

for i in range(len(oddpairs)):
    temp.append(oddpairs[i] + evenpairs[i])

print(min(temp))