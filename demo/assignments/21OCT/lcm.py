n1 = 10
n2 = 75

# 3.9 features
# import math
#
# print(math.lcm(n1, n2))
# print(math.gcd(n1, n2))


big = n1 if n1 > n2 else n2

if big % n1 == 0 and big % n2 == 0:
    print(big)
    exit()  # terminate program

num = big * 2
while True:
    if num % n1 == 0 and num % n2 == 0:
        print(num)
        exit()

    num += big
