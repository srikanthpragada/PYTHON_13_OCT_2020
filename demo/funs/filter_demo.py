def iseven(n):
    # print(n, end=' ')
    return n % 2 == 0


# Returns true if number has digit 0
def haszero(n):
    for c in str(n):
        if c == '0':
            return True

    return False


nums = [10, 20, 15, 45, 35, 60, 100, 99, 23, 88]

# evens = []
# for n in nums:
#     if n % 2 == 0:
#         evens.append(n)

# for n in filter(iseven, nums):
#     print(n)

for c in filter(str.isupper, "AbcDef"):
    print(c)

for n in filter(haszero, nums):
    print(n)
