# https://vjudge.net/problem/CSES-1094

n = map(int, input().split())

nums = list(map(int, input().split()))

res = 0

for i, k in enumerate(nums):
    if i == 0:
        pass
    elif nums[i-1] <= nums[i]:
        pass
    else:
        res += nums[i-1] - nums[i]
        nums[i] += nums[i-1] - nums[i]

print(res)
