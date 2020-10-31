def count_pos_neg(nums):
    pos = neg = 0
    for n in nums:
        if n >= 0:
            pos += 1
        else:
            neg += 1

    return (pos, neg)


numbers = [10, -10, -9, -8, 6, 7, 8, 77]
print(count_pos_neg(numbers))
