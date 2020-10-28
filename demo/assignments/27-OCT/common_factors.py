# Common factors for the given numbers

nums = [10, 35, 60]
factors = []
endvalue = min(nums) // 2 + 1

for i in range(2, endvalue):
    for n in nums:
        if n % i != 0:
            break
    else:
        factors.append(i)

print(factors)
