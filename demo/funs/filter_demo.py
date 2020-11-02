def iseven(n):
    # print(n, end=' ')
    return n % 2 == 0


nums = [10, 20, 15, 45, 35, 60, 100, 99, 23, 88]

# evens = []
# for n in nums:
#     if n % 2 == 0:
#         evens.append(n)

for n in filter(iseven, nums):
   print(n)

